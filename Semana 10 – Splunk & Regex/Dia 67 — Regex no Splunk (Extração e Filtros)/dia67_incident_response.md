# Dia 67 — Análise de Incidente SOC

## Cenário
- IP: 45.77.89.100
- Usuário alvo: admin
- Falhas: 18 em 3 minutos

## Análise
O volume de falhas em curto intervalo caracteriza ataque de brute force.
Usuário admin aumenta criticidade.

## Severidade
High

## Ações recomendadas
- Investigar imediatamente
- Bloquear IP no firewall
- Forçar reset de senha do usuário admin
- Monitorar novos eventos

## Conclusão
Incidente realista de brute force, exigindo resposta rápida do SOC.
