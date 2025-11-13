import json

dados = resposta.json()

with open("resultado_api.json", "w") as f:
    json.dump(dados, f, indent=4)


