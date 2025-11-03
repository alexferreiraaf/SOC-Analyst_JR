#!/usr/bin/env python3
import re
import csv
import collections
from pathlib import Path
import matplotlib.pyplot as plt

# --------------------------
# Configurações principais
# --------------------------
LOG_FILE = "auth_sample.log"
OUTPUT_CSV = "relatorio_bruteforce_com_data.csv"
OUTPUT_COUNTS_CSV = "relatorio_bruteforce_counts.csv"
ALERTA_THRESHOLD = 5
TOP_N = 5

# --------------------------
# Regex para capturar Data/Hora, Usuário e IP
# --------------------------
pattern = re.compile(
    r"^(\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}).*Failed password for (?:invalid user\s+)?(\w+)\s+from\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)",
    re.IGNORECASE
)

ips = collections.Counter()
registros = []

log_path = Path(LOG_FILE)
if not log_path.exists():
    print(f"Arquivo de log não encontrado: {LOG_FILE}")
    raise SystemExit(1)

# --------------------------
# Leitura e extração dos dados
# --------------------------
with log_path.open("r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        m = pattern.search(line)
        if m:
            dt_str, user, ip = m.groups()
            registros.append((dt_str, user, ip))
            ips[ip] += 1

# --------------------------
# Criação dos relatórios CSV
# --------------------------
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data/Hora", "Usuário", "IP"])
    writer.writerows(registros)

with open(OUTPUT_COUNTS_CSV, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP", "Tentativas"])
    for ip, count in ips.most_common():
        writer.writerow([ip, count])

print(f"✅ Relatório detalhado salvo em: {OUTPUT_CSV}")
print(f"✅ Relatório de contagens salvo em: {OUTPUT_COUNTS_CSV}")

# --------------------------
# Alertas de IPs suspeitos
# --------------------------
for ip, count in ips.items():
    if count > ALERTA_THRESHOLD:
        print(f"⚠️ ALERTA: IP {ip} com {count} tentativas de login!")

# --------------------------
# Exercício 2 — TOP 5 IPs
# --------------------------
print("\nTOP 5 IPs SUSPEITOS:")
for ip, count in ips.most_common(TOP_N):
    print(f"{ip} — {count} tentativas")

# --------------------------
# Exercício 3 — Gráfico (opcional)
# --------------------------
suspeitos = {ip: count for ip, count in ips.items() if count > 3}

if suspeitos:
    plt.bar(suspeitos.keys(), suspeitos.values())
    plt.title("IPs com Tentativas de Login Falhas")
    plt.xlabel("IP")
    plt.ylabel("Tentativas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafico_tentativas.png")
    plt.show()
    print("📊 Gráfico salvo como grafico_tentativas.png")
else:
    print("\nNenhum IP com mais de 3 tentativas para exibir no gráfico.")
