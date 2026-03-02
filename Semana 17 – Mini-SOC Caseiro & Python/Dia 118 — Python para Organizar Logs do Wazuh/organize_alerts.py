#!/usr/bin/env python3

"""
Dia 118 - Automação Wazuh + Python
Lê o arquivo alerts.json, filtra por severidade
e gera um CSV com IPs e quantidade de alertas.
"""

import json
import csv
from collections import defaultdict

# Caminho do arquivo de alertas (ajuste se necessário)
ALERTS_FILE = "/var/ossec/logs/alerts/alerts.json"

# Definição de severidade mínima
SEVERITY_MIN = 10

def main():
    alerts = []

    # Leitura linha a linha (JSON por linha)
    try:
        with open(ALERTS_FILE, "r") as file:
            for line in file:
                try:
                    alert = json.loads(line)
                    alerts.append(alert)
                except json.JSONDecodeError:
                    # Ignora linhas inválidas
                    continue
    except FileNotFoundError:
        print("Arquivo alerts.json não encontrado.")
        return

    # Filtrar por severidade
    filtered_alerts = []
    for alert in alerts:
        level = alert.get("rule", {}).get("level", 0)
        if level >= SEVERITY_MIN:
            filtered_alerts.append(alert)

    # Agrupar por IP de origem
    ip_counter = defaultdict(int)

    for alert in filtered_alerts:
        src_ip = alert.get("data", {}).get("srcip")
        if src_ip:
            ip_counter[src_ip] += 1

    # Gerar CSV
    output_file = "ips_suspeitos.csv"

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP", "Total_Alertas"])

        for ip, count in sorted(ip_counter.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([ip, count])

    print(f"Arquivo {output_file} gerado com sucesso.")
    print("Resumo:")
    for ip, count in ip_counter.items():
        print(f"{ip} → {count} alertas")

if __name__ == "__main__":
    main()