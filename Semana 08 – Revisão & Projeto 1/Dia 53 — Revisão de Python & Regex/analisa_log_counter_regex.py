import re
from collections import Counter

logfile = "auth_sample.log"
LIMITE_BRUTE_FORCE = 5  # Se falhar mais que isso, é alerta!

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

    # 1. O seu exercício: Usando Counter para contar
    contagem = Counter(ips_encontrados)

    print(f"\n{'STATUS':<10} | {'QTD':<5} | {'IP DE ORIGEM'}")
    print("-" * 40)

    # 2. Iterando e identificando ataques (Lógica SOC)
    # Usamos .most_common() para ordenar do maior para o menor (melhor visualização)
    for ip, total in contagem.most_common():
        if total >= LIMITE_BRUTE_FORCE:
            status = "[ALERTA]" # Possível ataque de Força Bruta
        else:
            status = "[NORMAL]"

        print(f"{status:<10} | {total:<5} | {ip}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{logfile}' não foi encontrado. Verifique se ele está na pasta.")