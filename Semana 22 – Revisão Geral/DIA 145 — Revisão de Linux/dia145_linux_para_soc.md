# DIA 145 — Linux para SOC

## Objetivo

Revisar comandos Linux essenciais para investigação de incidentes.

---

# Diretórios Importantes

/var/log

/etc

/home

/bin

---

# Logs Importantes

## auth.log

Contém:

* Logins SSH
* Falhas de autenticação
* Uso de sudo

---

## syslog

Eventos gerais do sistema.

---

## kern.log

Eventos do Kernel.

---

# Comandos Essenciais

## Navegação

pwd

ls

ls -la

cd

---

## Arquivos

cat

less

head

tail

tail -f

---

## Busca

grep

Exemplo:

grep "Failed password" /var/log/auth.log

---

## Processos

ps aux

top

---

## Usuários

who

---

# Investigação de Brute Force

Passo 1:

grep "Failed password" /var/log/auth.log

Passo 2:

Identificar IP de origem

Passo 3:

Verificar sucesso

grep "Accepted password" /var/log/auth.log

Passo 4:

Verificar usuários conectados

who

Passo 5:

Verificar processos

ps aux

---

# Indicadores de Ataque

* Muitas falhas SSH
* Logins externos
* Processos desconhecidos
* Uso elevado de CPU
* Usuários inesperados conectados

---

# Resumo

Grande parte das investigações em Linux começa pela análise de logs, usuários ativos, processos e conexões de rede.
