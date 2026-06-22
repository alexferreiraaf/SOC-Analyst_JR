# Cybersecurity Knowledge Base

## Networking

### Portas Importantes

| Porta | Serviço |
|---------|---------|
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3389 | RDP |

### Comandos

```bash
ping
nslookup
netstat
ss
```

---

## Linux

### Logs Importantes

```bash
/var/log/auth.log
/var/log/syslog
```

### Comandos Úteis

```bash
ls
grep
ps aux
who
top
tail -f
journalctl
netstat
```

---

## Windows

### Event IDs

| Event ID | Descrição |
|-----------|-----------|
| 4624 | Login com sucesso |
| 4625 | Login falhou |
| 4672 | Privilégios especiais |
| 4688 | Processo criado |

---

## SIEM

### Splunk

Buscar login falho:

```spl
index=auth_logs "Failed password"
```

Contar por IP:

```spl
index=auth_logs | stats count by src_ip
```

Contar remetentes:

```spl
index=email_logs | stats count by sender
```

---

## Python Automation

### analisar_logs.py

Objetivo:

- Extrair IPs
- Contar ocorrências
- Identificar IPs repetidos

---

## Incident Response

### Fluxo Básico

1. Detectar
2. Investigar
3. Correlacionar
4. Classificar
5. Escalonar
6. Documentar

---

## Conclusão

Esta base de conhecimento centraliza conceitos, comandos, scripts e exemplos utilizados em investigações de segurança.