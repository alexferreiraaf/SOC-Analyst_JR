import pandas as pd
import re

# ==============================
# CONFIGURAÇÃO
# ==============================
log_file = "access.log"
csv_output = "falhas_login_por_ip.csv"

# ==============================
# REGEX PARA LOG WEB
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
# CONVERSÃO DE TIPOS
# ==============================
df["status"] = df["status"].astype(int)

df["date"] = pd.to_datetime(
    df["date"],
    format="%d/%b/%Y:%H:%M:%S"
)

# ==============================
# FILTRAR FALHAS DE LOGIN (401 / 403)
# ==============================
falhas_login = df[df["status"].isin([401, 403])]

# ==============================
# CONTAR FALHAS POR IP
# ==============================
falhas_por_ip = (
    falhas_login["ip"]
    .value_counts()
    .reset_index()
)

falhas_por_ip.columns = ["ip", "total_falhas"]

# ==============================
# EXIBIR RESULTADO
# ==============================
print("\n🚨 FALHAS DE LOGIN POR IP (401 / 403)\n")
print(falhas_por_ip)

# ==============================
# SALVAR RELATÓRIO
# ==============================
falhas_por_ip.to_csv(csv_output, index=False)
print(f"\n📁 Relatório salvo em: {csv_output}")

# ==============================
# GERAR GRÁFICO (OPCIONAL)
# ==============================
try:
    falhas_por_ip.head(10).plot(
        kind="bar",
        x="ip",
        y="total_falhas",
        title="Falhas de Login por IP (Top 10)",
        legend=False
    )
    print("\n📊 Gráfico gerado com sucesso.")
except Exception as e:
    print("\n⚠️ Gráfico não gerado (ambiente sem suporte gráfico).")
    print("Motivo:", e)

