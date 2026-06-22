# DIA 146 — Windows para SOC

## Objetivo

Revisar logs de segurança e Event IDs importantes para investigação.

---

# Logs do Windows

Local:

Event Viewer

Windows Logs

---

# Categorias

## Security

Autenticação e acessos

## System

Eventos do sistema

## Application

Aplicações

## Setup

Instalações

## Forwarded Events

Logs centralizados

---

# Event IDs Importantes

| Event ID | Significado                 |
| -------- | --------------------------- |
| 4624     | Login com sucesso           |
| 4625     | Login falhou                |
| 4634     | Logout                      |
| 4672     | Privilégios administrativos |
| 4688     | Processo criado             |

---

# Investigações Comuns

## Brute Force

Procurar:

Event ID 4625

Perguntas:

* Quantas tentativas?
* Qual usuário?
* Qual origem?

---

## Login Bem-Sucedido

Procurar:

Event ID 4624

Verificar:

* Horário
* Usuário
* Host

---

## Privilégios Administrativos

Event ID:

4672

Verificar:

* Quem recebeu privilégio
* Qual contexto

---

## Processos Suspeitos

Event ID:

4688

Analisar:

* Nome do processo
* Caminho
* Usuário executante

---

# Ferramenta Principal

Event Viewer

Executar:

eventvwr.msc

---

# Indicadores de Ataque

* Muitos eventos 4625
* Logins fora do horário
* Uso inesperado de privilégios
* Execução de processos suspeitos

---

# Resumo

Os logs de segurança do Windows são fundamentais para detectar brute force, abuso de privilégios e execução de atividades maliciosas.
