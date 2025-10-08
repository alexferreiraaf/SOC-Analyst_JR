from collections import Counter
import re

with open("log_exemplo.txt", "r", encoding="utf-8") as f:
    texto = f.read()

ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", texto)
contagem = Counter(ips)

with open("relatorio_ips.txt", "w", encoding="utf-8") as f:
    for ip, qtd in contagem.most_common():
        f.write(f"{ip}: {qtd}\n")

print("Total de IPs únicos:", len(contagem))

