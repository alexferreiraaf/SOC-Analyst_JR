# Dia 119 — Mini-Projeto: Relatório Inicial com Wazuh

## Objetivo

Simular um incidente real (ex: brute force SSH) e produzir um relatório SOC profissional com base em alertas do Wazuh.

---

## Pipeline do dia

alerts.json  
↓  
Python (filtro por severidade e SSH)  
↓  
Análise de IP suspeito  
↓  
Criação de timeline  
↓  
Relatório técnico (.md)

---

## O que foi feito

- Filtragem de alertas relevantes
- Identificação de IP reincidente
- Análise de janela de tempo
- Construção de timeline do incidente
- Redação de relatório inicial com evidências e recomendações

---

## Resultado

Capacidade de:
- Investigar alerta como analista SOC
- Correlacionar eventos
- Documentar incidente de forma profissional
- Integrar SIEM + Python + análise humana