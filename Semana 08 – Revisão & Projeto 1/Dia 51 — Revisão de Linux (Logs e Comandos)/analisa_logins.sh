#!/bin/bash

LOG="/var/log/auth.log"
OUTPUT="relatorio_login.txt"

echo "=== Relatório de Tentativas de Login ===" > $OUTPUT
echo "Data de geração: $(date)" >> $OUTPUT
echo "" >> $OUTPUT

echo "🔹 Top 5 IPs com mais falhas:" >> $OUTPUT
grep "Failed password" $LOG | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head -5 >> $OUTPUT
echo "" >> $OUTPUT

echo "🔹 Logins bem-sucedidos recentes:" >> $OUTPUT
grep "Accepted password" $LOG | tail -n 5 >> $OUTPUT

echo "" >> $OUTPUT
echo "Relatório salvo em $OUTPUT"


