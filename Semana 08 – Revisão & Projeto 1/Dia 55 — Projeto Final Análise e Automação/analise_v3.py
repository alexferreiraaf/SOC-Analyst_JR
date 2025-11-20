import re
from collections import Counter

# --- 1. PREPARAÇÃO DO AMBIENTE (Criação do Log de Teste) ---
# Estou criando este arquivo para garantir que o script tenha dados para ler.
# Se você tiver um arquivo real, basta mudar o nome da variável 'ARQUIVO_ALVO'.
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

# --- 2. SCRIPT DE SOLUÇÃO (Nível 1) ---

def extrair_dados(arquivo):
    # Regex do seu script original
    padrao = re.compile(r"Failed password for (?:invalid user )?(\w+) from ([\d.]+)")
    
    lista_usuarios = []
    lista_ips = []

    print(f"📂 Lendo arquivo: {arquivo}...\n")

    try:
        with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
            for linha in f:
                match = padrao.search(linha)
                if match:
                    # O regex retorna grupos: (usuario, ip)
                    usuario, ip = match.groups()
                    lista_usuarios.append(usuario)
                    lista_ips.append(ip)
                    
        return lista_usuarios, lista_ips

    except FileNotFoundError:
        print("❌ Erro: Arquivo não encontrado.")
        return [], []

# --- 3. EXECUÇÃO E RESULTADOS ---

if __name__ == "__main__":
    # Passo A: Executar a extração
    usuarios, ips = extrair_dados("auth_sample.log")

    if ips:
        # Atividade 1: Mostrar usuários únicos encontrados
        # Usamos set() para remover duplicatas e mostrar apenas os nomes
        print(f"👤 Usuários Alvos ({len(set(usuarios))} únicos):")
        print(f"   {set(usuarios)}")
        print("-" * 40)

        # Atividade 2: Mostrar IPs únicos
        print(f"🌐 IPs Atacantes ({len(set(ips))} únicos):")
        print(f"   {set(ips)}")
        print("-" * 40)

        # Atividade 3: Top 5 IPs mais frequentes (Sua Dica Aplicada)
        print("🏆 TOP 5 IPs com mais falhas:")
        
        contagem = Counter(ips)
        top_5 = contagem.most_common(5)

        for i, (ip, qtd) in enumerate(top_5, 1):
            print(f"   {i}. {ip:<15} -> {qtd} tentativas")
            
    else:
        print("Nenhum dado encontrado. Verifique o Regex ou o arquivo de log.")
