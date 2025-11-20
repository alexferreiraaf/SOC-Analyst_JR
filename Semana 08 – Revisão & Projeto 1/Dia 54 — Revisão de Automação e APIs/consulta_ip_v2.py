import requests
import json
import csv
from datetime import datetime

# 1. Definição do Alvo
alvo = "8.8.8.8"
url = f"https://ipinfo.io/{alvo}/json"

print(f"🔍 Consultando e salvando dados para: {alvo}...")

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        # Adicionamos o timestamp da consulta ao dicionário de dados
        data_consulta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data['timestamp'] = data_consulta

        # --- TAREFA 1: Salvar em JSON (Dados Brutos) ---
        arquivo_json = "relatorio_ip.json"
        with open(arquivo_json, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✅ JSON salvo em: {arquivo_json}")

        # --- TAREFA 2: Salvar em CSV (Relatório Resumido) ---
        arquivo_csv = "relatorio_ip.csv"
        with open(arquivo_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            
            # Escrevendo o cabeçalho
            writer.writerow(["IP", "País", "Organização", "Data da Consulta"])
            
            # Escrevendo os dados
            # O método .get() evita erros se o campo não existir
            writer.writerow([
                data.get("ip"), 
                data.get("country"), 
                data.get("org"), 
                data_consulta
            ])
        print(f"✅ CSV salvo em: {arquivo_csv}")

    else:
        print(f"❌ Erro na API: {response.status_code}")

except Exception as e:
    print(f"❌ Erro de execução: {e}")