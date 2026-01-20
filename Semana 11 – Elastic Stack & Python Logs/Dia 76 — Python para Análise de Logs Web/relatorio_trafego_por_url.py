import pandas as pd
import re

# ==============================
# CONFIGURAÇÃO
# ==============================
log_file = "access.log"
csv_output = "trafego_por_url.csv"

# ==============================
# REGEX PARA LOG WEB (Apache / Nginx)
# ==============================
pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ '
    r'\[(?P<date>\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\] '
    r'"(?P<method>\S+) (?P<url>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)

# ==============================
# LEITURA E PARSING
# ==============================
logs = []

with open(log_file, "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            logs.append(match.groupdict())

df = pd.DataFrame(logs)

# ==============================
# CONTAGEM DE ACESSOS POR URL
# ==============================
trafego_por_url = (
    df["url"]
    .value_counts()
    .reset_index()
)

trafego_por_url.columns = ["url", "total_acessos"]

# ==============================
# EXIBIR TOP 10 URLs
# ==============================
print("\n🌐 TOP 10 URLs MAIS ACESSADAS\n")
print(trafego_por_url.head(10))

# ==============================
# SALVAR RELATÓRIO
# ==============================
trafego_por_url.to_csv(csv_output, index=False)
print(f"\n📁 Relatório salvo em: {csv_output}")

