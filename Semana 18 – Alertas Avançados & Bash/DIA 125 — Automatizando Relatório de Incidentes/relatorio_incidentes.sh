# `relatorio_incidentes.sh`

```bash
#!/bin/bash

ARQUIVO="/var/ossec/logs/alerts/alerts.json"

DATA_ATUAL=$(date)
DATA_ARQUIVO=$(date +%F)

SAIDA="relatorio_${DATA_ARQUIVO}.txt"

echo "Gerando relatório..."

# Total de alertas críticos
TOTAL=$(jq 'select(.rule.level >= 10)' "$ARQUIVO" | wc -l)

# IP mais recorrente
IP_TOP=$(jq -r 'select(.rule.level >= 10) | .data.srcip // empty' "$ARQUIVO" \
| sort | uniq -c | sort -nr | head -1)

# Usuário mais afetado
USER_TOP=$(jq -r 'select(.rule.level >= 10) | .data.dstuser // empty' "$ARQUIVO" \
| sort | uniq -c | sort -nr | head -1)

# Regra mais disparada
RULE_TOP=$(jq -r 'select(.rule.level >= 10) | .rule.description // empty' "$ARQUIVO" \
| sort | uniq -c | sort -nr | head -1)

# Classificação de risco
if [ "$TOTAL" -gt 50 ]; then
    NIVEL="ALTO"
elif [ "$TOTAL" -gt 10 ]; then
    NIVEL="MODERADO"
else
    NIVEL="BAIXO"
fi

{
echo "==========================================="
echo "RELATÓRIO AUTOMÁTICO DE INCIDENTES"
echo "==========================================="
echo
echo "Data de geração: $DATA_ATUAL"
echo
echo "Total de alertas críticos: $TOTAL"
echo
echo "Classificação geral de risco: $NIVEL"
echo
echo "IP mais recorrente:"
echo "$IP_TOP"
echo
echo "Usuário mais afetado:"
echo "$USER_TOP"
echo
echo "Regra mais disparada:"
echo "$RULE_TOP"
echo
echo "-------------------------------------------"
echo "Top 3 IPs ofensores:"
jq -r 'select(.rule.level >= 10) | .data.srcip // empty' "$ARQUIVO" \
| sort | uniq -c | sort -nr | head -3
echo "-------------------------------------------"
echo
echo "Relatório gerado automaticamente."
} > "$SAIDA"

echo "Relatório salvo em: $SAIDA"
```

---


