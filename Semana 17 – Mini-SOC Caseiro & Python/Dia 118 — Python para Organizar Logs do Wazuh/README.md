# Dia 118 — Automação Wazuh com Python

## 📌 Objetivo

Criar uma automação simples para organizar alertas do Wazuh
e auxiliar na priorização de investigação no SOC.

---

## 🧠 O que o script faz

1. Lê o arquivo alerts.json do Wazuh
2. Filtra alertas com severidade >= 10
3. Agrupa por IP de origem (srcip)
4. Conta quantos alertas cada IP gerou
5. Gera um CSV para análise externa

---

## 🎯 Por que isso ajuda o SOC?

- Reduz ruído de alertas repetidos
- Destaca IPs reincidentes
- Permite priorização baseada em volume
- Facilita geração de relatórios
- Integra SIEM com Python

---

## ▶ Como executar

```bash
python3 organize_alerts.py