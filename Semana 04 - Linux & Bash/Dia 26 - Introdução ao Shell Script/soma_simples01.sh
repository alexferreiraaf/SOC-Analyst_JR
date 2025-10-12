#!/bin/bash

echo "Digite o primeiro número:"
read n1

# Validação para garantir que n1 é um número
if [[ ! $n1 =~ ^[0-9]+$ ]]; then
    echo "Erro: o primeiro valor não é um número válido."
    exit 1
fi

echo "Digite o segundo número:"
read n2

# Validação para garantir que n2 é um número
if [[ ! $n2 =~ ^[0-9]+$ ]]; then
    echo "Erro: o segundo valor não é um número válido."
    exit 1
fi

resultado=$((n1 + n2))
echo "A soma é: $resultado"
