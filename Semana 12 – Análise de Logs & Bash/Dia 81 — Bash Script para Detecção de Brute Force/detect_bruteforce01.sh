#!/bin/bash

# Verificação de parâmetros
if [ $# -ne 2 ]; then
    echo "Uso correto: $0 <arquivo_de_log> <threshold>"
    echo "Exemplo: $0 auth_day81_long.log 5"
    exit 1
fi

LOG="$1"
THRESHOLD="$2"

# Verifica se o arquivo existe
if [ ! -f "$LOG" ]; then
    echo "Erro: arquivo de log não encontrado -> $LOG"
    exit 1
fi

echo "=== IPs com mais de $THRESHOLD falhas SSH ==="

grep "Failed password" "$LOG" |
awk '{print $(NF-3)}' |
sort |
uniq -c |
sort -nr |
awk -v limit="$THRESHOLD" '$1 > limit {print $2 " - " $1 " tentativas"}'

