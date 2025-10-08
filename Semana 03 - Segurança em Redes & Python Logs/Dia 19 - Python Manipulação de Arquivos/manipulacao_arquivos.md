# manipulação_arquivos.md

## Resumo rápido
- open(), with, read(), readline(), readlines(), write(), writelines()
- Modos: r, w, a, r+, x

## Scripts implementados
- arquivos_teste.py — cria `teste.txt` e lê.
- filtra_ips.py — filtra IPs que começam com 192.168. e gera ips_saida.txt.
- contar_ocorrencias.py — conta palavras-chave em logs.
- extrair_ips_regex.py — extrai padrões IPv4 via regex.
- gera_blacklist.py — gera blacklist.csv a partir de ips_saida.txt.

## Outputs (exemplos)
- Saída de `python arquivos_teste.py`:
Conteúdo do arquivo: ['Primeira linha\n', 'Segunda linha\n']

```
- Saída de `python filtra_ips.py`:

```

IPs escritos em ips_saida.txt: 4

- 192.168.1.10
- 192.168.1.15
- 192.168.0.12
- 192.168.5.100
## Observações
- Para arquivos muito grandes, iterar linha a linha é preferível a `read()`.
- Sempre especificar encoding.
- Testar scripts em ambiente controlado.

