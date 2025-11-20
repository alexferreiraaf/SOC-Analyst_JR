# 📘 Resumo do Dia 55  
### Projeto Final — Automação de Logs para SOC  
**Data:** 20 de Novembro de 2025  

**Foco:** Engenharia de Detecção, Python, Parsing de Logs, Threat Intelligence e Automação.  
**Objetivo:** Desenvolver um artefato (script) capaz de analisar logs multiplataforma, detectar anomalias e gerar inteligência acionável.

---

## 1. 🔍 Fundamentos de Log Analysis

O papel do analista de SOC moderno é reduzir o tempo de detecção (MTTD) automatizando a leitura de eventos brutos.

### 📂 Fontes de Dados Críticas

| Sistema Operacional | Arquivo/Fonte        | Eventos Chave                            |
|---------------------|----------------------|-------------------------------------------|
| Linux (SSH/Auth)    | `/var/log/auth.log`  | Failed password, Accepted password        |
| Windows (Security)  | `Security.evtx`      | 4625 (Falha de Logon), 4624 (Sucesso)     |

---

### 🧠 Padrões de Ataque para Monitorar

- **Brute Force:** Múltiplas falhas de senha para o mesmo usuário em < 1 minuto.  
- **Password Spraying:** Falhas em vários usuários diferentes vindas do mesmo IP.  
- **Acesso Improvável:** Login bem-sucedido de um país não autorizado (GeoIP).

---

## 2. 🛠️ A Ferramenta: Regex Cheat Sheet

Expressões Regulares são o “canivete suíço” para extrair dados de texto não estruturado.

```python
import re

# 1. Capturar Usuário e IP (Linux/Auth.log)
# Ex: "Failed password for invalid user admin from 192.168.1.10"
regex_linux = re.compile(r"Failed password for (?:invalid user )?(\w+) from ([\d.]+)")

# 2. Capturar qualquer endereço IP
regex_ip_generico = re.compile(r"(\d{1,3}\.){3}\d{1,3}")

# 3. Capturar Usuário em formato chave=valor
regex_kv = re.compile(r"user=(\w+)")
3. 🧱 Arquitetura do Script (analisador_logs.py)

O projeto final unifica a leitura de Linux e Windows em um fluxo único de inteligência.

🏗️ Estrutura Modular

Ingestão: Detectar extensão (.log vs .evtx) e escolher o parser.

Normalização: Converter dados brutos para o formato padrão → {'user', 'ip', 'timestamp'}.

Enriquecimento (Bônus): Consultar APIs externas (ipinfo.io) para GeoIP e ASN.

Análise: Contabilizar frequências (Counter) e aplicar regras (Threshold > 5).

Resposta: Gerar CSV, alertas TXT e disparar Webhooks.

🛡️ Snippet: Lógica de Detecção e Alerta (Rich UI)
from collections import Counter
from rich.console import Console
from rich.table import Table

def gerar_analise(dados, limite=5):
    console = Console()
    contador = Counter([ip for _, ip in dados])
    
    # Tabela Visual
    tabela = Table(title="🛡️ Relatório de Ameaças")
    tabela.add_column("IP Origem", style="cyan")
    tabela.add_column("Tentativas", style="magenta")
    tabela.add_column("Status", justify="right")

    for ip, qtd in contador.most_common():
        if qtd > limite:
            status = "[bold red]⛔ BLOQUEAR[/bold red]"
            # Aqui entraria a integração com Firewall ou Discord
        else:
            status = "[green]Monitorando[/green]"
            
        tabela.add_row(ip, str(qtd), status)
    
    console.print(tabela)
4. 🤖 Integrações Avançadas (SOC Automation Plus)
🌍 Threat Intelligence (Enriquecimento)

Não basta saber o IP — é preciso identificar origem e reputação.

APIs: ipinfo.io, AbuseIPDB

Regras: Se País != BR, aumentar criticidade.

💬 ChatOps (Discord/Slack Webhooks)

Envio de alertas em tempo real.

import requests

def enviar_discord(mensagem):
    webhook_url = "https://discord.com/api/webhooks/..."
    payload = {"content": f"🚨 **SOC ALERTA:** {mensagem}"}
    requests.post(webhook_url, json=payload)

🕒 Agendamento (Cron / Task Scheduler)

Scripts de segurança devem rodar constantemente.

Linux:

crontab -e
*/10 * * * * python3 /opt/soc/analisador.py


Windows:

Task Scheduler → Trigger: “Daily” ou “At logon”

📦 Entregáveis do Projeto

analisador_logs.py — Script principal híbrido

relatorio.csv — Auditoria histórica com GeoIP/ASN

alertas.txt — Incidentes críticos para bloqueio

README.md — Documentação e instalação (pip install rich python-evtx)

💡 Conclusão do Dia

A automação remove o ruído dos logs, permitindo que o analista foque apenas no que realmente importa: identificar e responder às anomalias mais perigosas.