#!/bin/bash
# Script: mudar_permissoes.sh
# Objetivo: alterar permissões de um arquivo para 644

# 1. Verifica se o parâmetro foi passado
if [ -z "$1" ]; then
    echo "Uso: $0 <nome_do_arquivo>"
    exit 1
fi

# 2. Mostra as permissões atuais
echo "🔹 Permissões atuais:"
ls -l "$1"

# 3. Muda as permissões para 644
chmod 644 "$1"

# 4. Mostra as novas permissões
echo "🔹 Novas permissões:"
ls -l "$1"
