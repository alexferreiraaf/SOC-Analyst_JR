import json
from pprint import pprint

def carregar_json(arquivo):
    with open(arquivo, "r") as f:
        return json.load(f)

def salvar_json(dados, arquivo):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)

def calcular_risco(item):
    falhas = int(item.get("falhas", 0))
    return falhas * 2

def enriquecer_com_risco(eventos):
    for item in eventos:
        item["risco"] = calcular_risco(item)
    return eventos

# === Execução ===

logs = carregar_json("auth.json")
logs_enriquecidos = enriquecer_com_risco(logs)

pprint(logs_enriquecidos)

salvar_json(logs_enriquecidos, "logs_com_risco.json")

