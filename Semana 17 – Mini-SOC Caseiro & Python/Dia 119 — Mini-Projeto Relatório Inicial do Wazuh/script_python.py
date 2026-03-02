#!/usr/bin/env python3

"""
Dia 119 - Mini SOC Wazuh
Filtra alertas relacionados a SSH/autenticação
e gera CSV para análise de possível brute force.
"""

import json
import csv

ALERTS_FILE = "/var/ossec/logs/alerts/alerts.json"
OUTPUT_FILE = "alerts_filtrados.csv"
SEVERITY_MIN = 8

KEYWORDS = ["ssh", "authentication", "login"]

def is_relevant(alert):
    level = alert.get("rule", {}).get("level", 0)
    description = alert.get("rule", {}).get("description", "").lower()

    if level < SEVERITY_MIN:
        return False

    return any(keyword in description for keyword in KEYWORDS)

def main():
    filtered = []

    try:
        with open(ALERTS_FILE, "r") as file:
            for line in file:
                try:
                    alert = json.loads(line)

                    if is_relevant(alert):
                        filtered.append({
                            "timestamp": alert.get("timestamp"),
                            "agent": alert.get("agent", {}).get("name"),
                            "srcip": alert.get("data", {}).get("srcip"),
                            "rule_id": alert.get("rule", {}).get("id"),
                            "description": alert.get("rule", {}).get("description"),
                            "level": alert.get("rule", {}).get("level")
                        })

                except json.JSONDecodeError:
                    continue

    except FileNotFoundError:
        print("Arquivo alerts.json não encontrado.")
        return

    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=filtered[0].keys())
        writer.writeheader()
        writer.writerows(filtered)

    print(f"{OUTPUT_FILE} gerado com {len(filtered)} alertas.")

if __name__ == "__main__":
    main()