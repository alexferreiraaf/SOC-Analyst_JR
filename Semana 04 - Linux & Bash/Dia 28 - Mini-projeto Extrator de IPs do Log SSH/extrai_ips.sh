#!/bin/bash

# Verifica se o arquivo de log existe
if [ ! -f aut.log ]; then
  echo "Arquivo auth.log não encontrado!"
  exit 1
fi

echo "Extraindo IPs de tentativas de login falhas..."

# Extrai IPs, conta quantas vezes aparecem, ordena por quantidade
grep "Failed password" auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr > relatorio_ips.txt

echo "Relatório gerado em relatorio_ips.txt"
echo
cat relatorio_ips.txt

