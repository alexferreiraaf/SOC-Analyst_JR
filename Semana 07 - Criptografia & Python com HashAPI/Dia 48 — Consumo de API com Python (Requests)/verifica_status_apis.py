import urllib.request
import time
import csv

# Lista de APIs para testar
apis = {
    "IPify": "https://api.ipify.org?format=json",
    "GitHub": "https://api.github.com",
    "IPinfo": "https://ipinfo.io/json"
}

# Arquivo de saída
arquivo_csv = "status_apis.csv"

# Cabeçalho do CSV
with open(arquivo_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["API", "Status", "Tempo de Resposta (s)", "Tamanho da Resposta (bytes)"])

# Teste de cada API
for nome, url in apis.items():
    inicio = time.time()
    try:
        with urllib.request.urlopen(url, timeout=10) as resposta:
            conteudo = resposta.read()
            tempo = round(time.time() - inicio, 3)
            tamanho = len(conteudo)
            status = "OK"
    except Exception as erro:
        tempo = round(time.time() - inicio, 3)
        tamanho = 0
        status = f"ERRO: {erro.__class__.__name__}"

    # Salvar resultado no CSV
    with open(arquivo_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nome, status, tempo, tamanho])

print("✅ Teste concluído! Resultados salvos em status_apis.csv")

