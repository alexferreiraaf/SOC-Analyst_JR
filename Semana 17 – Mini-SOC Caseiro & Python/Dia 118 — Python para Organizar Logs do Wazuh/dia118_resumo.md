# Dia 118 — Python para Organizar Logs do Wazuh

## Objetivo

Criar uma automação em Python para analisar o alerts.json do Wazuh, filtrar por severidade e agrupar alertas por IP.

---

## Pipeline do dia

alerts.json  
↓  
Python  
↓  
Filtro por level (>= 10)  
↓  
Agrupamento por srcip  
↓  
Geração de CSV  

---

## O que foi feito

- Leitura de JSON por linha
- Tratamento de erros
- Filtro por severidade
- Contagem de alertas por IP
- Geração do arquivo ips_suspeitos.csv

---

## Resultado

Capacidade de:
- Automatizar triagem de alertas
- Reduzir ruído no SIEM
- Priorizar IPs reincidentes
- Integrar SIEM + Python (diferencial para SOC)