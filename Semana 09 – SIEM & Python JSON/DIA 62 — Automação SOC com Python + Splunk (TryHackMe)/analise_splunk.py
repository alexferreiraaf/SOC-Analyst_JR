hosts = carregar_resultados("data/hosts_mais_ativos.json")
ps = carregar_resultados("data/execucoes_powershell.json")

correlacao = []

for h in hosts:
    for p in ps:
        if h["host"] == p["host"] and p["powershell_execucoes"] > 5:
            correlacao.append({
                "host": h["host"],
                "eventos": h["eventos"],
                "powershell": p["powershell_execucoes"],
                "risco": "ALTO"
            })

with open("alertas_splunk.json", "w") as f:
    json.dump(correlacao, f, indent=4)

