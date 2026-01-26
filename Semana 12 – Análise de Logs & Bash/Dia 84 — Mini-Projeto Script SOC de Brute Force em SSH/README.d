# Script SOC — Detecção de Brute Force em SSH

Este script analisa logs de autenticação Linux
e detecta ataques de brute force em SSH com base em:

- volume de falhas
- usuários privilegiados
- horário suspeito
- IP externo

Uso:
./bruteforce_ssh_soc.sh

Resultado:
Gera lista de IPs suspeitos e relatório SOC.


