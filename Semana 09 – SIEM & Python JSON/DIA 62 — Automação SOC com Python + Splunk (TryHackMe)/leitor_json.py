import json

def carregar_resultados(arquivo):
    with open(arquivo) as f:
        return json.load(f)


