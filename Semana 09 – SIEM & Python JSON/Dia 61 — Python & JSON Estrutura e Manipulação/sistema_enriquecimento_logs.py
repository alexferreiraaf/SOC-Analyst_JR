import json
import requests
from collections import Counter

# Função para buscar dados de geolocalização
def obter_dados_ip(ip):
    token = 'token_ipinfo.ip'  # Substitua com seu token
    url = f'http://ipinfo.io/{ip}/json?token={token}'
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        pais, cidade, org = dados.get('country', 'N/A'), dados.get('city', 'N/A'), dados.get('org', 'N/A')
        return pais, cidade, org
    except requests.exceptions.RequestException:
        return 'Desconhecido', 'Desconhecido', 'Desconhecido'

# Função de enriquecimento dos logs
def enriquecer_logs(eventos):
    for item in eventos:
        ip = item.get("ip") or item.get("src_ip")
        if ip:
            pais, cidade, org = obter_dados_ip(ip)
            item["pais"] = pais
            item["cidade"] = cidade
            item["org"] = org
    return eventos

# Função para gerar o relatório
def gerar_relatorio(eventos):
    paises = [item["pais"] for item in eventos]
    orgs = [item["org"] for item in eventos]
    ips = [item.get("ip") or item.get("src_ip") for item in eventos]

    top_paises = Counter(paises).most_common(5)
    top_orgs = Counter(orgs).most_common(5)
    top_ips = Counter(ips).most_common(5)

    relatorio = {
        "Top 5 Países": top_paises,
        "Top 5 Organizações": top_orgs,
        "Top 5 IPs mais ativos": top_ips
    }

    return relatorio

# === Execução ===

# Ler logs (suponha que você tenha "logs.json")
with open("logs.json", "r") as f:
    logs = json.load(f)

# Enriquecer logs com informações geográficas
logs_enriquecidos = enriquecer_logs(logs)

# Salvar logs enriquecidos
with open("logs_enriquecidos.json", "w") as f:
    json.dump(logs_enriquecidos, f, indent=4)

# Gerar e exibir relatório
relatorio = gerar_relatorio(logs_enriquecidos)
print(json.dumps(relatorio, indent=4))

