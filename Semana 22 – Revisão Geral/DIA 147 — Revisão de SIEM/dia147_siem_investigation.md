# DIA 147 — SIEM Investigation

## Ferramenta

Splunk

---

## O que é um SIEM

SIEM (Security Information and Event Management) é uma plataforma que centraliza logs de diferentes sistemas, permitindo correlação de eventos, criação de alertas e investigação de incidentes.

Principais funções:

- Coleta de logs
- Normalização
- Correlação
- Alertas
- Investigação

---

## Queries Úteis

### Buscar todos os logs

```spl
index=auth_logs
```

### Buscar logins falhos

```spl
index=auth_logs "Failed password"
```

### Contar eventos por usuário

```spl
index=auth_logs | stats count by user
```

### Contar eventos por IP

```spl
index=auth_logs | stats count by src_ip
```

### Ordenar por quantidade

```spl
index=auth_logs
| stats count by src_ip
| sort - count
```

### Analisar e-mails

```spl
index=email_logs
```

### Contar remetentes

```spl
index=email_logs | stats count by sender
```

### Contar URLs

```spl
index=email_logs | stats count by url
```

---

## Indicadores de Ataque

### Brute Force

- Muitas tentativas de login
- Mesmo IP repetido
- Contas privilegiadas

### Phishing

- Mesmo remetente para vários usuários
- Links suspeitos
- Domínios semelhantes aos legítimos

### Atividade Suspeita

- Acessos fora do horário
- IPs externos desconhecidos
- Volume incomum de eventos

---

## Conclusão

As consultas SPL permitem identificar rapidamente padrões de ataque como brute force, phishing e comportamento anômalo.