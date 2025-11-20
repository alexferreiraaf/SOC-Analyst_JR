import re
import csv
import argparse
import sys
from collections import Counter
from datetime import datetime

# --- BLOCO DE PREPARAÇÃO (Para funcionar no ambiente de teste) ---
# Cria um arquivo dummy para que o script tenha o que ler
def criar_log_teste():
    conteudo = """
Nov 20 06:25:01 server sshd[1234]: Failed password for root from 192.168.1.105 port 22 ssh2
Nov 20 06:25:05 server sshd[1235]: Failed password for invalid user admin from 192.168.1.105 port 22 ssh2
Nov 20 06:25:10 server sshd[1236]: Failed password for user1 from 10.0.0.5 port 22 ssh2
Nov 20 06:26:00 server sshd[1240]: Failed password for invalid user support from 45.33.22.11 port 5432 ssh2
Nov 20 06:26:02 server sshd[1241]: Failed password for invalid user guest from 45.33.22.11 port 5432 ssh2
Nov 20 06:26:05 server sshd[1242]: Failed password for root from 45.33.22.11 port 5432 ssh2
Nov 20 06:26:10 server sshd[1243]: Failed password for root from 182.10.50.4 port 22 ssh2
Nov 20 06:27:00 server sshd[1250]: Failed password for invalid user ubnt from 203.0.113.50 port 22 ssh2
Nov 20 06:27:02 server sshd[1251]: Failed password for invalid user ubnt from 203.0.113.50 port 22 ssh2
Nov 20 06:27:04 server sshd[1252]: Failed password for root from 203.0.113.50 port 22 ssh2
Nov 20 06:27:06 server sshd[1253]: Failed password for root from 203.0.113.50 port 22 ssh2
Nov 20 06:28:01 server sshd[1260]: Failed password for user2 from 192.168.1.200 port 22 ssh2
    """
    with open("auth_sample.log", "w") as f:
        f.write(conteudo.strip())
    print("📄 Arquivo de teste 'auth_sample.log' criado.")

# --- SEU SCRIPT ORIGINAL (Com pequenas melhorias comentadas) ---

def parse_logs(arquivo):
    # Lê e extrai IPs e usuários de falhas de login
    # Melhoria sugerida: ([\w.-]+) para pegar usuarios como "ana.paula"
    padrao = re.compile(r"Failed password for (?:invalid user )?([\w.-]+) from ([\d.]+)")
    tentativas = []

    try:
        with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
            for linha in f:
                match = padrao.search(linha)
                if match:
                    usuario, ip = match.groups()
                    tentativas.append((usuario, ip))
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{arquivo}' não encontrado.")
        return []
        
    return tentativas


def gerar_relatorio(tentativas):
    if not tentativas:
        print("⚠️ Nenhuma tentativa encontrada para gerar relatório.")
        return

    contador = Counter(tentativas)
    nome_relatorio = "relatorio.csv"
    
    with open(nome_relatorio, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Usuário", "IP", "Tentativas", "Data"])
        for (usuario, ip), total in contador.items():
            writer.writerow([usuario, ip, total, datetime.now().strftime("%Y-%m-%d %H:%M")])
    
    print(f"✅ Relatório gerado: {nome_relatorio}")


def gerar_alertas(tentativas, limite=3): # Reduzi o limite para 3 para disparar no teste
    if not tentativas:
        return

    contador_ip = Counter([ip for _, ip in tentativas])
    alertas_gerados = False
    
    with open("alertas.txt", "w", encoding="utf-8") as alertas:
        for ip, total in contador_ip.items():
            if total >= limite:
                mensagem = f"⚠️ ALERTA: IP {ip} com {total} falhas de login!"
                print(mensagem)
                alertas.write(mensagem + "\n")
                alertas_gerados = True
    
    if alertas_gerados:
        print("✅ Alertas salvos em alertas.txt")
    else:
        print("ℹ️ Nenhum IP ultrapassou o limite de alertas.")


if __name__ == "__main__":
    # 1. Cria o log falso para teste
    criar_log_teste()
    arquivo_alvo = "auth_sample.log"

    # 2. Simulação do argparse para o ambiente de estudo
    # Se estivesse no terminal real, usariamos:
    # parser = argparse.ArgumentParser(description="Analisador de logs SOC")
    # parser.add_argument("arquivo", help="Caminho do arquivo de log")
    # args = parser.parse_args()
    # arquivo_alvo = args.arquivo
    
    print(f"\n--- Iniciando Análise em {arquivo_alvo} ---")
    
    dados_extraidos = parse_logs(arquivo_alvo)
    print(f"📊 Total de linhas processadas com match: {len(dados_extraidos)}")
    
    gerar_relatorio(dados_extraidos)
    print("-" * 30)
    gerar_alertas(dados_extraidos, limite=3)
