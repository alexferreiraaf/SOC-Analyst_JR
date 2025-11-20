import re
from collections import Counter

logfile = "auth_sample.log"
LIMITE_BRUTE_FORCE = 3

# Regex 1: Captura apenas IPs (para contagem rápida)
ip_pattern = re.compile(r"Failed password.*from (\d{1,3}(?:\.\d{1,3}){3})")

# Regex 2 (Exercício 5): Captura Data, Usuário e IP
# Adicionamos (?:invalid user )? para capturar casos de usuários inexistentes também
padrao_detalhado = re.compile(r"(\w{3}\s+\d+\s[\d:]+).*Failed password for (?:invalid user )?(\w+) from (\d{1,3}(?:\.\d{1,3}){3})")

ips_encontrados = []
detalhes_ataques = []

try:
    print(f"--- Analisando {logfile} ---")
    
    with open(logfile, "r") as f:
        for linha in f:
            # 1. Lógica de Contagem de IPs
            match_ip = ip_pattern.search(linha)
            if match_ip:
                ips_encontrados.append(match_ip.group(1))
            
            # 2. Lógica de Extração Detalhada (Exercício 5)
            match_detalhe = padrao_detalhado.search(linha)
            if match_detalhe:
                # group(1)=Data, group(2)=Usuário, group(3)=IP
                dados = (match_detalhe.group(1), match_detalhe.group(2), match_detalhe.group(3))
                detalhes_ataques.append(dados)

    # --- RELATÓRIOS ---
    
    contagem = Counter(ips_encontrados)

    # Tabela Geral
    print(f"\n{'STATUS':<10} | {'QTD':<5} | {'IP DE ORIGEM'}")
    print("-" * 40)
    for ip, total in contagem.most_common():
        status = "[ALERTA]" if total > LIMITE_BRUTE_FORCE else "[NORMAL]"
        print(f"{status:<10} | {total:<5} | {ip}")

    # Lista de Suspeitos
    suspeitos = [ip for ip, total in contagem.items() if total > LIMITE_BRUTE_FORCE]
    print("\n" + "="*30)
    print(f"⚠️  IPs suspeitos (> {LIMITE_BRUTE_FORCE} tentativas):")
    if suspeitos:
        print("\n".join(suspeitos))
    else:
        print("Nenhum suspeito encontrado.")

    # --- EXERCÍCIO 5: Relatório Detalhado ---
    print("\n" + "="*30)
    print("📝 Detalhes das Tentativas (Exercício 5):")
    # Mostramos as últimas 10 para não poluir a tela, mas a lista 'detalhes_ataques' tem tudo
    for data, usuario, ip in detalhes_ataques[-10:]:
        print(f"[{data}] Usuário: {usuario:<10} | IP: {ip}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{logfile}' não foi encontrado.")