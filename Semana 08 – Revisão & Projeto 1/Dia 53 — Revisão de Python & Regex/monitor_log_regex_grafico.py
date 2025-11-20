import re
import csv
from collections import Counter

# Tenta importar matplotlib para o desafio avançado
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

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

        # --- DESAFIO AVANÇADO: GRÁFICO MATPLOTLIB ---
        if MATPLOTLIB_AVAILABLE:
            print("\n📊 Gerando gráfico de tentativas...")
            
            # Configuração do Gráfico
            plt.figure(figsize=(10, 6)) # Tamanho da janela
            
            # Separando dados para o gráfico (Top 10 para não poluir se houver muitos)
            dados_grafico = contagem.most_common(10)
            ips_plot = [ip for ip, qtd in dados_grafico]
            qtds_plot = [qtd for ip, qtd in dados_grafico]
            
            # Plotando
            plt.bar(ips_plot, qtds_plot, color='salmon', edgecolor='black')
            
            # Estilização
            plt.xticks(rotation=45, ha='right') # Rotação dos IPs para leitura
            plt.title("Top IPs com Falha de Login (Possível Brute Force)")
            plt.xlabel("Endereço IP de Origem")
            plt.ylabel("Quantidade de Tentativas")
            plt.grid(axis='y', linestyle='--', alpha=0.7) # Linhas de grade suaves
            plt.tight_layout() # Ajusta margens automaticamente
            
            print("A janela do gráfico foi aberta.")
            plt.show()
        else:
            print("\n⚠️  Matplotlib não está instalado.")
            print("Para ver o gráfico, instale usando: pip install matplotlib")

except FileNotFoundError:
    print(f"❌ Erro: O arquivo '{LOG}' não foi encontrado.")