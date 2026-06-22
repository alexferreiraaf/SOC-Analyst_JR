# SIEM Interview Notes

## O que é SIEM?

SIEM significa:

Security Information and Event Management

Funções:

* Coleta de logs
* Normalização
* Correlação
* Alertas
* Investigação

---

## Ferramentas Populares

* Splunk
* Wazuh
* Elastic Stack

---

## Queries Importantes

### Buscar login falho

```spl
index=auth_logs "Failed password"
```

### Contar por usuário

```spl
index=auth_logs | stats count by user
```

### Contar por IP

```spl
index=auth_logs | stats count by src_ip
```

### Contar remetentes de e-mail

```spl
index=email_logs | stats count by sender
```

### Contar URLs

```spl
index=email_logs | stats count by url
```

---

## Correlação de Eventos

Correlação é o processo de relacionar eventos diferentes para identificar comportamentos suspeitos.

Exemplo:

* Muitas falhas de login
* Seguidas por login bem sucedido

Possível comprometimento.

---

## Perguntas Frequentes

### O que é SIEM?

Ferramenta que centraliza logs e auxilia na detecção e investigação de incidentes.

### O que é correlação?

Relacionar eventos para identificar padrões de ataque.

### Como detectar phishing?

Analisando remetentes, URLs, assuntos e volume de mensagens.

### Recebi alerta de login suspeito. O que fazer?

1. Verificar IP
2. Verificar usuário
3. Verificar horário
4. Consultar histórico
5. Determinar impacto
