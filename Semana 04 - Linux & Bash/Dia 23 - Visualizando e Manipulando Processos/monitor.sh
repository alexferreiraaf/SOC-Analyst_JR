#!/bin/bash
echo "📅 Data: $(date)"
echo "🧠 Top 5 processos por CPU:"
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -6
echo "💾 Uso de memória:"
free -h

