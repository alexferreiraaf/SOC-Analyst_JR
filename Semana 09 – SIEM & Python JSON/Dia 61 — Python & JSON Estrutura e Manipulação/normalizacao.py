import json
from pprint import pprint

MAPA_NORMALIZACAO = {
    "IP-SOURCE": "src",
    "source_ip": "src",
    "src_ip": "src"
}

def normalizar_evento(evento):
    evento_normalizado = {}
    for campo, valor in evento.items():
        campo_padrao = MAPA_NORMALIZACAO.get(campo, campo)
        evento_normalizado[campo_padrao] = valor
    return evento_normalizado

def normalizar_eventos(eventos):
    return [normalizar_evento(evento) for evento in eventos]

# === Exemplo de uso ===

eventos = [
    {"IP-SOURCE": "10.0.0.5", "action": "blocked"},
    {"source_ip": "8.8.8.8", "action": "allowed"}
]

eventos_normalizados = normalizar_eventos(eventos)

pprint(eventos_normalizados)

