import requests

url = "https://api.ipify.org?format=json"
resposta = requests.get(url)

if resposta.status_code == 200:
    print("Resposta JSON:", resposta.json())
else:
    print("Erro:", resposta.status_code)


