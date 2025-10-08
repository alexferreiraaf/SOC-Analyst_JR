import re
from collections import Counter

def contar_ips_emails(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Expressões regulares
    padrao_ip = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    padrao_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    ips = re.findall(padrao_ip, conteudo)
    emails = re.findall(padrao_email, conteudo)

    contagem_ips = Counter(ips)
    contagem_emails = Counter(emails)

    print("=== Contagem de IPs ===")
    for ip, qtd in contagem_ips.most_common():
        print(f"{ip}: {qtd}")

    print("\n=== Contagem de E-mails ===")
    for email, qtd in contagem_emails.most_common():
        print(f"{email}: {qtd}")

if __name__ == "__main__":
    contar_ips_emails("log_misto_100.txt")
