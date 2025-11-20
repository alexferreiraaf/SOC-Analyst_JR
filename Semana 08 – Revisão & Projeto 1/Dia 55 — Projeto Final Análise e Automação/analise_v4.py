import re
import csv
from collections import Counter
from datetime import datetime

# --- 1. PREPARAÇÃO (Geração do Log) ---
conteudo_log = """
Nov 20 10:00:01 server sshd[1000]: Failed password for root from 192.168.1.10 port 22 ssh2
Nov 20 10:00:02 server sshd[1001]: Failed password for root from 192.168.1.10 port 22 ssh2
Nov 20 10:00:03 server sshd[1002]: Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
Nov 20 10:05:00 server sshd[1003]: Failed password for user1 from 10.0.0.50 port 22 ssh2
Nov 20 10:05:05 server sshd[1004]: Failed password for user1 from 10.0.0.50 port 22 ssh2
Nov 20 10:10:00 server sshd[1005]: Failed password for invalid user test from 45.33.22.11 port 22 ssh2
Nov 20 10:10:02 server sshd[1006]: Failed password for invalid user guest from 45.33.22.11 port 22 ssh2
Nov 20 10:10:05 server sshd[1007]: Failed password for root from 45.33.22.11 port 22 ssh2
Nov 20 10:10:08 server sshd[1008]: Failed password for root from 45.33.22.11 port 22 ssh2
Nov 20 10:20:00 server sshd[1009]: Failed password for root from 203.0.113.5 port 22 ssh2
Nov 20 10:20:01 server sshd[1010]: Failed password for root from 203.0.113.5 port 22 ssh2
Nov 20 10:20:02 server sshd[1011]: Failed password for root from 203.0.113.5 port 22 ssh2
Nov 20 10:25:00 server sshd[1012]: Failed password for invalid user ubnt from 172.16.0.1 port 22 ssh2
Nov 20 10:30:00 server sshd[1013]: Failed password for root from 8.8.8.8 port 22 ssh2
Nov 20 10:35:00 server sshd[1014]: Failed password for root from 1.1.1.1 port 22 ssh2
Nov 20 10:35:01 server sshd[1015]: Failed password for admin from 1.1.1.1 port 22 ssh2
"""

with open("auth_sample.log", "w") as f:
    f.write(conteudo_log.strip())

# --- 2. SCRIPT SOLUÇÃO (Nível 2) ---

def extrair_tentativas(arquivo):
    padrao = re.compile(r"Failed password for (?:invalid user )?(\w+) from ([\d.]+)")
    tentativas = []
    
    try:
        with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
            for linha in f:
                match = padrao.search(linha)
                if match:
                    usuario, ip = match.groups()
                    # Armazenamos a tupla (usuario, ip) para contar a combinação exata
                    tentativas.append((usuario, ip))
        return tentativas
    except FileNotFoundError:
        return []

def gerar_csv(dados_tentativas):
    if not dados_tentativas:
        print("⚠️ Sem dados para gerar CSV.")
        return

    # 1. Contar ocorrências da combinação (Usuário + IP)
    contador = Counter(dados_tentativas)
    
    # 2. Ordenar decrescente (quem teve mais falhas aparece primeiro)
    # item[1] é a contagem, reverse=True faz do maior para o menor
    dados_ordenados = sorted(contador.items(), key=lambda item: item[1], reverse=True)

    nome_arquivo = "relatorio_01.csv"
    
    # 3. Escrever no CSV
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        # Cabeçalho
        writer.writerow(["Usuário", "IP", "Quantidade de Falhas", "Data/Hora Relatório"])
        
        for (usuario, ip), qtd in dados_ordenados:
            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([usuario, ip, qtd, data_hora])

    print(f"✅ Relatório gerado com sucesso: {nome_arquivo}")
    
    # Exibir prévia no terminal para validação
    print("\n📋 Prévia do Relatório:")
    print(f"{'USUÁRIO':<15} | {'IP':<15} | {'QTD':<5}")
    print("-" * 40)
    for (usuario, ip), qtd in dados_ordenados[:5]: # Top 5 prévia
        print(f"{usuario:<15} | {ip:<15} | {qtd:<5}")

# --- 3. EXECUÇÃO ---
if __name__ == "__main__":
    arquivo_log = "auth_sample.log"
    dados = extrair_tentativas(arquivo_log)
    gerar_csv(dados)
