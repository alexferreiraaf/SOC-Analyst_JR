import requests
import csv
import time
import json
from datetime import datetime

# --- CONFIGURAÇÕES DO MINI-SOC ---
ARQUIVO_ENTRADA = "suspeitos.txt"
ARQUIVO_SAIDA = "relatorio_final_soc.csv"
API_KEY_ABUSE = "660400690376c9a376e984ceab851d07d33e7c7f1040c960b062d30e9c1c3b888c79495ed72ede27"  # 🔑 Insira sua chave do AbuseIPDB aqui

# Limites para considerar um IP perigoso
LIMITE_SCORE_RISCO = 20  # Se a pontuação for maior que 20, gera alerta

def consultar_ipinfo(ip):
    """Consulta dados de geolocalização e organização (ASN)."""
    # Ignora IPs de rede interna
    if ip.startswith(("192.168.", "10.", "172.16.", "127.")):
        return {"pais": "LAN", "org": "Rede Interna", "cidade": "Local"}

    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                "pais": data.get("country", "Desconhecido"),
                "org": data.get("org", "Desconhecido"),
                "cidade": data.get("city", "Desconhecido")
            }
    except Exception:
        pass
    return {"pais": "Erro", "org": "Erro", "cidade": "Erro"}

def consultar_abuseipdb(ip, api_key):
    """Consulta a reputação de segurança do IP."""
    if api_key == "660400690376c9a376e984ceab851d07d33e7c7f1040c960b062d30e9c1c3b888c79495ed72ede27" or ip.startswith(("192.168.", "10.")):
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
                "uso": data.get("usageType", "Desconhecido")
            }
    except Exception:
        pass
    return {"score": 0, "reports": 0, "uso": "Erro"}

def main():
    print(f"🛡️  INICIANDO ANALISADOR MINI-SOC v1.0")
    print(f"📂 Lendo suspeitos de: {ARQUIVO_ENTRADA}...\n")

    ips_para_analise = []
    try:
        with open(ARQUIVO_ENTRADA, "r") as f:
            ips_para_analise = [linha.strip() for linha in f if linha.strip()]
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{ARQUIVO_ENTRADA}' não encontrado.")
        return

    dados_consolidados = []

    # Cabeçalho visual
    print(f"{'STATUS':<10} | {'IP':<16} | {'PAÍS':<5} | {'DETALHES'}")
    print("-" * 60)

    for ip in ips_para_analise:
        # 1. Consultas nas APIs
        info_geo = consultar_ipinfo(ip)
        info_risk = consultar_abuseipdb(ip, API_KEY_ABUSE)

        # 2. Lógica de Alerta (SOC Decision Making)
        score = info_risk["score"]
        pais = info_geo["pais"]
        reports = info_risk["reports"]
        
        # Define o ícone e a mensagem baseada no risco
        if score > LIMITE_SCORE_RISCO:
            status_icon = "⚠️ ALERTA"
            msg_detalhe = f"Risco Alto ({score}%) — {reports} relatos de abuso"
            cor = "\033[91m" # Vermelho (ANSI code)
        elif score > 0:
            status_icon = "👀 SUSPEITO"
            msg_detalhe = f"Risco Baixo ({score}%)"
            cor = "\033[93m" # Amarelo
        else:
            status_icon = "✅ LIMPO"
            msg_detalhe = "Nenhum risco detectado"
            cor = "\033[92m" # Verde

        reset_cor = "\033[0m"

        # 3. Exibe no Console (Com cores se o terminal suportar)
        print(f"{cor}{status_icon:<10} | {ip:<16} | {pais:<5} | {msg_detalhe}{reset_cor}")

        # 4. Prepara dados para o CSV
        dados_consolidados.append({
            "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "IP": ip,
            "País": pais,
            "Cidade": info_geo["cidade"],
            "Organização": info_geo["org"],
            "Risco (%)": score,
            "Denúncias": reports,
            "Tipo de Uso": info_risk["uso"]
        })

        # Pausa para respeitar as APIs
        time.sleep(1)

    # 5. Geração do Relatório CSV
    if dados_consolidados:
        try:
            with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as csvfile:
                campos = ["Data", "IP", "País", "Cidade", "Organização", "Risco (%)", "Denúncias", "Tipo de Uso"]
                writer = csv.DictWriter(csvfile, fieldnames=campos)
                writer.writeheader()
                writer.writerows(dados_consolidados)
            print(f"\n📄 Relatório consolidado salvo em: {ARQUIVO_SAIDA}")
        except Exception as e:
            print(f"Erro ao salvar CSV: {e}")

if __name__ == "__main__":
    main()
