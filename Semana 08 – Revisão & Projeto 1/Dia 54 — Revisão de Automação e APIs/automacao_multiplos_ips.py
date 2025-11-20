import requests
import csv
import time
import re
from datetime import datetime

# --- CONFIGURAÇÕES ---
INPUT_FILE = "ips.txt"
OUTPUT_CSV = "relatorio_multiplos_ips.csv"
ABUSE_IPDB_KEY = "SUA_CHAVE_AQUI" # ⚠️ Coloque sua chave aqui se tiver, ou deixe assim

def get_geoip(ip):
    """Consulta IPInfo.io para dados geográficos e ASN."""
    # Verifica se é IP privado para economizar API
    if ip.startswith(("192.168.", "10.", "172.16.", "127.")):
        return {"ip": ip, "country": "LAN", "org": "Rede Interna", "asn": "N/A"}

    url = f"https://ipinfo.io/{ip}/json"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            
            # Tratamento especial para separar ASN da Organização
            # O campo 'org' geralmente vem como "AS15169 Google LLC"
            org_raw = data.get("org", "Desconhecido")
            asn_match = re.search(r"(AS\d+)", org_raw)
            asn = asn_match.group(1) if asn_match else "N/A"
            
            return {
                "ip": data.get("ip"),
                "country": data.get("country", "N/A"),
                "org": org_raw,
                "asn": asn
            }
    except Exception as e:
        print(f"❌ Erro GeoIP ({ip}): {e}")
    
    return {"ip": ip, "country": "Erro", "org": "Erro", "asn": "Erro"}

def get_reputation(ip, api_key):
    """Consulta AbuseIPDB para pontuação de risco."""
    if api_key == "SUA_CHAVE_AQUI" or ip.startswith(("192.168.", "10.")):
        return {"score": "N/A", "reports": "N/A"}

    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {'Key': api_key, 'Accept': 'application/json'}
    params = {'ipAddress': ip, 'maxAgeInDays': 90}

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json().get('data', {})
            return {
                "score": data.get("abuseConfidenceScore", 0),
                "reports": data.get("totalReports", 0)
            }
    except Exception:
        pass
    
    return {"score": "Erro", "reports": "Erro"}

# --- FLUXO PRINCIPAL ---
def main():
    print("🚀 Iniciando Automação de Análise de IPs...")
    
    # 1. Ler IPs do arquivo
    try:
        with open(INPUT_FILE, "r") as f:
            # Lê linhas, remove espaços e ignora linhas vazias
            lista_ips = [linha.strip() for linha in f if linha.strip()]
        print(f"📋 Carregados {len(lista_ips)} IPs para análise.\n")
    except FileNotFoundError:
        print(f"❌ Arquivo '{INPUT_FILE}' não encontrado.")
        return

    resultados = []

    # 2. Processar cada IP
    print(f"{'IP ALVO':<18} | {'PAÍS':<5} | {'STATUS'}")
    print("-" * 40)

    for ip in lista_ips:
        # Consulta GeoIP
        geo = get_geoip(ip)
        
        # Consulta Reputação (se tiver chave)
        rep = get_reputation(ip, ABUSE_IPDB_KEY)
        
        # Consolida dados
        dados_consolidados = {**geo, **rep, "data_consulta": datetime.now().strftime("%Y-%m-%d %H:%M")}
        resultados.append(dados_consolidados)
        
        print(f"{ip:<18} | {geo['country']:<5} | ✅ Processado")
        
        # Pausa ética para não estourar limite da API (Rate Limiting)
        time.sleep(1)

    # 3. Salvar Relatório CSV
    if resultados:
        chaves = ["ip", "country", "asn", "org", "score", "reports", "data_consulta"]
        
        try:
            with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=chaves)
                
                # Mapeamento de nomes bonitos para o cabeçalho
                header_names = {
                    "ip": "Endereço IP", "country": "País", "asn": "ASN", 
                    "org": "Organização", "score": "Risco (0-100)", 
                    "reports": "Denúncias", "data_consulta": "Data"
                }
                
                # Escreve cabeçalho personalizado
                writer.writerow(header_names)
                
                # Escreve linhas
                writer.writerows(resultados)
                
            print(f"\n🎉 Sucesso! Relatório gerado em: {OUTPUT_CSV}")
            
        except Exception as e:
            print(f"\n❌ Erro ao salvar CSV: {e}")
    else:
        print("\n⚠️ Nenhum resultado para salvar.")

if __name__ == "__main__":
    main()
