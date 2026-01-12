# Dia 70 — Análise SOC

## Cenário
Alerta disparado indicando possível brute force SSH.

## Avaliação
- IP externo repetindo falhas
- Tentativas em múltiplos usuários
- Comportamento automatizado

## Decisão SOC
Classificado como brute force confirmado.

## Resposta
- Bloqueio temporário no firewall
- Reset de senhas se necessário
- Monitoramento contínuo

## Conclusão
Detecção eficaz integrando Splunk + Regex + Python.
