#### 💻 Código Python (`extrair_ips.py`):

import re
from collections import Counter

# Abre o arquivo de logs
with open("sample.txt", "r") as f:
    logs = f.read()

# Regex para IPv4
pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

# Encontra todos os IPs
ips = re.findall(pattern, logs)

# Conta quantas vezes cada IP aparece
contagem = Counter(ips)

# Exibe os resultados
print("Contagem de IPs encontrados:\n")
for ip, qtd in contagem.items():
    print(f"{ip}: {qtd} ocorrência(s)")
