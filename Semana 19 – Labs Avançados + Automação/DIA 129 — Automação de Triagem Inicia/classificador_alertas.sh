```bash
#!/bin/bash

# ======================================================
# Classificador Automático de Alertas - Wazuh
# DIA 129
# ======================================================

ARQUIVO="/var/ossec/logs/alerts/alerts.json"

# Obtém informações do último alerta
LEVEL=$(jq -r '.rule.level' "$ARQUIVO" | tail -1)
USER=$(jq -r '.data.dstuser // "desconhecido"' "$ARQUIVO" | tail -1)
IP=$(jq -r '.data.srcip // "desconhecido"' "$ARQUIVO" | tail -1)

RISCO=0

# ------------------------------------------------------
# Classificação base pelo nível do alerta
# ------------------------------------------------------

if [ "$LEVEL" -ge 10 ]; then
    RISCO=3
elif [ "$LEVEL" -ge 6 ]; then
    RISCO=2
else
    RISCO=1
fi

# ------------------------------------------------------
# Usuário privilegiado
# ------------------------------------------------------

if [[ "$USER" == "root" || "$USER" == "admin" ]]; then
    RISCO=$((RISCO + 2))
fi

# ------------------------------------------------------
# Verificação simples de IP externo
# ------------------------------------------------------

if [[ ! "$IP" =~ ^192\.168\. ]] && \
   [[ ! "$IP" =~ ^10\. ]] && \
   [[ ! "$IP" =~ ^172\.1[6-9]\. ]] && \
   [[ ! "$IP" =~ ^172\.2[0-9]\. ]] && \
   [[ ! "$IP" =~ ^172\.3[0-1]\. ]]; then

    RISCO=$((RISCO + 2))
fi

# ------------------------------------------------------
# Verificação de horário incomum
# ------------------------------------------------------

HORA=$(date +%H)

if [ "$HORA" -ge 0 ] && [ "$HORA" -lt 6 ]; then
    RISCO=$((RISCO + 1))
fi

# ------------------------------------------------------
# Classificação final
# ------------------------------------------------------

if [ "$RISCO" -ge 6 ]; then
    CLASSIFICACAO="ALTO"
elif [ "$RISCO" -ge 3 ]; then
    CLASSIFICACAO="MÉDIO"
else
    CLASSIFICACAO="BAIXO"
fi

echo "========== TRIAGEM AUTOMÁTICA =========="
echo "Level...............: $LEVEL"
echo "Usuário.............: $USER"
echo "IP..................: $IP"
echo "Score de risco......: $RISCO"
echo "Classificação final.: $CLASSIFICACAO"
echo "========================================"
```