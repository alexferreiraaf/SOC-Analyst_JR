import re
import csv
import os
import sys
import argparse
from collections import Counter
from datetime import datetime

# Tenta importar rich para visualização, cria fallback se não existir
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    console = Console()
except ImportError:
    class Console:
        def print(self, text, style=None): print(text) # Fallback simples
        def rule(self, title): print(f"--- {title} ---")
    console = Console()

# --- MÓDULO DE SIMULAÇÃO (MOCKS) ---
# Necessário para o script rodar sem dependências externas de terceiros (python-evtx)
class MockEvtx:
    """Simula a biblioteca python-evtx para fins educacionais/teste"""
    def __init__(self, filename): self.filename = filename
    def records(self):
        # Gera dados mistos para estatística
        dados = [
            (4625, "admin", "192.168.1.15", "2025-11-20 10:00"),
            (4625, "admin", "192.168.1.15", "2025-11-20 10:01"), # Admin atacado
            (4625, "admin", "192.168.1.15", "2025-11-20 10:02"),
            (4625, "root", "10.0.0.5", "2025-11-20 10:05"),
            (4625, "guest", "45.33.22.11", "2025-11-20 11:00"),
            (4625, "guest", "45.33.22.11", "2025-11-20 11:05"),
            (4625, "support", "192.168.1.200", "2025-11-20 12:00")
        ] * 15  # Multiplica para gerar volume (Total ~100 falhas)
        
        for eid, user, ip, ts in dados:
            xml_str = f"""
            <Event><System><EventID>{eid}</EventID></System>
            <EventData>
                <Data Name='TargetUserName'>{user}</Data>
                <Data Name='IpAddress'>{ip}</Data>
            </EventData></Event>
            """
            yield type('obj', (object,), {'xml': lambda: xml_str})

def gerar_arquivos_teste():
    """Cria arquivos dummy se não existirem para testar o script"""
    # 1. Arquivo Linux
    if not os.path.exists("teste.log"):
        log_content = ""
        # Gera volume de dados para o Linux também
        for i in range(50):
            log_content += f"Nov 20 10:{i:02d}:01 srv sshd: Failed password for invalid user admin from 192.168.1.100 port 22\n"
        for i in range(20):
            log_content += f"Nov 20 11:{i:02d}:01 srv sshd: Failed password for root from 10.10.10.5 port 22\n"
        
        with open("teste.log", "w") as f: f.write(log_content)
        console.print("[dim]ℹ️ Arquivo 'teste.log' gerado para teste.[/dim]")

    # 2. Arquivo Windows (vazio, pois usamos Mock na leitura)
    if not os.path.exists("teste.evtx"):
        with open("teste.evtx", "w") as f: f.write("MOCK BINARY CONTENT")
        console.print("[dim]ℹ️ Arquivo 'teste.evtx' gerado para teste.[/dim]")

# --- NÚCLEO DO ANALISADOR ---

class AnalisadorLogs:
    def __init__(self):
        self.resultados = [] # Lista de tuplas (usuario, ip)

    def processar_arquivo(self, caminho_arquivo):
        if not os.path.exists(caminho_arquivo):
            console.print(f"[bold red]❌ Erro:[/bold red] Arquivo '{caminho_arquivo}' não encontrado.")
            return False

        extensao = os.path.splitext(caminho_arquivo)[1].lower()
        
        console.rule(f"Iniciando Análise: {os.path.basename(caminho_arquivo)}")

        if extensao == ".log" or extensao == ".txt":
            self._parse_linux(caminho_arquivo)
        elif extensao == ".evtx":
            self._parse_windows(caminho_arquivo)
        else:
            console.print(f"[yellow]⚠️ Extensão {extensao} desconhecida. Tentando como texto...[/yellow]")
            self._parse_linux(caminho_arquivo)
        
        return True

    def _parse_linux(self, arquivo):
        padrao = re.compile(r"Failed password for (?:invalid user )?(\w+) from ([\d.]+)")
        try:
            with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
                count = 0
                for linha in f:
                    match = padrao.search(linha)
                    if match:
                        self.resultados.append(match.groups())
                        count += 1
            console.print(f"[green]✅ Parse Linux concluído. {count} eventos detectados.[/green]")
        except Exception as e:
            console.print(f"[red]Erro ao ler log Linux: {e}[/red]")

    def _parse_windows(self, arquivo):
        # Em prod: from Evtx.Evtx import Evtx
        # Mock usado aqui:
        regex_user = re.compile(r"<Data Name='TargetUserName'>([^<]+)</Data>")
        regex_ip = re.compile(r"<Data Name='IpAddress'>([\d.]+)</Data>")
        
        count = 0
        try:
            # Substituir MockEvtx(arquivo) por Evtx(arquivo) na vida real
            for record in MockEvtx(arquivo).records():
                xml_content = record.xml()
                user_m = regex_user.search(xml_content)
                ip_m = regex_ip.search(xml_content)
                
                if user_m and ip_m:
                    self.resultados.append((user_m.group(1), ip_m.group(1)))
                    count += 1
            console.print(f"[green]✅ Parse Windows concluído. {count} eventos detectados.[/green]")
        except Exception as e:
            console.print(f"[red]Erro ao ler EVTX: {e}[/red]")

    def gerar_outputs(self):
        if not self.resultados:
            console.print("[yellow]⚠️ Sem dados para gerar relatórios.[/yellow]")
            return

        # 1. CSV
        with open("relatorio_final.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Usuário", "IP", "Data Exportação"])
            for user, ip in self.resultados:
                writer.writerow([user, ip, datetime.now().strftime("%Y-%m-%d %H:%M")])
        console.print(f"[cyan]📄 CSV salvo: relatorio_final.csv[/cyan]")

        # 2. TXT (Alertas) - Limite > 5
        contador_ip = Counter([ip for _, ip in self.resultados])
        with open("alertas_final.txt", "w", encoding="utf-8") as f:
            f.write("=== RELATÓRIO DE INCIDENTES CRÍTICOS ===\n")
            for ip, count in contador_ip.items():
                if count > 5:
                    f.write(f"[ALERTA] IP {ip} detectado com {count} falhas.\n")
        console.print(f"[cyan]📄 Alertas salvos: alertas_final.txt[/cyan]")

    def mostrar_estatisticas(self):
        if not self.resultados:
            return

        total_falhas = len(self.resultados)
        ips_unicos = set(ip for _, ip in self.resultados)
        usuarios_unicos = set(user for user, _ in self.resultados)
        
        # Top ofensores
        top_ip = Counter([ip for _, ip in self.resultados]).most_common(1)[0]
        top_user = Counter([u for u, _ in self.resultados]).most_common(1)[0]

        # Painel Rich
        stats_text = f"""
[bold]Total de falhas:[/bold] {total_falhas}
[bold]IPs únicos:[/bold] {len(ips_unicos)}
[bold]Usuários alvos únicos:[/bold] {len(usuarios_unicos)}

[red]🔥 IP mais ativo:[/red] {top_ip[0]} ({top_ip[1]} falhas)
[yellow]🎯 Usuário mais atacado:[/yellow] {top_user[0]} ({top_user[1]} tentativas)
        """
        console.print(Panel(stats_text, title="📊 Estatísticas Consolidadas", expand=False))

# --- EXECUÇÃO ---
if __name__ == "__main__":
    gerar_arquivos_teste() # Garante que existem arquivos para testar
    
    # Simulação de argumentos se não passados
    # Em produção: arquivo_alvo = sys.argv[1] se len(sys.argv) > 1 else "teste.log"
    
    analisador = AnalisadorLogs()
    
    # Vamos simular que o usuário passou dois arquivos para testar ambos
    print("\n--- TESTE 1: LOG LINUX ---")
    analisador.processar_arquivo("teste.log")
    
    print("\n--- TESTE 2: WINDOWS EVTX ---")
    analisador.processar_arquivo("teste.evtx")
    
    # Gera o report unificado
    analisador.mostrar_estatisticas()
    analisador.gerar_outputs()
