# DIA 148 — Python para Segurança

## Conceitos Revisados

### Variáveis

```python
ip = "185.223.89.44"
```

### Loops

```python
for linha in arquivo:
    print(linha)
```

### Funções

```python
def mostrar_ip(ip):
    print(ip)
```

### Leitura de Arquivos

```python
with open("log.txt") as arquivo:
    for linha in arquivo:
        print(linha)
```

### Regex

```python
import re

ips = re.findall(r'\d+\.\d+\.\d+\.\d+', linha)
```

---

## Script Exemplo

Arquivo:

analisar_logs.py

### Objetivo

Extrair IPs únicos de um arquivo de log.

---

## Aplicações em SOC

Python pode ser utilizado para:

- Análise de logs
- Extração de IOCs
- Enriquecimento de IPs
- Consultas ao VirusTotal
- Consultas ao AbuseIPDB
- Geração de relatórios
- Automação de triagem

---

## Conclusão

Python é uma das linguagens mais utilizadas em Cyber Security devido à simplicidade e capacidade de automação.