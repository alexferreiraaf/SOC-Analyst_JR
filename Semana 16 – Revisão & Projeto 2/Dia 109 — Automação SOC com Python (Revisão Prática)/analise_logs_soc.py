#!/usr/bin/env python3
"""
analise_logs_soc.py

Script de automação SOC para:
- Leitura de logs (ex: auth.log)
- Extração de IP, usuário e timestamp
- Contagem de tentativas por IP
- Aplicação de limiar de detecção
- Geração de evidências (.txt, .csv, .json)

Autor: SOC Study Project
"""

import re
import csv
import json
from collections import Counter
from datetime import datetime

# ==============================
# CONFIGURAÇÕES
# ==============================

LOG_FILE = "network.log"  # Altere para seu arquivo
LIMIAR = 5  # Número mínimo de tentativas para gerar alerta

# Regex simples para extrair dados estilo auth.log
LOG_PATTERN = re.compile(
    r"(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+).*Failed password.*for\s+(?P<user>\S+).*from\s+(?P<ip>\d+\.\d+\.\d+\.\d+)"
)

# ==============================
# FUNÇÕES
# ==============================

def ler_logs(caminho):
    """
    Lê o arquivo de log e retorna lista de linhas.
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return f.readlines()


def extrair_eventos(linhas):
    """
    Extrai timestamp, usuário e IP dos logs.
    """
    eventos = []

    for linha in linhas:
        match = LOG_PATTERN.search(linha)
        if match:
            eventos.append({
                "timestamp": match.group("timestamp"),
                "user": match.group("user"),
                "ip": match.group("ip")
            })

    return eventos


def contar_por_ip(eventos):
    """
    Conta ocorrências por IP.
    """
    ips = [evento["ip"] for evento in eventos]
    return Counter(ips)


def classificar_ips(contagem):
    """
    Classifica IPs com base no limiar.
    """
    resultado = []

    for ip, tentativas in contagem.items():
        if tentativas > LIMIAR:
            classificacao = "SUSPEITO"
        else:
            classificacao = "NORMAL"

        resultado.append({
            "ip": ip,
            "tentativas": tentativas,
            "classificacao": classificacao
        })

    return resultado


def gerar_txt(resultado):
    """
    Gera arquivo TXT com alertas.
    """
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("alertas_suspeitos.txt", "w", encoding="utf-8") as f:
        f.write(f"Relatório de Alertas SOC\n")
        f.write(f"Gerado em: {agora}\n\n")

        for item in resultado:
            if item["classificacao"] == "SUSPEITO":
                f.write(
                    f"[ALERTA] IP {item['ip']} excedeu limite "
                    f"({item['tentativas']} tentativas)\n"
                )


def gerar_csv(resultado):
    """
    Gera arquivo CSV estruturado.
    """
    with open("evidencias_logs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["IP", "Tentativas", "Classificacao"])

        for item in resultado:
            writer.writerow([
                item["ip"],
                item["tentativas"],
                item["classificacao"]
            ])


def gerar_json(resultado):
    """
    Gera arquivo JSON estruturado.
    """
    with open("evidencias_logs.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=4)


# ==============================
# EXECUÇÃO PRINCIPAL
# ==============================

def main():
    print("Iniciando análise SOC...\n")

    linhas = ler_logs(LOG_FILE)
    eventos = extrair_eventos(linhas)
    contagem = contar_por_ip(eventos)
    resultado = classificar_ips(contagem)

    # Exibir no terminal
    print("Resumo de tentativas por IP:\n")
    for item in resultado:
        print(f"{item['ip']} → {item['tentativas']} tentativas ({item['classificacao']})")

    # Gerar evidências
    gerar_txt(resultado)
    gerar_csv(resultado)
    gerar_json(resultado)

    print("\nArquivos gerados:")
    print("- alertas_suspeitos.txt")
    print("- evidencias_logs.csv")
    print("- evidencias_logs.json")
    print("\nAnálise concluída.")


if __name__ == "__main__":
    main()

