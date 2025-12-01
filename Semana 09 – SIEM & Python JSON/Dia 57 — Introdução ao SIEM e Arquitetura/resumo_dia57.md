# 📘 Resumo do Dia 57 — Introdução ao SIEM e Arquitetura
## 🎯 Objetivo do Dia

Compreender o que é um SIEM, como funciona sua arquitetura interna e qual o fluxo de processamento de logs utilizado por analistas SOC para detectar ameaças.

---

## 🧩 1. Conceitos Fundamentais
### 🔐 O que é SIEM (Security Information and Event Management)

Um SIEM é uma plataforma que reúne:

- Coleta de logs

- Normalização e correlação de eventos

- Geração de alertas

- Dashboards e visualização

É uma ferramenta essencial para analistas SOC, permitindo detecção, investigação e resposta a incidentes.

### 🏗️ 2. Componentes Principais de um SIEM
### 📥 Data Sources

São as fontes que geram eventos. Exemplos:

- Windows Event Logs

- Syslog (Linux)

- Firewalls

- IDS/IPS

- Proxy / Web Gateway

### 🚚 Collectors / Forwarders

Agentes que enviam logs para o SIEM.
Exemplos:

- Splunk Universal Forwarder

- Syslog-ng

- Filebeat

### 🧩 Parser / Normalização

Transforma dados brutos em campos estruturados (ex: `src_ip`, `user`, `action`).

**🔎 Correlation Engine**

Aplica regras lógicas para identificar comportamentos suspeitos e gerar alertas.

**📊 Dashboards / Visualização**

Área onde analistas SOC fazem buscas, dashboards e investigações.

### 🔄 3. Ciclo de Vida de um SIEM

**1. Coleta de Logs**

**2. Normalização e Parsing**

**3. Correlação**

**4. Geração de Alertas**

**5. Investigação pelo SOC**

🧠 Atividades Práticas do Dia

Criar um diagrama do fluxo SIEM
(Excalidraw, Lucidchart, PowerPoint, Draw.io).

Listar 5 fontes de log comuns em ambientes corporativos.

Ler o artigo oficial:
Splunk SIEM Overview

Pesquisar 3 alternativas ao Splunk, como:

IBM QRadar

ELK Stack (Elastic)

Wazuh SIEM