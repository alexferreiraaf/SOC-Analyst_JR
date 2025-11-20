import re
import csv
from collections import Counter

LOG = "auth_sample.log"
OUT = "relatorio_regex.csv"

try:
    print(f"Lendo arquivo: {LOG}...")
    with open(LOG, "r") as f:
        conteudo = f.read()

    # Captura Data (Grupo 1), Usuário (Grupo 2) e IP (Grupo 3)
    # Regex ajustado para ignorar "invalid user" e pegar o nome correto
    padrao = re.compile(r"(\w{3}\s+\d+\s[\d:]+).*Failed password for (?:invalid user )?(\w+) from (\d{1,3}(?:\.\d{1,3}){3})")
    
    eventos = padrao.findall(conteudo)

    if not eventos:
        print("Nenhum evento encontrado. Verifique se o log tem dados ou se o regex está correto.")
    else:
        # Contagem por IP (List Comprehension)
        ips = [ip for _, _, ip in eventos]
        contagem = Counter(ips)

        # Gera relatório CSV
        with open(OUT, "w", newline="", encoding='utf-8') as csvfile:
            campos = ["Data/Hora", "Usuário", "IP"]
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()
            
            for data, usuario, ip in eventos:
                writer.writerow({"Data/Hora": data, "Usuário": usuario, "IP": ip})

        # Mostra resumo no terminal
        print(f"\n✅ Relatório gerado em: {OUT}")
        print("-" * 30)
        print("🚨 Top IPs suspeitos:")
        for ip, total in contagem.most_common(5):
            print(f"{ip} — {total} tentativas")

except FileNotFoundError:
    print(f"❌ Erro: O arquivo '{LOG}' não foi encontrado.")