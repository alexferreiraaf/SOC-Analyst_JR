#!/bin/bash

# Arquivo de origem
ARQUIVO="/var/ossec/logs/alerts/alerts.json"

# Nome do arquivo de saída
SAIDA="criticos_$(date +%F_%H-%M).json"

echo "====================================="
echo " Extraindo alertas críticos do Wazuh "
echo "====================================="
echo

# Verifica se o arquivo existe
if [ ! -f "$ARQUIVO" ]; then
    echo "Erro: arquivo não encontrado."
    exit 1
fi

# Filtra eventos com severidade >= 10
jq 'select(.rule.level >= 10)' "$ARQUIVO" > "$SAIDA"

TOTAL=$(jq 'select(.rule.level >= 10)' "$ARQUIVO" | wc -l)

echo "Total de alertas críticos encontrados: $TOTAL"
echo
echo "Arquivo gerado: $SAIDA"
echo

echo "Top 5 IPs ofensores:"
jq -r 'select(.rule.level >= 10) | .data.srcip // empty' "$ARQUIVO" \
| sort \
| uniq -c \
| sort -nr \
| head -5

echo
echo "Processo concluído."