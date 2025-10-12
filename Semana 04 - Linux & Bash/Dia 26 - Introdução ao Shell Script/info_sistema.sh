#!/bin/bash
echo "==== Informações do Sistema ===="
echo "Usuário: $(whoami)"
echo "Hostname: $(hostname)"
echo "Data e hora: $(date)"
echo "Tempo ligado: $(uptime -p)"
echo "Espaço em disco:"
df -h | grep "/dev/"

