# 🐍 detector_bruteforce.py

import re
import os
import csv
import json
from datetime import datetime

# ==========================
# CONFIGURAÇÕES
# ==========================

LOG_PATH = "auth.log"
THRESHOLD = 5

# ==========================
# VALIDAÇÃO DO ARQUIVO
# ==========================

if not os.path.exists(LOG_PATH):
    print("[ERRO] Arquivo de log não encontrado.")
    exit()

# ==========================
# LEITURA DO LOG
# ==========================

with open(LOG_PATH, "r") as file:
    lines = file.readlines()

# ==========================
# PROCESSAMENTO
# ==========================

ip_counter = {}

for line in lines:
    if "Failed password" in line:
        match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)
        if match:
            ip = match.group(1)
            ip_counter[ip] = ip_counter.get(ip, 0) + 1

# ==========================
# DETECÇÃO
# ==========================

suspeitos = {}

for ip, count in ip_counter.items():
    if count >= THRESHOLD:
        suspeitos[ip] = count
        print(f"[ALERTA] IP {ip} → {count} tentativas")

# ==========================
# GERAÇÃO DE EVIDÊNCIAS
# ==========================

os.makedirs("../evidencias", exist_ok=True)

data_analise = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 1️⃣ alertas.txt
with open("../evidencias/alertas.txt", "w") as f:
    for ip, count in suspeitos.items():
        f.write(f"IP: {ip}\n")
        f.write(f"Tentativas: {count}\n")
        f.write("Status: Suspeito\n")
        f.write(f"Data da análise: {data_analise}\n")
        f.write("-" * 30 + "\n")

# 2️⃣ ips_suspeitos.csv
with open("../evidencias/ips_suspeitos.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP", "Tentativas", "Data"])
    for ip, count in suspeitos.items():
        writer.writerow([ip, count, data_analise])

# 3️⃣ resumo.json
resumo = {
    "data_analise": data_analise,
    "total_ips_analisados": len(ip_counter),
    "total_ips_suspeitos": len(suspeitos),
    "threshold": THRESHOLD
}

with open("../evidencias/resumo.json", "w") as jsonfile:
    json.dump(resumo, jsonfile, indent=4)

print("\n[INFO] Análise concluída.")

