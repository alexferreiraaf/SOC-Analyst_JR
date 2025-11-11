import hashlib, requests

def gerar_hash_sha256(arquivo):
    with open(arquivo, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def consultar_virustotal(hash, api_key):
    url = f"https://www.virustotal.com/api/v3/files/{hash}"
    headers = {"x-apikey": api_key}
    r = requests.get(url, headers=headers)
    return r.json() if r.status_code == 200 else None

arquivo = input("Arquivo: ")
api_key = input("API Key: ")

hash = gerar_hash_sha256(arquivo)
print(f"\nHash SHA256: {hash}")

dados = consultar_virustotal(hash, api_key)
if dados:
    stats = dados["data"]["attributes"]["last_analysis_stats"]
    print("\n🔍 Resultado da análise:")
    for k, v in stats.items():
        print(f"- {k.capitalize()}: {v}")
else:
    print("⚠️ Hash não encontrado.")

