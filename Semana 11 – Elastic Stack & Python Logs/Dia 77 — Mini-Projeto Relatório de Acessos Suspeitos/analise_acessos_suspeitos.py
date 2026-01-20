import pandas as pd
import re

# =========================
# Configuração
# =========================
LOG_FILE = "access.log"

pattern = r'(?P<ip>\S+) - - \[(?P<date>\d+/\w+/\d+:\d+:\d+:\d+) .*?\] "(?P<method>\S+) (?P<url>\S+) .*?" (?P<status>\d+)'

logs = []

# =========================
# Leitura e Parsing
# =========================
with open(LOG_FILE) as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            logs.append(match.groupdict())

df = pd.DataFrame(logs)

# Conversões
df["status"] = df["status"].astype(int)
df["date"] = pd.to_datetime(df["date"], format="%d/%b/%Y:%H:%M:%S")

# =========================
# REGRA 1 — Muitas requisições em 1 hora
# =========================
df["hour"] = df["date"].dt.floor("H")
req_por_ip_hora = df.groupby(["ip", "hour"]).size()
suspeitos_requisicoes = req_por_ip_hora[req_por_ip_hora > 100]

# =========================
# REGRA 2 — Falhas de login
# =========================
falhas = df[df["status"].isin([401, 403])]
falhas_por_ip = falhas["ip"].value_counts()
suspeitos_falhas = falhas_por_ip[falhas_por_ip > 10]

# =========================
# REGRA 3 — Endpoints sensíveis
# =========================
endpoints = ["/login", "/admin", "/wp-admin"]
suspeitos_endpoints = df[df["url"].str.contains("|".join(endpoints))]["ip"].unique()

# =========================
# Consolidação
# =========================
ips_suspeitos = (
    set(suspeitos_requisicoes.index.get_level_values(0))
    | set(suspeitos_falhas.index)
    | set(suspeitos_endpoints)
)

relatorio = df[df["ip"].isin(ips_suspeitos)]
relatorio.to_csv("relatorio_ips_suspeitos.csv", index=False)

# =========================
# Relatório SOC
# =========================
with open("resumo_incidente.txt", "w") as f:
    f.write("Relatório de Acessos Suspeitos\n\n")
    f.write(f"Total de IPs suspeitos: {len(ips_suspeitos)}\n")
    f.write("IPs identificados:\n")
    for ip in ips_suspeitos:
        f.write(f"- {ip}\n")
    f.write("\nAções recomendadas:\n")
    f.write("- Monitorar tráfego\n")
    f.write("- Aplicar rate limit\n")
    f.write("- Avaliar bloqueio temporário\n")

print("✅ Análise concluída com sucesso")
print("📄 Arquivos gerados:")
print("- relatorio_ips_suspeitos.csv")
print("- resumo_incidente.txt")

