import re
import csv
from collections import Counter
from datetime import datetime
# Importação da biblioteca rich para visualização profissional
try:
    from rich.console import Console
    from rich.table import Table
    console = Console()
except ImportError:
    # Fallback caso rich não esteja instalado
    print("⚠️ Biblioteca 'rich' não encontrada. Instale com 'pip install rich'.")
    class Console:
        def print(self, text, style=None): print(text)
    console = Console()

# --- 1. PREPARAÇÃO (Geração de Log com Ataque Volumoso) ---
# Adicionei mais linhas para o IP 10.0.0.200 para garantir que o alerta dispare (>5)
conteudo_log = """
Nov 20 10:00:01 server sshd[1000]: Failed password for root from 192.168.1.10 port 22 ssh2
Nov 20 10:00:02 server sshd[1001]: Failed password for root from 192.168.1.10 port 22 ssh2
Nov 20 10:00:03 server sshd[1002]: Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
Nov 20 10:05:00 server sshd[1003]: Failed password for user1 from 10.0.0.50 port 22 ssh2
Nov 20 10:05:05 server sshd[1004]: Failed password for user1 from 10.0.0.50 port 22 ssh2
Nov 20 11:00:00 server sshd[2000]: Failed password for root from 10.0.0.200 port 22 ssh2
Nov 20 11:00:01 server sshd[2001]: Failed password for root from 10.0.0.200 port 22 ssh2
Nov 20 11:00:02 server sshd[2002]: Failed password for root from 10.0.0.200 port 22 ssh2
Nov 20 11:00:03 server sshd[2003]: Failed password for admin from 10.0.0.200 port 22 ssh2
Nov 20 11:00:04 server sshd[2004]: Failed password for admin from 10.0.0.200 port 22 ssh2
Nov 20 11:00:05 server sshd[2005]: Failed password for service from 10.0.0.200 port 22 ssh2
Nov 20 11:00:06 server sshd[2006]: Failed password for service from 10.0.0.200 port 22 ssh2
"""

with open("auth_sample.log", "w") as f:
    f.write(conteudo_log.strip())

# --- 2. SCRIPT SOLUÇÃO (Nível 3) ---

def extrair_dados(arquivo):
    padrao = re.compile(r"Failed password for (?:invalid user )?(\w+) from ([\d.]+)")
    tentativas = []
    
    try:
        with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
            for linha in f:
                match = padrao.search(linha)
                if match:
                    usuario, ip = match.groups()
                    tentativas.append((usuario, ip))
        return tentativas
    except FileNotFoundError:
        console.print(f"[bold red]Erro:[/bold red] Arquivo {arquivo} não encontrado.")
        return []

def gerar_alertas_e_relatorio(dados):
    if not dados:
        return

    # Contagem por IP (para o alerta de bloqueio)
    ips = [ip for _, ip in dados]
    contador_ip = Counter(ips)

    limite_alerta = 5
    arquivo_alertas = "alertas_01.txt"
    alertas_detectados = False

    console.print(f"\n🔍 [bold cyan]Iniciando Análise de Segurança...[/bold cyan]")

    with open(arquivo_alertas, "w", encoding="utf-8") as f_alertas:
        f_alertas.write(f"RELATORIO DE ALERTAS - {datetime.now()}\n")
        f_alertas.write("="*40 + "\n")

        # Tabela Rich para visualização bonita no terminal
        tabela = Table(title="Estatísticas de Ataque")
        tabela.add_column("IP Origem", style="cyan")
        tabela.add_column("Tentativas", style="magenta")
        tabela.add_column("Status", justify="right")

        for ip, qtd in contador_ip.most_common():
            status = "[green]Monitorando[/green]"
            
            # Lógica do Alerta (Nível 3)
            if qtd > limite_alerta:
                status = "[bold red]⛔ CRÍTICO[/bold red]"
                
                # 1. Exibe no terminal com destaque
                console.print(f"[bold red]⚠️  ALERTA DE SEGURANÇA:[/bold red] IP {ip} excedeu {qtd} tentativas!")
                
                # 2. Salva no arquivo txt
                mensagem_txt = f"[CRITICO] IP {ip} realizou {qtd} tentativas de falha de login.\n"
                f_alertas.write(mensagem_txt)
                alertas_detectados = True
            
            tabela.add_row(ip, str(qtd), status)

        console.print("\n")
        console.print(tabela)

    if alertas_detectados:
        console.print(f"\n[bold yellow]📄 Arquivo '{arquivo_alertas}' gerado com os incidentes críticos.[/bold yellow]")
    else:
        console.print("\n[green]✅ Nenhum IP ultrapassou o limite de bloqueio.[/green]")

# --- 3. EXECUÇÃO ---
if __name__ == "__main__":
    dados = extrair_dados("auth_sample.log")
    gerar_alertas_e_relatorio(dados)
