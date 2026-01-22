# Decisão SOC — Dia 80

## Evidências Observadas
- Múltiplas falhas de login SSH
- Repetição do mesmo IP atacante
- Usuários comuns e privilegiados como alvo
- Alta frequência em curto intervalo de tempo

## Classificação do Incidente
- Tipo: Brute Force SSH
- Severidade: Média → Alta

## Ações Recomendadas
- Bloqueio temporário do IP atacante
- Hardening do serviço SSH
- Implementação de fail2ban
- Monitoramento contínuo do host
