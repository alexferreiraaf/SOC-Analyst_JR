#!/usr/bin/env python3
import re
import csv
import collections
from pathlib import Path

LOG_FILE = "auth_sample.log"
OUTPUT_CSV = "relatorio_bruteforce_com_data.csv"
OUTPUT_COUNTS_CSV = "relatorio_bruteforce_counts.csv"
ALERTA_THRESHOLD = 5  # alerta quando um IP tem mais que esse número de tentativas
TOP_N = 5

# Regex: captura "Mmm dd HH:MM:SS" no começo da linha (syslog style),
# usuário (\w+) e IP IPv4 simples.
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

with log_path.open("r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        m = pattern.search(line)
        if m:
            dt_str, user, ip = m.groups()
            registros.append((dt_str, user, ip))
            ips[ip] += 1

# Salva CSV com Data/Hora, Usuário, IP
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data/Hora", "Usuário", "IP"])
    writer.writerows(registros)

# Salva CSV com contagem por IP (opcional, útil para análises)
with open(OUTPUT_COUNTS_CSV, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP", "Tentativas"])
    for ip, count in ips.most_common():
        writer.writerow([ip, count])

print(f"✅ Relatório detalhado salvo em: {OUTPUT_CSV}")
print(f"✅ Relatório de contagens salvo em: {OUTPUT_COUNTS_CSV}")

# Alerta para IPs acima do threshold
for ip, count in ips.items():
    if count > ALERTA_THRESHOLD:
        print(f"⚠️ ALERTA: IP {ip} com {count} tentativas de login!")

# Exercício 2 — TOP 5 IPs
print("\nTOP 5 IPs SUSPEITOS:")
for ip, count in ips.most_common(TOP_N):
    print(f"{ip} — {count} tentativas")
