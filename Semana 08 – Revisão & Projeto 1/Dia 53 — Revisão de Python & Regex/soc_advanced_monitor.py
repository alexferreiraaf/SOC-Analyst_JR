import re
import time
import json
from collections import Counter
from datetime import datetime

# --- CONFIGURAÇÃO ---
LOG_FILE = "auth_sample.log"
REPORT_FILE = f"incident_report_{datetime.now().strftime('%Y-%m-%d')}.md"
LIMITE_ALERTA = 5
API_URL = "http://ip-api.com/json/"

# Tenta importar bibliotecas externas (que exigem pip install)
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

# --- FUNÇÕES AUXILIARES ---

def get_geolocation(ip):
    """Consulta a API pública para descobrir o país do IP."""
    if not REQUESTS_AVAILABLE:
        return "N/A (Instale 'requests')"
    
    # IPs privados/locais não têm geolocalização
    if ip.startswith(("192.168.", "10.", "172.16.", "127.")):
        return "Local Network (LAN)"

    try:
        # Sleep para respeitar rate-limit da API gratuita (45 req/min)
        time.sleep(0.6) 
        response = requests.get(f"{API_URL}{ip}", timeout=3)
        dados = response.json()
        if dados['status'] == 'success':
            return f"{dados['country']} ({dados['countryCode']})"
        return "Desconhecido"
    except Exception:
        return "Erro API"

def gerar_grafico(contagem):
    """Gera gráfico de barras com Matplotlib."""
    if not MATPLOTLIB_AVAILABLE:
        print("⚠️  Matplotlib não instalado. Gráfico pulado.")
        return

    print("📊 Gerando gráfico de visualização...")
    plt.figure(figsize=(10, 6))
    
    # Pegamos os Top 10 para o gráfico não ficar ilegível
    dados = contagem.most_common(10)
    ips = [d[0] for d in dados]
    qtds = [d[1] for d in dados]

    plt.bar(ips, qtds, color='#e74c3c', edgecolor='black')
    plt.xticks(rotation=45, ha='right')
    plt.title(f"Top IPs Atacantes - {datetime.now().strftime('%d/%m/%Y')}")
    plt.xlabel("Endereço IP")
    plt.ylabel("Tentativas de Falha")
    plt.tight_layout()
    plt.show()

def gerar_relatorio_md(suspeitos_detalhados):
    """Cria um arquivo Markdown com o dossiê do incidente."""
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(f"# 🛡️ Relatório de Incidente de Segurança\n")
        f.write(f"**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
        f.write("## 🚨 Resumo de Ameaças (Brute Force)\n")
        f.write(f"Critério de Alerta: > {LIMITE_ALERTA} tentativas.\n\n")
        f.write("| IP de Origem | País | Tentativas | Status |\n")
        f.write("|---|---|---|---|\n")
        
        for ip, dados in suspeitos_detalhados.items():
            f.write(f"| **{ip}** | {dados['pais']} | {dados['qtd']} | 🔴 CRÍTICO |\n")
    
    print(f"✅ Relatório de Incidente salvo em: {REPORT_FILE}")

# --- CORE DO PROGRAMA ---

def analise_estatica():
    """Lê o arquivo existente e gera estatísticas passadas."""
    print(f"--- 🔍 Iniciando Análise Estática de {LOG_FILE} ---")
    
    try:
        with open(LOG_FILE, "r") as f:
            conteudo = f.read()
    except FileNotFoundError:
        print(f"❌ Arquivo {LOG_FILE} não encontrado. Crie-o primeiro.")
        return

    # Regex para capturar IPs em falhas
    padrao = re.compile(r"Failed password.*from (\d{1,3}(?:\.\d{1,3}){3})")
    ips = padrao.findall(conteudo)
    contagem = Counter(ips)

    # Identifica suspeitos
    suspeitos = {ip: qtd for ip, qtd in contagem.items() if qtd > LIMITE_ALERTA}
    
    if suspeitos:
        print(f"⚠️  Detectados {len(suspeitos)} IPs críticos (> {LIMITE_ALERTA} falhas).")
        print("🌍 Enriquecendo dados com Geolocalização (pode demorar um pouco)...")
        
        suspeitos_detalhados = {}
        for ip, qtd in suspeitos.items():
            pais = get_geolocation(ip)
            suspeitos_detalhados[ip] = {'qtd': qtd, 'pais': pais}
            print(f"   -> {ip}: {qtd} tentativas | Origem: {pais}")

        # Gera artefatos
        gerar_relatorio_md(suspeitos_detalhados)
        gerar_grafico(contagem)
    else:
        print("✅ Nenhum IP ultrapassou o limite crítico na análise estática.")

def monitoramento_tempo_real():
    """Monitora o arquivo como o comando 'tail -f'."""
    print(f"\n--- 📡 Iniciando Monitoramento em Tempo Real (Watchdog) ---")
    print(f"Observando {LOG_FILE} por novos ataques... (Pressione Ctrl+C para sair)")

    padrao = re.compile(r"Failed password.*from (\d{1,3}(?:\.\d{1,3}){3})")
    
    # Controle de sessão para não alertar o mesmo IP a cada milissegundo
    sessao_ataques = Counter()

    try:
        with open(LOG_FILE, "r") as f:
            # Vai para o final do arquivo
            f.seek(0, 2)
            
            while True:
                linha = f.readline()
                if not linha:
                    time.sleep(0.5) # Espera novos dados
                    continue
                
                # Processa nova linha
                match = padrao.search(linha)
                if match:
                    ip = match.group(1)
                    sessao_ataques[ip] += 1
                    
                    # Alerta Imediato no Terminal
                    hora = datetime.now().strftime("%H:%M:%S")
                    print(f"[{hora}] 🛡️ Tentativa bloqueada: {ip} (Total na sessão: {sessao_ataques[ip]})")
                    
                    if sessao_ataques[ip] == LIMITE_ALERTA + 1:
                         pais = get_geolocation(ip)
                         print(f"\n🚨 ALERTA MÁXIMO: {ip} ultrapassou limite! Origem: {pais}\n")

    except KeyboardInterrupt:
        print("\n🛑 Monitoramento encerrado pelo usuário.")
    except FileNotFoundError:
        print("Arquivo de log não encontrado para monitoramento.")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    # 1. Análise do Passado
    analise_estatica()
    
    # 2. Monitoramento do Futuro
    monitoramento_tempo_real()