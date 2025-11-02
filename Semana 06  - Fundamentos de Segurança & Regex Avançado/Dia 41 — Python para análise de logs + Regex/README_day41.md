# 🧩 **Resumo — Dia 41: Python para Análise de Logs + Regex**

## 🎯 **Objetivo**
Aplicar **expressões regulares (Regex)** em **Python** para detectar padrões de ataque em logs de autenticação (como tentativas de login SSH), automatizando a geração de relatórios e identificando IPs suspeitos.

---

## 🧠 **Conceitos-Chave**

- **Regex + Python** = combinação poderosa para análise de logs.
- Extração automatizada de **usuários**, **IPs** e **timestamps**.
- Identificação de **comportamentos suspeitos** (múltiplas falhas seguidas).
- Geração de **CSVs** para análise em Excel, PowerBI ou SIEM.

---

## ⚙️ **Script principal:** `analisador_log_regex.py`

- Lê `auth_sample.log`
- Extrai eventos com `"Failed password"`
- Gera dois arquivos:
  - `logins_falhos.csv` → todos os eventos parseados
  - `logins_suspeitos.csv` → IPs com tentativas acima do limite configurado

### 🔧 Configurações principais:
| Variável | Função | Padrão |
|-----------|---------|--------|
| `GLOBAL_THRESHOLD` | Máximo de tentativas antes de marcar IP como suspeito | 2 |
| `WINDOW_THRESHOLD` | Tentativas dentro de uma janela de tempo | 5 |
| `WINDOW_MINUTES` | Tamanho da janela em minutos | 5 |

---

## 🧩 **Regex usados**

| Padrão | Descrição |
|--------|------------|
| `(?P<ts>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})` | Captura timestamp |
| `Failed\s+password\s+for\s+(?:invalid\s+user\s+)?(?P<user>\S+)\s+from\s+(?P<ip>(?:\d{1,3}\.){3}\d{1,3})` | Captura usuário e IP de falha SSH |

---

## 🧪 **Exemplo de execução**

### Arquivo de entrada: `auth_sample.log`
2025-10-20 08:15:23 host1 sshd[1234]: Failed password for invalid user admin from 185.222.123.45 port 514 ssh2
2025-10-20 08:15:27 host1 sshd[1234]: Failed password for invalid user admin from 185.222.123.45 port 514 ssh2
2025-10-20 08:15:30 host1 sshd[1234]: Failed password for invalid user root from 203.0.113.55 port 3456 ssh2
2025-10-20 08:23:11 host3 sshd[5678]: Failed password for user2 from 10.0.0.5 port 2222 ssh2

shell
Copiar código

### Saída no console:
[+] 5 eventos parseados. Salvo em: logins_falhos.csv
[+] 1 IPs suspeitos detectados. Salvo em: logins_suspeitos.csv

Top 10 IPs por tentativas:
185.222.123.45 -> 3
203.0.113.55 -> 1
10.0.0.5 -> 1

yaml
Copiar código

---

## 📊 **Arquivos gerados**

| Arquivo | Conteúdo | Uso |
|----------|-----------|-----|
| `logins_falhos.csv` | Todos os eventos com time, user, ip, raw | Base de análise |
| `logins_suspeitos.csv` | IPs com tentativas acima do limite | Relatório de alerta |

---

## 🧠 **Exercícios realizados**

1. **Ajustar thresholds** → testar diferentes valores de `GLOBAL_THRESHOLD`.  
2. **Janela temporal** → alterar `WINDOW_MINUTES` e `WINDOW_THRESHOLD`.  
3. **Parsing expandido** → adaptar regex para outros tipos de log.  
4. **Correlação de sucesso** → incluir logs com `Accepted password`.  
5. **Export JSON** → gerar relatório `report.json`.  
6. **Visualização** → gráficos no Excel/PowerBI.

---

## ⚙️ **Extensões sugeridas (nível intermediário)**

- Uso de **Pandas** para análise temporal e gráficos.  
- Enriquecimento com APIs externas (ex: AbuseIPDB, VirusTotal).  
- Envio de alertas automáticos via e-mail ou Slack.  
- Conversão para **regras Sigma**, **KQL** ou **SPL** para uso em SIEM.

---

## 🧾 **Entregáveis do Dia 41**

| Arquivo | Descrição |
|----------|------------|
| `analisador_log_regex.py` | Script principal |
| `auth_sample.log` | Dataset de exemplo |
| `logins_falhos.csv` | Eventos parseados |
| `logins_suspeitos.csv` | IPs suspeitos |
| `README_day41.md` | Instruções e resumo |

---

## 💡 **Conclusão**

Neste exercício, aprendi a **automatizar a detecção de padrões de ataque** em logs com **Python e Regex**, gerando relatórios claros e acionáveis.  
A técnica é base para **análises de segurança em SOCs**, permitindo identificar rapidamente **ataques de força bruta** e **tentativas de acesso indevido**.

---