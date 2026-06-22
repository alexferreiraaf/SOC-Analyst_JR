# Incident Report — SSH Brute Force Attempt

## Descrição

Múltiplas tentativas de login SSH foram detectadas a partir do IP externo 185.223.89.44.

O comportamento observado é compatível com um ataque de brute force direcionado a contas privilegiadas.

---

## Impacto

Tentativas repetidas de autenticação podem resultar em comprometimento do servidor caso credenciais válidas sejam descobertas.

Contas privilegiadas como root e admin foram alvo das tentativas.

---

## Investigação

### Identificação do IP

IP analisado:

185.223.89.44

Classificação:

- Externo
- Potencial origem maliciosa

---

### Análise dos Logs Linux

Comando utilizado:

```bash
grep "Failed password" /var/log/auth.log
```

Eventos encontrados:

```text
Failed password for root from 185.223.89.44
Failed password for root from 185.223.89.44
Failed password for admin from 185.223.89.44
```

---

### Contagem de Eventos

```bash
grep "185.223.89.44" /var/log/auth.log | wc -l
```

Resultado:

```text
75 tentativas
```

---

### Investigação no SIEM

Consulta:

```spl
index=auth_logs 185.223.89.44
```

Agrupamento por usuário:

```spl
index=auth_logs 185.223.89.44
| stats count by user
```

Resultado:

| Usuário | Tentativas |
|----------|----------|
| root | 60 |
| admin | 15 |

---

### Automação Utilizada

Script Python utilizado para contabilizar ocorrências do IP suspeito.

Objetivo:

- Identificar quantidade de tentativas
- Facilitar triagem inicial

---

## Conclusão

Foi identificado um padrão consistente com ataque de brute force SSH.

O IP externo realizou diversas tentativas de autenticação contra contas privilegiadas.

Não foram observados logins bem-sucedidos durante a investigação.

Classificação:

ALTO RISCO

---

## Recomendações

- Bloquear IP atacante no firewall
- Implementar Fail2Ban
- Utilizar autenticação por chave SSH
- Desabilitar login direto do usuário root
- Monitorar novos eventos relacionados
- Configurar alertas automáticos no SIEM