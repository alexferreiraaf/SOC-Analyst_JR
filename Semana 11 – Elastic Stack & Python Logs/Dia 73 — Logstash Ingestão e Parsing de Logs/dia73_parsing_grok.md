# Dia 73 — Parsing com GROK (Visão SOC)

## Objetivo
Demonstrar como GROK (regex SOC-friendly) é usado para transformar logs de autenticação em eventos estruturados, prontos para detecção e alertas.

---

## Exemplo 1 — Falha de login

### Log bruto
Failedpasswordforadminfrom192.168.1.50 port443 ssh2

### GROK utilizado
Failedpasswordfor%{WORD:user.name}from%{IP:source.ip}

### Campos extraídos
- user.name = admin
- source.ip = 192.168.1.50
- event.action = login_failed

---

## Exemplo 2 — Login bem-sucedido

### Log bruto
Accepted password for root from10.10.10.8 port22

### GROK utilizado
Accepted password for %{WORD:user.name} from%{IP:source.ip}

### Campos extraídos
- user.name = root
- source.ip = 10.10.10.8
- event.action = login_success

---

## Insight SOC
GROK bem construído é a base de alertas confiáveis. Regex frágil gera falso negativo.
