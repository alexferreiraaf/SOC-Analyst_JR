import requests

# URL da API pública para obter o IP
url = "https://api.ipify.org?format=json"

print("🌐 Consultando IP público...")

# Faz a requisição GET
resposta = requests.get(url)

# Verifica se a resposta foi bem-sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    print("\n✅ Requisição bem-sucedida!")
    print(f"🌎 IP Público: {dados['ip']}")
    print(f"⏱️ Tempo de resposta: {resposta.elapsed.total_seconds()} segundos")
    print(f"📦 Content-Type: {resposta.headers.get('Content-Type')}")
else:
    print("\n❌ Erro ao consultar API!")
    print(f"Código HTTP: {resposta.status_code}")

