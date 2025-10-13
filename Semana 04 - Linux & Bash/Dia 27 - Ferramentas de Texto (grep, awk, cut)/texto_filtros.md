# Ferramentas de Texto — grep, cut e awk

## 1. Diferenças principais
- **grep:** busca linhas com padrões específicos.
- **cut:** extrai colunas delimitadas.
- **awk:** interpreta, formata e processa o texto.

## 2. Exemplos de uso
- `grep "FAIL" log_exemplo.txt`
- `cut -d " " -f4 log_exemplo.txt`
- `awk '{print $4, $5}' log_exemplo.txt`

## 3. Cenário prático
Usei um arquivo de log e consegui:
- Contar falhas com `awk`;
- Extrair usuários com `cut`;
- Buscar eventos específicos com `grep`.

## 4. Conclusão
Essas ferramentas são essenciais para análise de logs e automação no Linux.
Combinadas em pipelines (`|`), se tornam extremamente poderosas.

