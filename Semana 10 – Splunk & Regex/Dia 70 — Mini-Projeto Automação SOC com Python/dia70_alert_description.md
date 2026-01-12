# Dia 70 — Descrição do Alerta SOC

## Nome do Alerta
[SECURITY] Possible SSH Brute Force

## Descrição
Detecta múltiplas falhas de autenticação SSH vindas do mesmo endereço IP em curto intervalo de tempo.

## Critério de Detecção
- Mais de 10 falhas de login
- Mais de 5 usuários distintos
- Janela de 10 minutos

## Severidade
Média (P2)

## Ação Recomendada
- Bloquear IP ofensivo
- Investigar usuários impactados
- Monitorar recorrência
