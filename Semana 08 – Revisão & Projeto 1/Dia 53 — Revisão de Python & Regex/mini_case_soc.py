import re
import json
import time
from collections import Counter
from datetime import datetime

# Tenta importar bibliotecas externas
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

# --- CONFIGURAÇÃO ---
LOG_FILE = "auth_sample.log"
REPORT_FILE = "relatorio_final_soc.md"
API_URL = "http://ip-api.com/json/"

def get_geoip(ip):
    """Consulta API pública para GeoIP (requer internet)."""
    if ip.startswith(("192.168.", "10.", "172.16.", "127.")):
        return "Rede Interna (LAN)"
    
    if not REQUESTS_AVAILABLE:
        return "N/A (Instale 'requests')"

    try:
        time.sleep(0.5) # Rate limit
        resp = requests.get(f"{API_URL}{ip}", timeout=2)
        if resp.status_code == 200:
            data = resp.json()
            if data['status'] == 'success':
                return f"{data['country']} ({data['countryCode']})"
        return "Desconhecido"
    except:
        return "Erro de Conexão"

def analisar_logs():
    print(f"🔍 Iniciando análise forense em {LOG_FILE}...")
    
    try:
        with open(LOG_FILE, 'r') as f:
            conteudo = f.readlines()
    except FileNotFoundError:
        print("❌ Erro: Arquivo de log não encontrado.")
        return

    # Regex para extrair: Data, Usuário, IP
    regex = re.compile(r"(\w{3}\s+\d+\s[\d:]+).*Failed password for (?:invalid user )?(\w+) from (\d{1,3}(?:\.\d{1,3}){3})")
    
    dados_ataque = []
    ips_list = []

    for linha in conteudo:
        match = regex.search(linha)
        if match:
            data, user, ip = match.groups()
            dados_ataque.append({'data': data, 'user': user, 'ip': ip})
            ips_list.append(ip)

    # 1. Identificar Top 3 IPs
    contagem = Counter(ips_list)
    top_3 = contagem.most_common(3)
    
    if not top_3:
        print("✅ Nenhuma falha de login encontrada.")
        return

    print(f"⚠️  Top 3 Atacantes identificados: {[ip for ip, qtd in top_3]}")

    # 2. Enriquecimento (GeoIP) e Evidências
    analise_detalhada = []
    for ip, qtd in top_3:
        pais = get_geoip(ip)
        
        # Coleta evidências específicas deste IP
        evidencias_ip = [d for d in dados_ataque if d['ip'] == ip]
        usuarios_tentados = list(set([d['user'] for d in evidencias_ip])) # Remove duplicados
        horarios = [d['data'] for d in evidencias_ip]
        
        analise_detalhada.append({
            'ip': ip,
            'qtd': qtd,
            'pais': pais,
            'users': usuarios_tentados[:5], # Top 5 users tentados
            'inicio': horarios[0],
            'fim': horarios[-1]
        })

    # 3. Gerar Relatório Markdown
    gerar_markdown(analise_detalhada)

    # 4. Gerar Gráfico
    if MATPLOTLIB_AVAILABLE:
        gerar_grafico(top_3)

def gerar_markdown(dados):
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("# 🛡️ Relatório de Incidente: Análise de Tentativas SSH\n")
        f.write(f"**Data da Análise:** {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
        
        f.write("## 1. Resumo Executivo\n")
        f.write("Foram detectadas múltiplas tentativas de autenticação falha no servidor. ")
        f.write("A análise identificou os 3 principais vetores de ataque listados abaixo.\n\n")
        
        f.write("## 2. Top 3 Origens de Ataque\n")
        f.write("| Rank | Endereço IP | País de Origem | Tentativas | Status |\n")
        f.write("|---|---|---|---|---|\n")
        
        paises = set()
        for i, item in enumerate(dados, 1):
            f.write(f"| #{i} | **{item['ip']}** | {item['pais']} | {item['qtd']} | 🔴 Crítico |\n")
            paises.add(item['pais'])
        
        f.write("\n### Observação de Origem\n")
        if len(paises) == 1:
            f.write(f"ℹ️ **Ataque Coordenado:** Todos os IPs pertencem à mesma região ({list(paises)[0]}).\n")
        else:
            f.write("ℹ️ **Ataque Distribuído:** Os ataques originaram-se de múltiplas regiões.\n")

        f.write("\n## 3. Evidências Técnicas e IoCs\n")
        for item in dados:
            f.write(f"### Alvo: {item['ip']} ({item['pais']})\n")
            f.write(f"- **Total de Falhas:** {item['qtd']}\n")
            f.write(f"- **Janela de Tempo:** {item['inicio']} até {item['fim']}\n")
            f.write(f"- **Usuários Alvo:** `{', '.join(item['users'])}`\n\n")

        f.write("---\n*Relatório gerado automaticamente pelo Python SOC Tool.*\n")
    
    print(f"✅ Relatório salvo em: {REPORT_FILE}")

def gerar_grafico(top_3):
    ips = [ip for ip, qtd in top_3]
    qtds = [qtd for ip, qtd in top_3]
    
    plt.figure(figsize=(8, 5))
    plt.bar(ips, qtds, color=['#c0392b', '#e67e22', '#f1c40f'])
    plt.title("Top 3 Fontes de Ataque SSH")
    plt.xlabel("IP de Origem")
    plt.ylabel("Tentativas Bloqueadas")
    plt.grid(axis='y', alpha=0.3)
    print("📊 Exibindo gráfico...")
    plt.show()

if __name__ == "__main__":
    analisar_logs()