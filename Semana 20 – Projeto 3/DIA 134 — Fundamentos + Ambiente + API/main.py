import requests
import json

# =====================================================
# CONFIGURAÇÃO
# =====================================================

# Substitua pela sua API Key do VirusTotal
API_KEY = "sua API_KEY"

# IP que será consultado
IP = "8.8.8.8"

# Endpoint da API
URL = f"https://www.virustotal.com/api/v3/ip_addresses/{IP}"

# Cabeçalhos da requisição
headers = {
    "x-apikey": API_KEY
}

# =====================================================
# CONSULTA À API
# =====================================================

print(f"Consultando informações do IP: {IP}...\n")

try:
    response = requests.get(URL, headers=headers)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        dados = response.json()

        print("Consulta realizada com sucesso!\n")

        # Exibe o JSON formatado
        print(json.dumps(dados, indent=4, ensure_ascii=False))

    elif response.status_code == 401:
        print("Erro: API Key inválida ou não informada.")

    elif response.status_code == 429:
        print("Erro: Limite de consultas da API gratuita excedido.")

    else:
        print(f"Erro HTTP {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as erro:
    print("Erro ao conectar com a API do VirusTotal.")
    print(f"Detalhes: {erro}")
