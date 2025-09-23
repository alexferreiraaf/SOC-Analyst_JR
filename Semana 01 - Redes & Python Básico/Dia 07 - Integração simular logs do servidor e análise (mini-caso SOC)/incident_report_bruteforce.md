# Incident Report – Brute Force SSH
ID: SOC-2025-001

## Resumo Executivo
Detectamos tentativas de brute force SSH contra o servidor interno 192.168.10.10 na porta 22.
Um IP externo realizou múltiplas tentativas falhas em poucos segundos.

## Timeline
2025-09-07 08:15:23 Login Failed – SRC=185.222.123.45
2025-09-07 08:15:27 Login Failed – SRC=185.222.123.45
2025-09-07 08:15:30 Login Failed – SRC=185.222.123.45

## IPs Suspeitos
- 185.222.123.45 (3 tentativas)

## Ação Recomendada
- Bloquear IP no firewall.
- Criar regra de correlação no SIEM para alertar brute force SSH.
- Escalonar para N2 caso persistam tentativas.

## Evidências
- Output do script detect_bruteforce.py.
- Logs originais em ssh_auth.log.
