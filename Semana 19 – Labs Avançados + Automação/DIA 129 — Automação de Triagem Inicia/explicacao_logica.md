# Lógica Utilizada na Classificação Automática

## Objetivo

Automatizar uma triagem inicial de alertas do Wazuh utilizando critérios simples para priorização de investigação.

## Critérios considerados

### 1. Severidade do alerta (rule.level)

- Level 0–5 → Score 1
- Level 6–9 → Score 2
- Level ≥10 → Score 3

Esse valor representa o risco base do evento.

---

### 2. Usuário privilegiado

Caso o usuário envolvido seja:

- root
- admin

São adicionados **+2 pontos** ao score, devido ao maior impacto potencial.

---

### 3. Origem do IP

IPs que não pertencem às redes privadas:

- 192.168.0.0/16
- 10.0.0.0/8
- 172.16.0.0/12

recebem **+2 pontos**, sendo tratados como possíveis origens externas.

---

### 4. Horário incomum

Eventos ocorridos entre **00:00 e 06:00** recebem **+1 ponto**, considerando maior probabilidade de atividade suspeita.

---

## Classificação Final

| Score | Classificação |
|---------|--------------|
| 1–2 | BAIXO |
| 3–5 | MÉDIO |
| ≥6 | ALTO |

---

## Limitações

Este modelo é simplificado e não substitui a análise humana.

Ele não considera fatores como:

- Histórico do usuário
- Reputação do IP
- Correlação entre múltiplos eventos
- Contexto operacional da empresa

Seu objetivo é apenas acelerar a triagem inicial e auxiliar na priorização dos alertas.