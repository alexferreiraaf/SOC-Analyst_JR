
# Dia 78 — Introdução à Análise de Logs de Autenticação (Linux)

## 🎯 Objetivo do Dia
Aprender a ler e interpretar logs de autenticação Linux para identificar acessos legítimos, falhas de login e possíveis ataques de força bruta em SSH, com mentalidade de SOC Analyst Júnior.

---

## 📘 Conceitos Fundamentais

### O que são logs de autenticação?
Registros que mostram tentativas de acesso ao sistema, incluindo:
- Logins SSH
- Falhas de autenticação
- Uso de sudo
- Tentativas com usuários inexistentes

São uma das **principais fontes de detecção de ataques** em ambientes Linux.

---

## 📂 Arquivos Importantes

- **Debian / Ubuntu:** `/var/log/auth.log`
- **RHEL / CentOS:** `/var/log/secure`

Saber onde procurar é essencial para investigação rápida em SOC.

---

## 🔍 Eventos Comuns

### Login bem-sucedido
Accepted password for user from IP ssh2

Indica acesso legítimo, mas deve ser validado por horário e origem.

### Login falho
Failed password for user from IP ssh2

Múltiplas ocorrências seguidas indicam possível brute force.

### Usuário inexistente
Failed password for invalid user admin from IP

Indicador forte de ataque automatizado.

### Uso de sudo
Mostra elevação de privilégio e é usado para auditoria e detecção de abuso.

---

## 🚨 Relação com Brute Force

Ataques de brute force apresentam:
- Muitas falhas de login
- Mesmo IP repetidamente
- Curto intervalo de tempo
- Usuários comuns (root, admin)

SOC analisa **padrões**, não eventos isolados.

---

## 🧪 Prática SOC

Ferramentas comuns:
- `cat` e `less` para leitura
- `grep` para filtrar falhas ou sucessos
- `awk` para extrair IPs e usuários

Exemplo:
grep "Failed password" /var/log/auth.log

---

## 🧠 Mentalidade SOC

Perguntas-chave:
- O IP se repete?
- O horário faz sentido?
- Houve sucesso após falhas?
- É erro humano ou ataque?

Decisões:
- Erro isolado → monitorar
- Ataque automatizado → escalar incidente

---

## 🏁 Conclusão

Ao final do Dia 78, você:
- Lê logs Linux com segurança
- Identifica padrões suspeitos
- Reconhece brute force inicial
- Age como SOC Analyst desde a triagem

> “Quem sabe ler log, sabe investigar.”
