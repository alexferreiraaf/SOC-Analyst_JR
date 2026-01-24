#!/bin/bash

LOG="auth.log"
THRESHOLD=5

echo "=== IPs com mais de $THRESHOLD falhas SSH ==="

grep "Failed password" $LOG |
awk '{print $(NF-3)}' |
sort |
uniq -c |
sort -nr |
awk -v limit=$THRESHOLD '$1 > limit {print $2 " - " $1 " tentativas"}'


