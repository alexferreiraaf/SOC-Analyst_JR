import re
from collections import Counter

logfile = "auth_sample.log"
LIMITE_BRUTE_FORCE = 3  # Ajustado para 3 conforme o Exercício 4

# Regex para capturar IPs após "from" em falhas de senha
ip_pattern = re.compile(r"Failed password.*from (\d{1,3}(?:\.\d{1,3}){3})")
ips_encontrados = []

try:
    print(f"--- Analisando {logfile} ---")
    
    with open(logfile, "r") as f:
        for linha in f:
            match = ip_pattern.search(linha)
            if match:
                ips_encontrados.append(match.group(1))

    # Contagem estatística
    contagem = Counter(ips_encontrados)

    # Visualização em Tabela (Exercício Anterior)
    print(f"\n{'STATUS':<10} | {'QTD':<5} | {'IP DE ORIGEM'}")
    print("-" * 40)
    for ip, total in contagem.most_common():
        if total > LIMITE_BRUTE_FORCE:
            status = "[ALERTA]"
        else:
            status = "[NORMAL]"
        print(f"{status:<10} | {total:<5} | {ip}")

    # --- EXERCÍCIO 4: Filtragem com List Comprehension ---
    print("\n" + "="*30)
    
    # Aqui está a linha mágica que filtra e cria a lista numa única passagem
    suspeitos = [ip for ip, total in contagem.items() if total > LIMITE_BRUTE_FORCE]
    
    print(f"⚠️  IPs suspeitos (> {LIMITE_BRUTE_FORCE} tentativas):")
    
    if suspeitos:
        print("\n".join(suspeitos))
    else:
        print("Nenhum suspeito encontrado.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{logfile}' não foi encontrado.")