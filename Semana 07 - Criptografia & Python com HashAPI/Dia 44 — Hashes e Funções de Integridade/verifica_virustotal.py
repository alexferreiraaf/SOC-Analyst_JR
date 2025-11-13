import requests

# Substitua pela sua chave da API VirusTotal
API_KEY = ""
HASH = input("Digite o hash SHA256 do arquivo: ")

url = f"https://www.virustotal.com/api/v3/files/{HASH}"
headers = {"x-apikey": API_KEY}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    stats = data["data"]["attributes"]["last_analysis_stats"]
    print("\n🔍 Resultado da análise:")
    print(f"- Malicioso: {stats['malicious']}")
    print(f"- Suspeito: {stats['suspicious']}")
    print(f"- Inofensivo: {stats['harmless']}")
    print(f"- Não detectado: {stats['undetected']}")
else:
    print("⚠️ Hash não encontrado ou erro na requisição.")

