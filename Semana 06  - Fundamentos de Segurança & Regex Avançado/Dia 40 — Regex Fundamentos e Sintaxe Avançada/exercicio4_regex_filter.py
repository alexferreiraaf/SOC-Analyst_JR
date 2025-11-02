#!/usr/bin/env python3
# exercicio4_regex_filter.py
# Objetivo: prevenir falsos positivos — ignorar logs sem IP e IPs inválidos (0.0.0.0)

import re

with open("auth_sample.log", "r", encoding="utf-8", errors="ignore") as f:
    logs = f.readlines()

# ✅ Regex aprimorado:
# - Captura apenas IPs válidos (1-255 em cada octeto)
# - Ignora "Source Network Address: -" e IPs "0.0.0.0"
failed_re = re.compile(
    r"Failed\s+login.*Source\s+Network\s+Address:\s+(?P<ip>(?!0\.0\.0\.0)(?:\b(?!-)(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b\.){3}\b(?!-)(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b)"
)

valid_failures = []

for line in logs:
    # Ignorar linhas com endereço "-"
    if "Source Network Address: -" in line:
        continue

    match = failed_re.search(line)
    if match:
        ip = match.group("ip")
        valid_failures.append(ip)

# Mostrar resultados
if valid_failures:
    print("Endereços IP válidos detectados em falhas de login:")
    for ip in valid_failures:
        print("-", ip)
else:
    print("Nenhuma falha de login com IP válido encontrada.")
