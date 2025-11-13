import re
import hashlib
import requests
import csv
import time
from datetime import datetime

API_KEY = ""
url_vt = "https://www.virustotal.com/api/v3/files/"

# 1️⃣ Ler logs e extrair nomes de arquivos suspeitos
with open("logs.txt", "r", encoding="utf-8") as f:
    logs = f.read()

# Exemplo de linha: "ALERTA: executável suspeito detectado → arquivo.exe"
arquivos = re.findall(r"→\s*(\S+\.exe)", logs)
print(f"Arquivos detectados: {arquivos}")

# 2️⃣ Calcular hash SHA256 de cada arquivo
def gerar_hash(caminho):
    try:
        with open(caminho, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        print(f"[!] Arquivo não encontrado: {caminho}")
        return None

hashes = {arq: gerar_hash(arq) for arq in arquivos if gerar_hash(arq)}

# 3️⃣ Consultar VirusTotal com tratamento de erros e limite
resultados = []

for arquivo, hash_arquivo in hashes.items():
    if not hash_arquivo:
        continue

    print(f"🔍 Consultando VirusTotal para {arquivo}...")

    try:
        resp = requests.get(url_vt + hash_arquivo, headers={"x-apikey": API_KEY})
        
        if resp.status_code == 429:
            print("⚠️ Limite de requisições atingido. Aguardando 60 segundos...")
            time.sleep(60)
            continue
        
        resp.raise_for_status()
        dados = resp.json()

        estatisticas = dados["data"]["attributes"]["last_analysis_stats"]
        maliciosos = estatisticas.get("malicious", 0)
        suspeitos = estatisticas.get("suspicious", 0)

        resultado = (
            "Malicioso" if maliciosos > 0
            else "Suspeito" if suspeitos > 0
            else "Limpo"
        )

        link_relatorio = f"https://www.virustotal.com/gui/file/{hash_arquivo}"
        data_analise = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        resultados.append({
            "Arquivo": arquivo,
            "Hash": hash_arquivo,
            "Resultado": resultado,
            "Maliciosos": maliciosos,
            "Suspeitos": suspeitos,
            "Data Análise": data_analise,
            "Link": link_relatorio
        })

    except requests.exceptions.RequestException as e:
        print(f"Erro de rede ao consultar {arquivo}: {e}")
    except (KeyError, ValueError) as e:
        print(f"Erro ao processar resposta do VirusTotal para {arquivo}: {e}")

    # Evita atingir o limite (máx. 4/min para contas grátis)
    time.sleep(15)

# 4️⃣ Salvar relatório CSV consolidado
with open("relatorio_incidentes.csv", "w", newline="", encoding="utf-8") as csvfile:
    campos = ["Arquivo", "Hash", "Resultado", "Maliciosos", "Suspeitos", "Data Análise", "Link"]
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()
    writer.writerows(resultados)

print("\n✅ Relatório consolidado salvo em 'relatorio_incidentes.csv'")

