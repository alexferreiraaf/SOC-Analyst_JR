import re
from collections import Counter

logfile = "auth_sample.log"
ip_pattern = re.compile(r"Failed password.*from (\d{1,3}(?:\.\d{1,3}){3})")

ips_encontrados = []

try:
    with open(logfile, "r") as f:
        # Itera linha por linha (Não carrega tudo na RAM)
        for linha in f:
            match = ip_pattern.search(linha)
            if match:
                # Adiciona o IP capturado à lista
                ips_encontrados.append(match.group(1))

    # Conta a frequência de cada IP automaticamente
    contagem = Counter(ips_encontrados)

    print(f"{'QTD':<5} | {'IP DE ORIGEM'}")
    print("-" * 25)
    
    # Mostra apenas os Top 10 mais barulhentos
    for ip, qtd in contagem.most_common(10):
        print(f"{qtd:<5} | {ip}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{logfile}' não foi encontrado.")