import requests
import csv

# Arquivo de entrada e saída
ARQUIVO_IPS = "ips.txt"
ARQUIVO_SAIDA = "enriquecimento_ips.csv"

# Lê IPs do arquivo
with open(ARQUIVO_IPS, "r") as f:
    ips = [linha.strip() for linha in f.readlines() if linha.strip()]

# Prepara o arquivo CSV de saída
with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ip", "city", "region", "country", "org"])  # cabeçalho

    # Percorre cada IP e faz a consulta
    for ip in ips:
        url = f"https://ipinfo.io/{ip}/json"
        print(f"🔍 Consultando {ip} ...")

        try:
            resposta = requests.get(url, timeout=5)
            if resposta.status_code == 200:
                dados = resposta.json()

                # Extrai apenas os campos desejados
                linha = [
                    dados.get("ip", ip),
                    dados.get("city", "N/A"),
                    dados.get("region", "N/A"),
                    dados.get("country", "N/A"),
                    dados.get("org", "N/A")
                ]
                writer.writerow(linha)
                print(f"✅ Dados coletados para {ip}")

            else:
                print(f"⚠️ Erro {resposta.status_code} ao consultar {ip}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Falha na consulta de {ip}: {e}")

print("\n💾 Resultados salvos em 'enriquecimento_ips.csv'")

