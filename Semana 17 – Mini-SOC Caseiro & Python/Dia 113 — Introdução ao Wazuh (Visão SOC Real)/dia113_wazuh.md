# Dia 113 — Wazuh (Visão SOC Real)

## O que é o Wazuh

O Wazuh é uma plataforma open source que combina funcionalidades de SIEM e EDR, oferecendo monitoramento de segurança, detecção de ameaças, resposta a incidentes e compliance.

Na prática de um SOC, ele é utilizado para:

- Detectar atividades suspeitas em endpoints
- Correlacionar eventos automaticamente
- Gerar alertas com níveis de severidade
- Monitorar integridade de arquivos
- Apoiar auditorias e conformidade (CIS, PCI-DSS, etc.)

---

## Wazuh é SIEM ou EDR?

Ele atua como ambos:

- **SIEM:** coleta, correlaciona e gera alertas a partir de eventos
- **EDR:** monitora atividades diretamente no endpoint por meio do agente

---

## Arquitetura do Wazuh

Fluxo simplificado:

Host (Linux/Windows)
↓
Wazuh Agent
↓
Wazuh Manager
↓
Indexer (OpenSearch)
↓
Dashboard

---

### Componentes

### Agent
- Instalado no endpoint
- Coleta logs, eventos de segurança, alterações de arquivos e atividades de processo

### Manager
- Recebe dados dos agentes
- Aplica regras
- Gera alertas

### Indexer
- Armazena e indexa eventos
- Permite buscas rápidas

### Dashboard
- Interface usada pelo analista SOC
- Exibe alertas, regras, severidade e dados do host

---

## Onde o Wazuh entra no fluxo SOC?

1. Coleta eventos no endpoint
2. Aplica regras de detecção
3. Gera alerta
4. Analista realiza triagem
5. Caso necessário, incidente é aberto