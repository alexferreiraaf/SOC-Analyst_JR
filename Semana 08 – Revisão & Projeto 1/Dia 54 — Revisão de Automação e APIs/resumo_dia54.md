📘 Resumo do Dia 54: Automação SOC e Integração de APIs

Data: 20 de Novembro de 2025

Foco: Automação com Python, Requisições HTTP, Manipulação de JSON/CSV e Threat Intelligence.

Objetivo: Criar ferramentas que automatizam a coleta de dados de IPs suspeitos para agilizar a resposta a incidentes.

1. O Papel da Automação no SOC

A automação não substitui o analista, mas remove o trabalho repetitivo ("braçal"). Em um SOC moderno, Python é usado para:

Reduzir o MTTR (Mean Time to Respond): Coleta de dados em segundos, não minutos.

Enriquecimento de Dados: Consultar múltiplas fontes (GeoIP, Reputação, Whois) automaticamente.

Padronização: Garantir que todo incidente seja analisado com o mesmo rigor.

1. Ferramentas e Bibliotecas Essenciais

🐍 Biblioteca requests

O padrão ouro para fazer o Python "conversar" com a internet.

import requests

\# Estrutura básica de uma consulta GET

resposta = requests.get("[https://api.exemplo.com/dados](https://api.exemplo.com/dados)")

\# Verificação de sucesso (HTTP 200 OK)

if resposta.status\_code == 200:

dados = resposta.json() # Converte a resposta para Dicionário Python


📄 Formato JSON

O JSON (JavaScript Object Notation) é a linguagem universal das APIs. O Python o trata como um Dicionário (chave: valor).


📊 Manipulação de CSV

Essencial para gerar relatórios que podem ser abertos no Excel ou importados para um SIEM.

import csv

with open("relatorio.csv", "w", newline="") as f:

writer = csv.writer(f)

writer.writerow(["IP", "País", "Risco"]) # Cabeçalho

writer.writerow(["8.8.8.8", "US", "Baixo"]) # Dados


1. Workflow de um Script de Inteligência de Ameaças

Todo script de automação SOC segue um fluxo lógico de 5 etapas:

Input (Entrada): Ler uma lista de alvos (ex: arquivo suspeitos.txt ou input do usuário).

Enriquecimento (Processamento): Para cada alvo, consultar APIs externas.

GeoIP (Onde está?): ipinfo.io, ip-api.com

Reputação (É malicioso?): AbuseIPDB, VirusTotal

Parsing (Tratamento): Extrair apenas o necessário do JSON (País, ASN, Score de Risco).

Output (Saída): Salvar em arquivo consolidado (.csv, .json).

Ação (Resposta): Exibir alerta no terminal, enviar e-mail ou Webhook (Discord/Slack).

1. Código de Referência: O "Mini-SOC"

Abaixo, o script consolidado que integra leitura de arquivo, consulta a API, lógica de decisão (IF) e geração de CSV.

import requests

import csv

import time

from datetime import datetime

\# Configurações

ARQUIVO\_ALVOS = "suspeitos.txt"

ARQUIVO\_RELATORIO = "relatorio\_ameacas.csv"

API\_KEY = "SUA\_KEY\_ABUSEIPDB" # Opcional para reputação

def consultar\_ip(ip):

"""Consulta dados básicos e reputação"""

dados = {"ip": ip, "pais": "N/A", "org": "N/A", "risco": 0}

\# 1. GeoIP (IPInfo)

try:

resp = requests.get(f"[https://ipinfo.io/](https://ipinfo.io/){ip}/json", timeout=5)

if resp.status\_code == 200:

json\_data = resp.json()

dados["pais"] = json\_data.get("country", "N/A")

dados["org"] = json\_data.get("org", "N/A")

except: pass

\# 2. Reputação (AbuseIPDB - Exemplo Conceitual)

\# (Adicionar lógica de requests aqui se tiver chave)

return dados

\# Fluxo Principal

print("🛡️ Iniciando Análise de Ameaças...")

try:

with open(ARQUIVO\_ALVOS, "r") as f:

ips = [line.strip() for line in f if line.strip()]

resultados = []

print(f"📋 Analisando {len(ips)} endereços IP...\n")

for ip in ips:

info = consultar\_ip(ip)

\# Lógica de Alerta SOC

if info["pais"] not in ["BR", "US"] or "BadActor" in info["org"]:

print(f"⚠️ ALERTA: {ip} ({info['pais']}) - Origem Suspeita!")

else:

print(f"✅ Limpo: {ip}")

info["data\_analise"] = datetime.now().strftime("%Y-%m-%d %H:%M")

resultados.append(info)

time.sleep(1) # Rate Limit (Ética)

\# Salvando CSV

if resultados:

with open(ARQUIVO\_RELATORIO, "w", newline="") as csvfile:

writer = csv.DictWriter(csvfile, fieldnames=resultados[0].keys())

writer.writeheader()

writer.writerows(resultados)

print(f"\n📄 Relatório salvo em: {ARQUIVO\_RELATORIO}")

except FileNotFoundError:

print("Erro: Crie o arquivo 'suspeitos.txt' primeiro.")


1. Conceitos Avançados (Nível Profissional)

Webhooks (Discord/Slack)

Permitem que seu script envie notificações em tempo real para canais de chat.

Payload: É o JSON enviado via POST para a URL do webhook.

Uso: Alerta imediato para IPs com Risk Score > 80.

Agendamento (Cron / Task Scheduler)

Scripts de segurança devem rodar sozinhos.

Linux (Cron): 0 8 \* \* \* python3 script.py (Roda todo dia às 08h).

Windows: Agendador de Tarefas > Criar Tarefa Básica > Iniciar Programa.

Biblioteca rich

Melhora a experiência do usuário (UX) no terminal com cores, tabelas e barras de progresso, facilitando a leitura visual dos alertas.

Conclusão

Dominar APIs e Python permite ao analista de SOC sair da "fila de tickets" e atuar na Engenharia de Detecção, criando ferramentas que trabalham por ele e aumentam a segurança da organização.
