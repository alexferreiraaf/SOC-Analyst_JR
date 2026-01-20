import pandas as pd
import re

# ==============================
# CONFIGURAÇÃO
# ==============================
log_file = "access.log"
alert_output = "alerta_bruteforce.csv"

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
# CONVERSÃO DE DATA
# ==============================
df["date"] = pd.to_datetime(
    df["date"],
    format="%d/%b/%Y:%H:%M:%S"
)

df["status"] = df["status"].astype(int)

# ==============================
# FILTRAR FALHAS DE LOGIN
# ==============================
falhas_login = df[
    (df["status"].isin([401, 403])) &
    (df["url"].str.contains("login", case=False, na=False))
]

# ==============================
# AGRUPAR EM JANELAS DE 5 MINUTOS
# ==============================
falhas_login["janela_5min"] = falhas_login["date"].dt.floor("5T")

agrupado = (
    falhas_login
    .groupby(["ip", "janela_5min"])
    .size()
    .reset_index(name="falhas")
)

# ==============================
# DETECTAR BRUTE FORCE
# ==============================
bruteforce = agrupado[agrupado["falhas"] > 10]

# ==============================
# ALERTA SOC
# ==============================
if not bruteforce.empty:
    print("\n🚨 ALERTA SOC — POSSÍVEL BRUTE FORCE DETECTADO 🚨\n")
    print(bruteforce)

    bruteforce.to_csv(alert_output, index=False)
    print(f"\n📁 Alerta salvo em: {alert_output}")
else:
    print("\n✅ Nenhum brute force detectado no período analisado.")

