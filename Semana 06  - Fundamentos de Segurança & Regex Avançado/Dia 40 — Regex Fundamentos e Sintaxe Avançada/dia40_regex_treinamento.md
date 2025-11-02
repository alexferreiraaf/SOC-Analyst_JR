# 🧩 **Resumo — Dia 40: Regex — Fundamentos e Sintaxe Avançada**

## 🎯 **Objetivo**
Aprender a criar e aplicar **expressões regulares (regex)** para extrair padrões úteis em logs, como IPs, e-mails, timestamps e falhas de login.  
O foco foi dominar a sintaxe, testar padrões em ferramentas (regex101, Python, PowerShell) e entender boas práticas de eficiência e precisão.

---

## 🧠 **Principais Conceitos**

- `.` → qualquer caractere  
- `\d`, `\w`, `\s` → dígito, caractere, espaço  
- Quantificadores: `+`, `*`, `?`, `{n,m}`  
- Grupos: `()`, `(?:...)`  
- Âncoras: `^` (início), `$` (fim)  
- Lookaround:  
  - `(?=...)` → seguido por  
  - `(?!...)` → não seguido por  
  - `(?<=...)` → precedido por  
  - `(?<!...)` → não precedido por  

---

## ⚙️ **Patterns úteis**

| Tipo | Regex |
|------|--------|
| IPv4 simples | `\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b` |
| IPv4 rigoroso | `\b(?:(?:25[0-5]|2[0-4]\d|1?\d{1,2})\.){3}(?:25[0-5]|2[0-4]\d|1?\d{1,2})\b` |
| E-mail | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` |
| URL suspeita | `https?:\/\/[^\s"]+\.(?:xyz|ru|top|info)(?:\/[^\s"]*)?` |
| Hash MD5 | `\b[a-fA-F0-9]{32}\b` |
| SSH Log | `^(\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2})\s+([\w\-.]+)\s+([\w\-/]+):\s+(.*)$` |

---

## 🧩 **Scripts usados**

### 🐍 Python — `log_parser.py`
Extrai IPs e usuários com falhas de login e gera `logins_falhos.csv`.

### 💻 PowerShell — `parse_failed.ps1`
Busca por “Failed password” e exporta resultados para CSV, extraindo IP e usuário.

---

## 🧪 **Exercícios realizados**

1. **Teste básico:** extrair e contar IPs de um arquivo `sample.txt`.  
2. **Contagem de falhas:** rodar `log_parser.py` e verificar top IPs e usuários.  
3. **Lookaround avançado:** correlacionar logs de falha e sucesso em até 5 min.  
4. **Prevenção de falsos positivos:** ignorar linhas sem IP e evitar `0.0.0.0`.  
5. **Performance:** comparar `re.search` vs. `re.compile` e medir tempos com `timeit`.

---

## ⚠️ **Armadilhas e Boas Práticas**

- Evitar **greedy matching** (`.*`) → usar `.*?`  
- Escapar caracteres com `re.escape()`  
- Testar com **casos negativos** para evitar falsos positivos  
- Usar **\b boundaries** em IPs e hashes  
- Compilar regex com `re.compile()` para ganho de performance  

---

## 🗂️ **Arquivos produzidos**

- `dia40_regex_treinamento.md` → resumo da aula  
- `auth_sample.log` → dataset de teste  
- `log_parser.py` e `parse_failed.ps1` → scripts  
- `regex_tests.txt` → resultados dos testes  
- `performance_report.md` → comparação de desempenho  

---

## 🧠 **Aprendizado-chave**
Regex é uma das ferramentas mais poderosas para analistas SOC e DFIR.  
Dominar padrões e boas práticas permite **extrair IOCs rapidamente**, reduzir falsos positivos e automatizar correlações em logs de grande volume.

---
