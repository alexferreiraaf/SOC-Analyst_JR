#!/bin/bash

LOG="auth.log"
THRESHOLD=5
USERS="root|admin"
HORAS="00:|01:|02:|03:|04:|05:"

echo "==== DETECÇÃO SOC — BRUTE FORCE SSH ===="
echo "Data: $(date)"
echo ""

grep "Failed password" $LOG |
grep -E "$USERS" |
grep -E "$HORAS" |
grep -v "127.0.0.1" |
awk '{print $(NF-3)}' |
sort |
uniq -c |
sort -nr |
awk -vlimit=$THRESHOLD '$1 > limit {print $2 " - " $1 " tentativas"}' |
tee evidencias.txt


