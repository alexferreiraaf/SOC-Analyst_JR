# Dia 81 — Explicação Técnica do Script de Detecção de Brute Force (Bash)

Este documento explica **linha por linha** o script de detecção de brute force em SSH,
com foco em **uso prático em SOC** e **justificativa técnica**.

---

## Script analisado

```bash
#!/bin/bash

LOG="/var/log/auth.log"
THRESHOLD=5

echo "=== IPs com mais de $THRESHOLD falhas SSH ==="

grep "Failed password" "$LOG" |
awk '{print $(NF-3)}' |
sort |
uniq -c |
sort -nr |
awk -v limit=$THRESHOLD '$1 > limit {print $2 " - " $1 " tentativas"}'
```

---

## Explicação linha por linha (Visão SOC)

### `#!/bin/bash`
Define que o script será executado com o interpretador **Bash**.

**Uso em SOC:**  
Garante compatibilidade e execução correta em servidores Linux, padrão em ambientes SOC.

---

### `LOG="/var/log/auth.log"`
Armazena o caminho do arquivo de log de autenticação.

**Uso em SOC:**  
`auth.log` é a principal fonte para detectar tentativas de brute force em SSH.

---

### `THRESHOLD=5`
Define o número mínimo de falhas para considerar um IP suspeito.

**Uso em SOC:**  
Evita falso positivo e estabelece critério objetivo de detecção.

---

### `echo "=== IPs com mais de $THRESHOLD falhas SSH ==="`
Exibe um cabeçalho informativo.

**Uso em SOC:**  
Facilita leitura rápida do resultado durante incidentes.

---

### `grep "Failed password" "$LOG"`
Filtra apenas eventos de falha de login SSH.

**Uso em SOC:**  
Reduz ruído e isola eventos relevantes para brute force.

---

### `awk '{print $(NF-3)}'`
Extrai o campo que contém o IP de origem.

**Uso em SOC:**  
O IP é o principal indicador para identificar o atacante.

---

### `sort`
Ordena os IPs.

**Uso em SOC:**  
Preparação necessária para contagem correta com `uniq`.

---

### `uniq -c`
Conta quantas vezes cada IP aparece.

**Uso em SOC:**  
Transforma eventos brutos em evidência quantitativa.

---

### `sort -nr`
Ordena os IPs do maior para o menor número de falhas.

**Uso em SOC:**  
Permite priorizar o IP mais agressivo.

---

### `awk -v limit=$THRESHOLD '$1 > limit {print $2 " - " $1 " tentativas"}'`
Filtra apenas IPs acima do threshold e formata a saída.

**Uso em SOC:**  
Entrega resultado direto para tomada de decisão e resposta.

---

## Conclusão SOC

Este script automatiza a triagem inicial de brute force em SSH,
transformando logs brutos em evidência clara e acionável,
seguindo exatamente a lógica usada em operações reais de SOC.

