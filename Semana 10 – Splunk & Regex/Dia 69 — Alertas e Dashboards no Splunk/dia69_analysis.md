# Dia 69 — Análise SOC com Regex

## Observações
Regex permitiu extrair IPs e usuários diretamente do log bruto.

## Indicadores identificados
- IP repetido muitas vezes
- Tentativas em usuários inválidos
- Alta frequência em curto período

## Interpretação SOC
Esses padrões indicam ataque automatizado de brute force.

## Ações recomendadas
- Abrir incidente
- Bloquear IP no firewall
- Monitorar contas afetadas
