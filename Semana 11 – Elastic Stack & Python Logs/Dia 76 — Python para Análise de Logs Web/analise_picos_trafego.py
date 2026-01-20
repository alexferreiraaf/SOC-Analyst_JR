import pandas as pd
import re

# ==============================
# CONFIGURAÇÃO
# ==============================
log_file = "access.log"
output_file = "relatorio_top_5_picos_trafego.csv"

# ==============================
# REGEX PARA LOG APACHE/NGINX
# ==============================
pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ '
    r'\[(?P<date>\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\] '
    r'"(?P<method>\S+) (?P<url>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)

# ==============================
# LEITURA E PARSING DOS LOGS
# ==============================
logs = []

with open(log_file, "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            logs.append(match.groupdict())

# Criar DataFrame
df = pd.DataFrame(logs)

# ==============================
# CONVERSÃO DE DATA
# ==============================
df["date"] = pd.to_datetime(
    df["date"],
    format="%d/%b/%Y:%H:%M:%S"
)

# ==============================
# AGRUPAR REQUISIÇÕES POR HORA
# ==============================
df["hour"] = df["date"].dt.floor("H")

requests_per_hour = (
    df.groupby("hour")
    .size()
    .reset_index(name="total_requests")
)

# ==============================
# IDENTIFICAR TOP 5 PICOS
# ==============================
top_5_picos = (
    requests_per_hour
    .sort_values(by="total_requests", ascending=False)
    .head(5)
)

# ==============================
# EXIBIR RESULTADO
# ==============================
print("\n📊 TOP 5 PICOS DE TRÁFEGO (REQUISIÇÕES POR HORA)\n")
print(top_5_picos)

# ==============================
# GERAR RELATÓRIO
# ==============================
top_5_picos.to_csv(output_file, index=False)

print(f"\n📁 Relatório gerado com sucesso: {output_file}")

