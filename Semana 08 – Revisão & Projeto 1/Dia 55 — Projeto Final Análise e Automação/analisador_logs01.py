import re
import csv
import os
import json
import time
from collections import Counter
from datetime import datetime

# --- CONFIGURAÇÕES (PREENCHA AQUI NA VIDA REAL) ---
# Obtenha token grátis em: https://ipinfo.io/signup
IPINFO_TOKEN = "SEU TOKEN AQUI" 
# Crie um Webhook no seu servidor Discord (Editar Canal > Integrações > Webhooks)
DISCORD_WEBHOOK_URL = "" 

# --- DEPENDÊNCIAS EXTERNAS (TENTATIVA DE IMPORT) ---
try:
    import requests
except ImportError:
    requests = None # Fallback se não tiver requests instalado

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    console = Console()
except ImportError:
    class Console:
        def print(self, text, style=None): print(text)
        def rule(self, title): print(f"--- {title} ---")
    console = Console()

# --- MÓDULO DE SIMULAÇÃO (MOCKS) ---
class MockEvtx:
    """Simula a biblioteca python-evtx"""
    def __init__(self, filename): self.filename = filename
    def records(self):
        dados = [
            (4625, "admin", "192.168.1.15", "2025-11-20 10:00"),
            (4625, "root", "45.33.22.11", "2025-11-20 11:00"), # IP EUA
            (4625, "guest", "185.200.11.1", "2025-11-20 11:05"), # IP Rússia (Simulado)
            (4625, "support", "192.168.1.200", "2025-11-20 12:00")
        ] * 5
        for eid, user, ip, ts in dados:
            xml_str = f"<Event><System><EventID>{eid}</EventID></System><EventData><Data Name='TargetUserName'>{user}</Data><Data Name='IpAddress'>{ip}</Data></EventData></Event>"
            yield type('obj', (object,), {'xml': lambda: xml_str})

def gerar_arquivos_teste():
    if not os.path.exists("teste.log"):
        # Gerar IPs variados para testar GeoIP
        c = "Nov 20 10:00:01 srv sshd: Failed password for root from 8.8.8.8 port 22\n" # Google US
        c += "Nov 20 10:00:02 srv sshd: Failed password for admin from 45.33.22.11 port 22\n" # Akamai US
        c += "Nov 20 10:00:03 srv sshd: Failed password for user from 192.168.0.50 port 22\n" # Local
        with open("teste.log", "w") as f: f.write(c * 10)
    if not os.path.exists("teste.evtx"):
        with open("teste.evtx", "w") as f: f.write("MOCK")

# --- CLASSE DE THREAT INTELLIGENCE ---
class ThreatIntel:
    def __init__(self):
        self.cache = {} # Evita consultar o mesmo IP repetidamente (Rate Limit)

    def consultar_ip(self, ip):
        """Consulta API ipinfo.io. Retorna (Pais, Org)."""
        # 1. Verifica Cache
        if ip in self.cache:
            return self.cache[ip]

        # 2. IPs Privados (LAN) não consultam API
        if ip.startswith("192.168.") or ip.startswith("10.") or ip.startswith("127."):
            return "BR (LAN)", "Rede Local"

        # 3. Consulta Real (Se requests existir e tiver Token)
        if requests and IPINFO_TOKEN != "SEU_TOKEN_AQUI":
            try:
                url = f"https://ipinfo.io/{ip}?token={IPINFO_TOKEN}"
                resp = requests.get(url, timeout=3)
                if resp.status_code == 200:
                    dados = resp.json()
                    pais = dados.get("country", "Unknown")
                    org = dados.get("org", "Unknown ISP")
                    self.cache[ip] = (pais, org)
                    return pais, org
            except Exception:
                pass

        # 4. Mock/Fallback (Para demonstração funcionar sem API Key)
        if ip == "8.8.8.8": return "US", "Google LLC"
        if ip == "45.33.22.11": return "US", "Linode"
        if ip == "185.200.11.1": return "RU", "Evil Corp"
        
        return "XX", "N/A"

class Notificador:
    @staticmethod
    def enviar_discord(mensagem):
        if not DISCORD_WEBHOOK_URL or not requests:
            console.print(f"[dim]ℹ️ Webhook não configurado. Simulando envio: {mensagem[:50]}...[/dim]")
            return

        payload = {"content": mensagem, "username": "SOC Bot 🤖"}
        try:
            requests.post(DISCORD_WEBHOOK_URL, json=payload)
            console.print("[green]✅ Alerta enviado para o Discord![/green]")
        except Exception as e:
            console.print(f"[red]Erro ao enviar Discord: {e}[/red]")

# --- NÚCLEO DO ANALISADOR ---

class AnalisadorLogs:
    def __init__(self):
        self.resultados = [] 
        self.intel = ThreatIntel() # Instancia o módulo de inteligência

    def processar_arquivo(self, caminho_arquivo):
        if not os.path.exists(caminho_arquivo): return False
        
        console.rule(f"Analisando: {os.path.basename(caminho_arquivo)}")
        extensao = os.path.splitext(caminho_arquivo)[1].lower()

        dados_temp = []
        if extensao == ".evtx":
            # Mock de leitura Windows
            regex_user = re.compile(r"<Data Name='TargetUserName'>([^<]+)</Data>")
            regex_ip = re.compile(r"<Data Name='IpAddress'>([\d.]+)</Data>")
            for record in MockEvtx(caminho_arquivo).records():
                xml = record.xml()
                u, i = regex_user.search(xml), regex_ip.search(xml)
                if u and i: dados_temp.append((u.group(1), i.group(1)))
        else:
            # Leitura Linux/Texto
            padrao = re.compile(r"Failed password for (?:invalid user )?(\w+) from ([\d.]+)")
            with open(caminho_arquivo, "r", errors="ignore") as f:
                for linha in f:
                    m = padrao.search(linha)
                    if m: dados_temp.append(m.groups())

        # Enriquecimento (Adiciona País e Org aos dados)
        console.print(f"[yellow]🌍 Enriquecendo {len(dados_temp)} eventos com GeoIP...[/yellow]")
        for user, ip in dados_temp:
            pais, org = self.intel.consultar_ip(ip)
            self.resultados.append({
                "user": user, 
                "ip": ip, 
                "pais": pais, 
                "org": org,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
        
        console.print(f"[green]✅ Processamento concluído.[/green]")

    def gerar_outputs(self):
        if not self.resultados: return

        # 1. CSV Enriquecido
        colunas = ["user", "ip", "pais", "org", "timestamp"]
        with open("relatorio_soc_pro.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=colunas)
            writer.writeheader()
            writer.writerows(self.resultados)
        console.print(f"[cyan]📄 CSV Enriquecido salvo: relatorio_soc_pro.csv[/cyan]")

        # 2. Análise de Alertas e Webhook
        self._analisar_alertas()

    def _analisar_alertas(self):
        # Conta falhas por IP
        ips = [d['ip'] for d in self.resultados]
        ip_counts = Counter(ips)
        
        # Pega metadados do IP (já enriquecido)
        # Truque: cria um dicionario {ip: {dados}} para acesso rápido
        ip_meta = {d['ip']: {'pais': d['pais'], 'org': d['org']} for d in self.resultados}

        console.rule("Alertas de Segurança")
        
        for ip, count in ip_counts.items():
            pais = ip_meta[ip]['pais']
            org = ip_meta[ip]['org']
            
            # REGRA DE ALERTA 1: Estrangeiro (Fora do BR)
            if pais != "BR (LAN)" and pais != "BR":
                msg = f"🚨 **ALERTA CRÍTICO (GEOIP)**\nIP: `{ip}`\nOrigem: {pais} - {org}\nTentativas: {count}"
                console.print(f"[bold red]{msg}[/bold red]")
                Notificador.enviar_discord(msg)
            
            # REGRA DE ALERTA 2: Ataque Volumoso (> 50)
            elif count > 50:
                msg = f"⚠️ **ALERTA DE VOLUME**\nIP: `{ip}`\nTentativas: {count}"
                Notificador.enviar_discord(msg)

# --- EXECUÇÃO ---
if __name__ == "__main__":
    gerar_arquivos_teste()
    
    app = AnalisadorLogs()
    # Processa Linux e Windows
    app.processar_arquivo("teste.log")
    app.processar_arquivo("teste.evtx")
    
    app.gerar_outputs()
