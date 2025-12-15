import json
from pprint import pprint

def carregar_json(arquivo):
    with open(arquivo, "r") as f:
        return json.load(f)

def filtrar_alertas(logs, limite=3):
    alertas = []
    for item in logs:
        falhas = int(item.get("falhas", 0))
        if falhas > limite:
            alertas.append(item)
    return alertas

def salvar_json(dados, arquivo):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)

# === Execução ===

logs = carregar_json("logs.json")
alertas = filtrar_alertas(logs)

print(f"[+] Total de alertas gerados: {len(alertas)}\n")

pprint(alertas)

salvar_json(alertas, "alertas.json")

