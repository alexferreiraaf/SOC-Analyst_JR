# 📘 Mini-projeto – Contador de IPs em Log

## 🎯 Objetivo
Criar um script em Python que leia um arquivo de log, identifique os IPs contidos nele e conte quantas vezes cada IP aparece.
Esse exercício ajuda a praticar **regex**, **manipulação de arquivos** e **uso de coleções (Counter)**.

---

## ⚙️ Como o script funciona
1. O script abre o arquivo `log_exemplo.txt` e lê todo o conteúdo.
2. Utiliza **expressão regular (regex)** para encontrar todos os endereços IPv4 no texto.
3. Conta as ocorrências de cada IP usando `collections.Counter`.
4. Gera um relatório chamado `relatorio_ips.txt`, listando os IPs encontrados e suas quantidades.
5. Exibe no terminal o número total de IPs únicos encontrados.

---

## 📜 Exemplo de log (`log_exemplo.txt`)
```txt
192.168.0.1 - acesso permitido
10.0.0.5 - acesso negado
192.168.0.1 - acesso permitido
8.8.8.8 - consulta DNS
8.8.8.8 - consulta DNS

