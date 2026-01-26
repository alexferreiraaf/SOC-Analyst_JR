# Explicação SOC — Detecção de Brute Force em SSH

## Visão Executiva
Este script foi desenvolvido para identificar ataques de brute force em SSH a partir dos logs de autenticação de servidores Linux.

Ele analisa padrões de falhas repetidas de login que indicam tentativas automatizadas de acesso não autorizado.

## O que o script detecta
O script identifica:
- IPs externos com múltiplas falhas de login
- Tentativas contra usuários privilegiados (root, admin)
- Atividades em horários suspeitos (madrugada)
- Volume de tentativas acima do limite definido

## Por que isso é importante
Ataques de brute force podem resultar em:
- Comprometimento do servidor
- Acesso não autorizado
- Impacto operacional e de segurança

A detecção antecipada permite resposta rápida e mitigação do risco.

## Conclusão
O script converte logs técnicos em informação acionável para tomada de decisão em SOC, mesmo sem o uso de SIEM.
