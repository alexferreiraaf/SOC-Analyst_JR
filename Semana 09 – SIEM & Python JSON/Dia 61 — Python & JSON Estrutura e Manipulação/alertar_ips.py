import json
from pprint import pprint

def carregar_json(arquivo):
    with open(arquivo, "r") as f:
        return json.load(f)

def extrair_ips(eventos):
    ips = set()
    for item in eventos:
        ip = (
            item.get("ip") or
            item.get("src_ip") or
            item.get("source_ip")
        )
        if ip:
            ips.add(ip)
    return ips

def correlacionar_ips(arquivos):
    correlacao = {}
    for arquivo in arquivos:
        eventos = carregar_json(arquivo)
        ips = extrair_ips(eventos)

        for ip in ips:
            correlacao.setdefault(ip, []).append(arquivo)
    return correlacao

def alertas_multiplas_fontes(correlacao, minimo=2):
    return {
        ip: fontes
        for ip, fontes in correlacao.items()
        if len(fontes) >= minimo
    }

# === Execução ===

arquivos = ["auth.json", "syslog.json", "firewall.json"]

correlacao = correlacionar_ips(arquivos)
alertas = alertas_multiplas_fontes(correlacao)

print(f"[!] IPs em múltiplas fontes: {len(alertas)}\n")
pprint(alertas)

with open("alertas_multiplas_fontes.json", "w") as f:
    json.dump(alertas, f, indent=4)

