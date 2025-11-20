import re, csv, argparse
from collections import Counter
from datetime import datetime

def parse_logs(arquivo):
    # Lê e extrai IPs e usuários de falhas de login
    padrao = re.compile(r"Failed password for (?:invalid user )?(\w+) from ([\d.]+)")
    tentativas = []

    with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
        for linha in f:
            match = padrao.search(linha)
            if match:
                usuario, ip = match.groups()
                tentativas.append((usuario, ip))
    return tentativas


def gerar_relatorio(tentativas):
    contador = Counter(tentativas)
    with open("relatorio.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Usuário", "IP", "Tentativas", "Data"])
        for (usuario, ip), total in contador.items():
            writer.writerow([usuario, ip, total, datetime.now().strftime("%Y-%m-%d %H:%M")])
    print("✅ Relatório gerado: relatorio.csv")


def gerar_alertas(tentativas, limite=5):
    contador_ip = Counter([ip for _, ip in tentativas])
    with open("alertas.txt", "w") as alertas:
        for ip, total in contador_ip.items():
            if total > limite:
                mensagem = f"⚠️ ALERTA: IP {ip} com {total} falhas de login!"
                print(mensagem)
                alertas.write(mensagem + "\n")
    print("✅ Alertas salvos em alertas.txt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analisador de logs SOC")
    parser.add_argument("arquivo", help="Caminho do arquivo de log")
    args = parser.parse_args()

    tentativas = parse_logs(args.arquivo)
    gerar_relatorio(tentativas)
    gerar_alertas(tentativas)


