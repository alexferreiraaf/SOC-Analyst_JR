# 🧠 Dia 28 — Mini-projeto: Extrator de IPs do Log SSH

⏱️ Duração estimada: ~2h30

---

## 🎯 Objetivo do dia

Criar um script em **Bash** que analise logs do sistema (como `/var/log/auth.log`) e gere um **relatório com os IPs** que tentaram acessar o servidor via SSH.  
Esse projeto é uma introdução à **análise de logs e automação de segurança**, fundamental para profissionais de **SOC e SysAdmin**.

---

## 🧩 Etapa 1 — Preparação (30 min)

### 1.1 — Criar log de exemplo

Caso você não tenha acesso ao log real (`/var/log/auth.log`), crie um arquivo simulado:

```bash
nano auth_sample.log
```

Cole o conteúdo abaixo:

```
Oct  8 12:11:22 server sshd[1288]: Failed password for root from 192.168.0.45 port 55522 ssh2
Oct  8 12:11:25 server sshd[1288]: Failed password for invalid user admin from 203.0.113.10 port 55221 ssh2
Oct  8 12:11:30 server sshd[1288]: Failed password for root from 192.168.0.45 port 55523 ssh2
Oct  8 12:11:35 server sshd[1288]: Accepted password for user1 from 10.0.0.25 port 55801 ssh2
Oct  8 12:11:42 server sshd[1288]: Failed password for user test from 203.0.113.10 port 55990 ssh2
Oct  8 12:11:50 server sshd[1288]: Failed password for root from 198.51.100.88 port 56001 ssh2
```

💡 Dica: você pode adicionar mais linhas manualmente ou com `echo`:
```bash
echo "Oct 8 12:11:22 server sshd[1288]: Failed password for root from 203.0.113.11 port 55100 ssh2" >> auth_sample.log
```

---

## ⚙️ Etapa 2 — Criando o script `extrai_ips.sh` (70 min)

Crie e edite o arquivo:

```bash
nano extrai_ips.sh
```

Cole o conteúdo completo:

```bash
#!/bin/bash

# Verifica se o arquivo de log existe
if [ ! -f auth_sample.log ]; then
  echo "Arquivo auth_sample.log não encontrado!"
  exit 1
fi

echo "Extraindo IPs de tentativas de login falhas..."

# Extrai IPs, conta quantas vezes aparecem e ordena do maior para o menor
grep "Failed password" auth_sample.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr > relatorio_ips.txt

echo "Relatório gerado em relatorio_ips.txt"
echo
cat relatorio_ips.txt
```

Dê permissão de execução:

```bash
chmod +x extrai_ips.sh
```

---

## 🧩 Etapa 3 — Executando o script (40 min)

Execute:

```bash
./extrai_ips.sh
```

### ✅ Saída esperada:
```
Extraindo IPs de tentativas de login falhas...
Relatório gerado em relatorio_ips.txt

   2 192.168.0.45
   2 203.0.113.10
   1 198.51.100.88
```

Verifique o arquivo de saída:

```bash
cat relatorio_ips.txt
```

---

## 🔍 Entendendo o código passo a passo

| Linha | Comando | Explicação |
|:------|:---------|:-----------|
| `grep "Failed password"` | Filtra apenas linhas com falhas de senha no log. |
| `awk '{print $(NF-3)}'` | Extrai o IP (campo 3 antes do fim da linha). |
| `sort` | Ordena os IPs antes de agrupar. |
| `uniq -c` | Agrupa IPs iguais e mostra quantas vezes aparecem. |
| `sort -nr` | Ordena de forma numérica e decrescente. |
| `> relatorio_ips.txt` | Salva o resultado no arquivo de saída. |

---

## 🧩 Etapa 4 — Testando com logs reais

Se quiser testar com o log real do sistema Linux:

```bash
sudo ./extrai_ips.sh /var/log/auth.log
```

Para isso, altere o script para aceitar um argumento:

```bash
#!/bin/bash
arquivo=${1:-auth_sample.log}

if [ ! -f "$arquivo" ]; then
  echo "Arquivo $arquivo não encontrado!"
  exit 1
fi

grep "Failed password" "$arquivo" | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr > relatorio_ips.txt
echo "Relatório gerado com base no arquivo $arquivo"
```

---

## 🧩 Etapa 5 — Exercícios práticos

### 🧠 1. Contar total de falhas
```bash
grep -c "Failed password" auth_sample.log
```

### 📊 2. Mostrar apenas os 5 IPs mais reincidentes
```bash
grep "Failed password" auth_sample.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head -n 5
```

### 🧱 3. Mostrar apenas IPs únicos
```bash
grep "Failed password" auth_sample.log | awk '{print $(NF-3)}' | sort -u
```

### 🚫 4. Excluir IPs internos (192.168.x.x)
```bash
grep "Failed password" auth_sample.log | awk '{print $(NF-3)}' | grep -v "^192\.168" | sort | uniq -c | sort -nr
```

### 📁 5. Exportar resultado em CSV
```bash
awk '{print $2 "," $1}' relatorio_ips.txt > relatorio_ips.csv
```

---

## 📦 Entregáveis do dia

| Arquivo | Descrição |
|:--------:|:-----------|
| `extrai_ips.sh` | Script principal. |
| `auth_sample.log` | Log de exemplo (ou real). |
| `relatorio_ips.txt` | Relatório gerado pelo script. |
| `dia28_resumo.md` | Resumo completo do aprendizado. |
| `README_semana4.md` | Resumo final da semana. |

---

## 🧭 Conclusão do dia

Hoje você:
- Entendeu o funcionamento dos logs SSH.
- Usou `grep`, `awk`, `sort`, `uniq` e `cat` juntos.
- Criou um **script shell automatizado** para gerar relatórios de IPs suspeitos.
- Deu o primeiro passo para **análise automatizada de logs e segurança**.

🎯 **Próximo passo:** expandir o script para bloquear IPs com muitas tentativas ou gerar relatórios em CSV/HTML.
