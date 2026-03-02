# Dia 117 — Extração de Logs do Wazuh

## Objetivo

Aprender onde o Wazuh armazena alertas e como extrair dados em JSON para análise e automação.

---

## Conceitos-chave

- Arquivo principal: /var/ossec/logs/alerts/alerts.json
- Cada linha = 1 alerta em formato JSON
- Campos importantes: timestamp, agent.name, rule.id, rule.level, srcip, usuário
- JSON permite integração com Python, relatórios e automação

---

## Prática

- Localização do alerts.json no Manager
- Leitura manual da estrutura dos alertas
- Filtragem com grep (triagem rápida)
- Filtragem estruturada com jq (extração de campos relevantes)
- Mini-análise de IP suspeito

---

## Resultado

Capacidade de:
- Extrair dados brutos do SIEM
- Filtrar informações relevantes
- Preparar dados para automação
- Pensar como SOC focado em análise técnica