# Dia 89 — Eventos Críticos do Windows para SOC

## Objetivo
Identificar, correlacionar e interpretar eventos críticos do Windows durante investigações de segurança usando PowerShell.

---

## 🔐 Eventos de Autenticação

### Event ID 4625 — Logon Falho
Indica tentativas de login malsucedidas.
Usado para detectar:
- brute force
- enumeração de usuários
- erros repetidos de autenticação

Campos importantes:
- Usuário
- IP de origem
- Horário

---

### Event ID 4624 — Logon Bem-Sucedido
Indica autenticação válida no sistema.

Atenção especial para:
- LogonType 10 (RDP)
- horários fora do padrão
- IP externo

---

### Event ID 4648 — Credenciais Explícitas
Indica uso de credenciais fornecidas manualmente.
Possível uso de:
- runas
- ferramentas pós-exploração

---

## 🧠 Eventos de Execução

### Event ID 4688 — Criação de Processo
Mostra que um processo foi iniciado.

Importante para identificar:
- execução de PowerShell
- cmd.exe
- ferramentas administrativas suspeitas

---

## 👤 Eventos de Privilégio e Contas

### Event ID 4672 — Privilégios Especiais
Indica que o usuário recebeu privilégios administrativos.

Usuário inesperado = alerta grave.

---

## 🔗 Correlação Clássica de Incidente

4625 → 4625 → 4624 → 4688 → 4672

Indica:
- ataque de força bruta
- acesso obtido
- execução de comandos
- elevação de privilégio
