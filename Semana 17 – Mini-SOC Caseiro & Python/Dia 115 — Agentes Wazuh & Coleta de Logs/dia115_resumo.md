# Dia 115 — Agentes Wazuh & Coleta de Logs

## Objetivo

Comprovar que o SIEM funciona na prática, entendendo o fluxo completo:

Host → Agent → Manager → Regra → Alerta → Dashboard

---

## O que foi feito

- Instalação do Wazuh Agent em uma VM Linux
- Registro e ativação do agent no Manager
- Geração de eventos reais via SSH (login correto e falho)
- Análise dos alertas no Dashboard

---

## Aprendizado Principal

- O Agent apenas coleta eventos
- O Manager aplica regras e decide se é alerta
- Tentativas repetidas de login falho podem gerar alerta de brute force
- O ciclo completo de detecção foi validado

---

## Resultado

SIEM funcional com:
- Agent ativo
- Logs coletados
- Regras aplicadas
- Alertas visíveis

Agora o ambiente está pronto para simular incidentes reais.