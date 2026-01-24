#!/bin/bash

# ==========================
# Validação de parâmetros
# ==========================
if [ "$#" -lt 4 ]; then
  echo "Uso: $0 <log_file> <threshold> <horario_inicio-horario_fim> <usuarios_criticos>"
  echo "Exemplo: $0 auth.log 5 00-06 root,admin"
  exit 1
fi

LOG_FILE="$1"
THRESHOLD="$2"
HORARIO_RANGE="$3"
USUARIOS_CRITICOS="$4"

# ==========================
# Preparação dos parâmetros
# ==========================
HORARIO_REGEX=$(echo "$HORARIO_RANGE" | sed 's/-/:|/g')
USUARIOS_REGEX=$(echo "$USUARIOS_CRITICOS" | sed 's/,/|/g')

echo "=============================================="
echo " DETECÇÃO REFINADA DE BRUTE FORCE SSH (SOC)"
echo "=============================================="
echo "Log analisado       : $LOG_FILE"
echo "Threshold           : $THRESHOLD falhas"
echo "Horário suspeito    : $HORARIO_RANGE"
echo "Usuários críticos   : $USUARIOS_CRITICOS"
echo "----------------------------------------------"

# ==========================
# Pipeline de detecção SOC
# ==========================
grep "Failed password" "$LOG_FILE" |
grep -E "$USUARIOS_REGEX" |
grep -v "127.0.0.1" |
grep -E "$HORARIO_REGEX:" |
awk '{print $(NF-3)}' |
sort |
uniq -c |
sort -nr |
awk -v limit="$THRESHOLD" '$1 > limit {print $2 " - " $1 " tentativas"}'

echo "=============================================="
echo " Análise concluída"
echo "=============================================="

