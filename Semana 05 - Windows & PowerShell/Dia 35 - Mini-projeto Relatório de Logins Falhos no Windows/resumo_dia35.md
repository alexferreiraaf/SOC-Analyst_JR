# 🧾 Resumo — Dia 35: Mini-projeto de Logins Falhos no Windows

## 🎯 Objetivo
Aprender a **extrair, analisar e automatizar relatórios de logons falhos (Event ID 4625)** no log de Segurança do Windows. O foco foi entender padrões de tentativas de acesso indevido e como detectar possíveis ataques.

---

## 🧠 Tópicos estudados

### 1. Evento 4625 — Logon Falho
- Ocorre quando há falha de autenticação no sistema.
- Campos importantes:
  - **Account Name:** usuário que tentou o logon
  - **Source Network Address:** IP de origem
  - **Logon Type:** tipo de logon (2 = local, 3 = rede, 10 = RDP)
  - **Failure Reason:** motivo da falha (senha incorreta, conta inexistente etc.)

---

### 2. Script principal: `logins_falhos.ps1`
- Extrai os últimos 1000 eventos 4625.
- Analisa e exporta para `logins_falhos.csv` com campos:
  - Data/Hora, Usuário, IP, Tipo de Logon e Mensagem.
- Inclui parsing de texto com **regex** para capturar informações do log.

---

### 3. Análises e consultas em PowerShell
- **Contar tentativas por IP:**
  ```powershell
  Import-Csv .\logins_falhos.csv | Group-Object IP | Sort-Object Count -Descending
  ```
- **Filtrar tentativas de um usuário específico.**
- **Detectar IPs com mais de 5 ou 10 falhas** e gerar relatório `suspeitos.csv`.

---

### 4. Interpretação dos resultados
| Sintoma | Interpretação | Ação |
| --- | --- | --- |
| IP com várias tentativas | Brute force | Bloquear e investigar |
| Vários usuários de um mesmo IP | Ataque automatizado | Criar regra de alerta |
| Logons tipo 10 (RDP) fora de hora | Tentativa remota suspeita | Monitorar e alertar |
| Falhas seguidas de sucesso | Possível credencial comprometida | Escalar incidente |

---

### 5. Boas práticas
- Sempre fazer **backup dos logs** antes da análise.
- Testar scripts em **ambientes de laboratório**.
- Documentar achados e manter **versionamento com Git**.
- Automatizar execução diária via **Agendador de Tarefas**.

---

### 6. Desafio final
Criar um **painel no Power BI ou Excel** mostrando:
- Total de falhas por hora
- Top 5 contas atacadas
- Top 5 IPs suspeitos
- Tendência diária de tentativas

---

## 📦 Entregáveis do dia
- `logins_falhos.ps1`
- `logins_falhos.csv`
- `suspeitos.csv`
- `analise_logons.md`
- `README_logins.md`

---

> 🔐 **Resumo:** O dia 35 consolidou o uso prático do PowerShell em segurança, com foco em detecção de ataques de logon e automação de relatórios SOC.
