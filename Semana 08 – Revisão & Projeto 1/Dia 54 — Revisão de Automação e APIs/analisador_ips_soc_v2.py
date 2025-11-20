import requests
import csv
import time
import json
from datetime import datetime

# --- CONFIGURAÇÕES DO MINI-SOC ---
ARQUIVO_ENTRADA = "suspeitos.txt"
ARQUIVO_SAIDA = "relatorio_final_soc.csv"
ARQUIVO_HTML = "dashboard_soc.html"

# 🔑 CHAVES DE API (Substitua pelas suas)
API_KEY_ABUSE = "SUA API-AQUI" 
DISCORD_WEBHOOK = ""  # Cole seu Webhook do Discord aqui para ativar

# Limites de Risco
LIMITE_SCORE_RISCO = 20

# Tenta importar Rich para visualização profissional
try:
    from rich.console import Console
    from rich.table import Table
    from rich import print as rprint
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

# --- FUNÇÕES DE CONSULTA ---
def consultar_ipinfo(ip):
    if ip.startswith(("192.168.", "10.", "172.16.", "127.")):
        return {"pais": "LAN", "org": "Rede Interna", "cidade": "Local"}
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                "pais": data.get("country", "N/A"),
                "org": data.get("org", "N/A"),
                "cidade": data.get("city", "N/A")
            }
    except: pass
    return {"pais": "Erro", "org": "Erro", "cidade": "Erro"}

def consultar_abuseipdb(ip, api_key):
    if api_key == "SUA API-AQUI" or ip.startswith(("192.168.", "10.")):
        return {"score": 0, "reports": 0, "uso": "N/A"}
    
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {'Key': api_key, 'Accept': 'application/json'}
    params = {'ipAddress': ip, 'maxAgeInDays': 90}
    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return {
                "score": data.get("abuseConfidenceScore", 0),
                "reports": data.get("totalReports", 0),
                "uso": data.get("usageType", "N/A")
            }
    except: pass
    return {"score": 0, "reports": 0, "uso": "Erro"}

# --- FUNÇÕES BÔNUS (DISCORD & HTML) ---
def alertar_discord(ip, dados_geo, dados_risk):
    """Envia um card elegante para o Discord via Webhook."""
    if not DISCORD_WEBHOOK: return

    cor = 15158332 if dados_risk['score'] > LIMITE_SCORE_RISCO else 16776960 # Vermelho ou Amarelo
    
    payload = {
        "username": "SOC Bot 🤖",
        "embeds": [{
            "title": f"🚨 Alerta de Ameaça Detectada: {ip}",
            "description": "O sistema detectou um IP com reputação maliciosa.",
            "color": cor,
            "fields": [
                {"name": "🌍 Origem", "value": f"{dados_geo['cidade']}, {dados_geo['pais']}", "inline": True},
                {"name": "🔥 Risco", "value": f"{dados_risk['score']}/100", "inline": True},
                {"name": "🏢 ISP/Org", "value": dados_geo['org'], "inline": False},
                {"name": "⚠️ Denúncias", "value": str(dados_risk['reports']), "inline": True}
            ],
            "footer": {"text": f"Mini-SOC Automation • {datetime.now().strftime('%H:%M')}"}
        }]
    }
    try:
        requests.post(DISCORD_WEBHOOK, json=payload)
    except Exception as e:
        print(f"Erro Discord: {e}")

def gerar_dashboard_html(dados_consolidados):
    """Gera uma página HTML moderna com os resultados."""
    linhas_html = ""
    for d in dados_consolidados:
        classe_risco = "bg-red-100 text-red-800" if d['Risco (%)'] > LIMITE_SCORE_RISCO else "bg-green-100 text-green-800"
        if 0 < d['Risco (%)'] <= LIMITE_SCORE_RISCO: classe_risco = "bg-yellow-100 text-yellow-800"
        
        linhas_html += f"""
        <tr class="hover:bg-gray-50">
            <td class="px-6 py-4 font-medium text-gray-900">{d['IP']}</td>
            <td class="px-6 py-4">{d['País']}</td>
            <td class="px-6 py-4">{d['Organização']}</td>
            <td class="px-6 py-4"><span class="px-2 py-1 rounded-full text-xs font-semibold {classe_risco}">{d['Risco (%)']}%</span></td>
            <td class="px-6 py-4">{d['Denúncias']}</td>
        </tr>
        """

    html_template = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Dashboard Mini-SOC</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-100 p-8">
        <div class="max-w-6xl mx-auto bg-white rounded-lg shadow-lg p-6">
            <div class="flex justify-between items-center mb-6">
                <h1 class="text-3xl font-bold text-gray-800">🛡️ Dashboard de Inteligência de Ameaças</h1>
                <span class="text-sm text-gray-500">Atualizado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}</span>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-sm text-left text-gray-500">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                        <tr>
                            <th class="px-6 py-3">Endereço IP</th>
                            <th class="px-6 py-3">País</th>
                            <th class="px-6 py-3">Organização</th>
                            <th class="px-6 py-3">Score de Risco</th>
                            <th class="px-6 py-3">Relatos de Abuso</th>
                        </tr>
                    </thead>
                    <tbody>
                        {linhas_html}
                    </tbody>
                </table>
            </div>
        </div>
    </body>
    </html>
    """
    with open(ARQUIVO_HTML, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"🌐 Dashboard HTML gerado: {ARQUIVO_HTML}")

# --- MAIN ---
def main():
    console = Console() if RICH_AVAILABLE else None
    
    if RICH_AVAILABLE:
        console.print("[bold blue]🛡️  INICIANDO ANALISADOR MINI-SOC v2.0 (PRO)[/bold blue]")
        tabela = Table(show_header=True, header_style="bold magenta")
        tabela.add_column("Status", justify="center")
        tabela.add_column("IP", style="cyan")
        tabela.add_column("País")
        tabela.add_column("Detalhes")
    else:
        print("🛡️  INICIANDO ANALISADOR MINI-SOC v2.0")

    try:
        with open(ARQUIVO_ENTRADA, "r") as f:
            ips = [l.strip() for l in f if l.strip()]
    except: return

    dados_finais = []

    for ip in ips:
        geo = consultar_ipinfo(ip)
        risk = consultar_abuseipdb(ip, API_KEY_ABUSE)
        
        score = risk['score']
        
        # Lógica de Status
        if score > LIMITE_SCORE_RISCO:
            status = "🔴 CRÍTICO"
            detalhe = f"Risco Alto ({score}%)"
            alertar_discord(ip, geo, risk) # Dispara Webhook
        elif score > 0:
            status = "🟡 SUSPEITO"
            detalhe = f"Risco Baixo ({score}%)"
        else:
            status = "🟢 LIMPO"
            detalhe = "Seguro"

        # Output Visual
        if RICH_AVAILABLE:
            tabela.add_row(status, ip, geo['pais'], detalhe)
        else:
            print(f"{status} | {ip} | {geo['pais']} | {detalhe}")
        
        dados_finais.append({
            "IP": ip, "País": geo['pais'], "Organização": geo['org'],
            "Risco (%)": score, "Denúncias": risk['reports'], "Data": datetime.now().strftime("%Y-%m-%d")
        })
        time.sleep(1)

    # Exibe tabela final se usar Rich
    if RICH_AVAILABLE:
        console.print(tabela)

    # Gera arquivos
    gerar_dashboard_html(dados_finais)
    
    # Salva CSV (código resumido para brevidade)
    try:
        with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=dados_finais[0].keys())
            w.writeheader()
            w.writerows(dados_finais)
        print(f"📄 CSV Salvo: {ARQUIVO_SAIDA}")
    except: pass

if __name__ == "__main__":
    main()
