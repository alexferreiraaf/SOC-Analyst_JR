#!/usr/bin/env python3
# bruteforce_report.py
# Integra Exercícios 1-4:
# - Captura Data/Hora, Usuário, IP
# - Gera relatorio_bruteforce.csv
# - Imprime TOP5
# - Cria alertas.txt
# - Tenta gerar grafico_tentativas.png (matplotlib) se disponível

import re
import csv
import collections
from collections import Counter
import sys
import os

# ----------------------------
# Configurações
INPUT_FILE = "auth_sample.log"
OUTPUT_CSV = "relatorio_bruteforce.csv"
ALERT_FILE = "alertas.txt"
GRAFICO_PNG = "grafico_tentativas.png"
ALERTA_THRESHOLD = 5   # >5 tentativas gera alerta
GRAFICO_THRESHOLD = 3  # mostra no gráfico IPs com mais de 3 tentativas
# ----------------------------

# Regex que captura dois formatos comuns de timestamp:
# - Syslog: "Oct  8 12:34:56"  (Mon  DD HH:MM:SS)
# - ISO: "2025-10-20 08:15:23"
pattern = re.compile(
    r"^(?P<datetime>(?:[A-Za-z]{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})|(?:\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})).*"
    r"Failed\s+password\s+for\s+(?:invalid\s+user\s+)?(?P<user>\S+)\s+from\s+(?P<ip>(?:\d{1,3}\.){3}\d{1,3})",
    re.IGNORECASE
)

ips = Counter()
rows = []  # lista de tuplas (datetime, user, ip)

# Ler arquivo de logs
if not os.path.exists(INPUT_FILE):
    print(f"Arquivo de entrada não encontrado: {INPUT_FILE}")
    print("Coloque o auth_sample.log (ou outro log) no mesmo diretório ou altere INPUT_FILE no script.")
    sys.exit(1)

with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        m = pattern.search(line)
        if m:
            dt = m.group("datetime")
            user = m.group("user")
            ip = m.group("ip")
            rows.append((dt, user, ip))
            ips[ip] += 1

# Escrever CSV com Data/Hora | Usuário | IP
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data/Hora", "Usuário", "IP"])
    for dt, user, ip in rows:
        writer.writerow([dt, user, ip])

print(f"✅ CSV gerado: {OUTPUT_CSV} (total de eventos parseados: {len(rows)})")

# Escrever alertas.txt
with open(ALERT_FILE, "w", encoding="utf-8") as alerta:
    for ip, count in ips.items():
        if count > ALERTA_THRESHOLD:
            alerta.write(f"ALERTA: {ip} com {count} tentativas\n")

print(f"✅ Alertas (IPs com > {ALERTA_THRESHOLD} tentativas) gravados em: {ALERT_FILE}")

# Imprimir TOP 5 IPs
print("\nTOP 5 IPs SUSPEITOS:")
for ip, count in ips.most_common(5):
    print(f"{ip} — {count} tentativas")

# Tentar gerar gráfico (matplotlib) se disponível
suspeitos_para_grafico = {ip: cnt for ip, cnt in ips.items() if cnt > GRAFICO_THRESHOLD}
if suspeitos_para_grafico:
    try:
        import matplotlib
        # forçar backend não-GUI apropriado para servidores/headless
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        ips_list = list(suspeitos_para_grafico.keys())
        counts = list(suspeitos_para_grafico.values())

        plt.figure(figsize=(8, 4))
        plt.bar(ips_list, counts)
        plt.title("IPs com Tentativas de Login Falhas")
        plt.xlabel("IP")
        plt.ylabel("Tentativas")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(GRAFICO_PNG)
        plt.close()
        print(f"✅ Gráfico salvo: {GRAFICO_PNG}")
    except Exception as e:
        print("⚠️ Não foi possível gerar gráfico com matplotlib:", e)
        print("   Se quiser, instale matplotlib com: python -m pip install matplotlib")
else:
    print(f"🔁 Nenhum IP com mais de {GRAFICO_THRESHOLD} tentativas para gerar gráfico.")

# Mensagem final
print("\nConcluído. Arquivos gerados:")
print(f" - {OUTPUT_CSV}")
print(f" - {ALERT_FILE}")
if os.path.exists(GRAFICO_PNG):
    print(f" - {GRAFICO_PNG}")
