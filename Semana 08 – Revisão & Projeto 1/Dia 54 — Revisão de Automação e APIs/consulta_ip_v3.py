import requests
import json
import csv
from datetime import datetime

# --- CONFIGURAÇÃO ---
ALVO = "8.8.8.8"  # IP para consulta (DNS Google como exemplo)
ABUSE_IPDB_KEY = "660400690376c9a376e984ceab851d07d33e7c7f1040c960b062d30e9c1c3b888c79495ed72ede27"  # ⚠️ Insira sua API Key do AbuseIPDB aqui

def get_geoip(ip):
    """Consulta dados geográficos no ipinfo.io (Não requer chave para baixo volume)"""
    url = f"https://ipinfo.io/{ip}/json"
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
    except Exception as e:
        print(f"Erro GeoIP: {e}")
    return {}

def get_reputation(ip, api_key):
    """Consulta reputação no AbuseIPDB (Requer chave)"""
    if api_key == "660400690376c9a376e984ceab851d07d33e7c7f1040c960b062d30e9c1c3b888c79495ed72ede27":
        return None # Retorna vazio se o usuário não configurou a chave
        
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        'Key': api_key,
        'Accept': 'application/json'
    }
    params = {
        'ipAddress': ip,
        'maxAgeInDays': 90
    }
    
    try:
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code == 200:
            return resp.json().get('data', {})
        elif resp.status_code == 401:
            print("❌ Erro AbuseIPDB: Chave de API inválida ou não autorizada.")
    except Exception as e:
        print(f"Erro Reputação: {e}")
    return {}

# --- EXECUÇÃO PRINCIPAL ---
print(f"🔍 Iniciando Análise SOC para: {ALVO}...")
print("-" * 40)

# 1. Coleta de Dados
dados_geo = get_geoip(ALVO)
dados_rep = get_reputation(ALVO, ABUSE_IPDB_KEY)

if not dados_geo:
    print("❌ Falha crítica: Não foi possível obter dados básicos do IP.")
else:
    # 2. Consolidação (Enriquecimento)
    # Mesclamos os dados em um único dicionário mestre
    relatorio_final = {
        "ip": dados_geo.get("ip"),
        "pais": dados_geo.get("country"),
        "org": dados_geo.get("org"),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        # Se não tiver dados de reputação (sem chave), preenche com 'N/A'
        "reputacao_score": dados_rep.get("abuseConfidenceScore", "N/A") if dados_rep else "N/A",
        "total_reports": dados_rep.get("totalReports", "N/A") if dados_rep else "N/A",
        "last_report": dados_rep.get("lastReportedAt", "N/A") if dados_rep else "N/A"
    }

    # 3. Exibição no Terminal
    print("📊 Resultado da Análise:")
    print(f"   IP: {relatorio_final['ip']}")
    print(f"   País: {relatorio_final['pais']}")
    print(f"   Org: {relatorio_final['org']}")
    print(f"   Pontuação de Risco (0-100): {relatorio_final['reputacao_score']}")
    print(f"   Relatórios de Abuso: {relatorio_final['total_reports']}")

    # 4. Exportação para JSON
    with open("relatorio_ip.json", "w", encoding="utf-8") as f:
        json.dump(relatorio_final, f, indent=4, ensure_ascii=False)
    print("\n✅ JSON salvo com sucesso.")

    # 5. Exportação para CSV
    arquivo_csv = "relatorio_ip.csv"
    with open(arquivo_csv, "w", newline="", encoding="utf-8") as csvfile:
        colunas = ["IP", "País", "Organização", "Reputação (Score)", "Relatórios de Abuso", "Data"]
        writer = csv.writer(csvfile)
        writer.writerow(colunas)
        writer.writerow([
            relatorio_final["ip"],
            relatorio_final["pais"],
            relatorio_final["org"],
            relatorio_final["reputacao_score"],
            relatorio_final["total_reports"],
            relatorio_final["timestamp"]
        ])
    print("✅ CSV salvo com sucesso.")
