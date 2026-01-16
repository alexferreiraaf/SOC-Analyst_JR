# Prática 3 — Filtro Simples no Discover (Elastic / Kibana)

## Objetivo da prática
Avaliar se é possível **isolar eventos relevantes** usando filtros simples no Kibana Discover, simulando a análise de um **incidente real**.

---

## 1. Filtro por IP específico

### Observação baseada no arquivo analisado
No conjunto de eventos fornecido (**Prática 1 — Navegando no Kibana Discover.csv**):

- Não existe o campo `source.ip`
- Não existem campos equivalentes como:
  - `client.ip`
  - `destination.ip`
  - `network.forwarded_ip`

### Interpretação SOC
Isso indica que os eventos **não são logs de tráfego de rede**, firewall ou proxy.

**Conclusão:**
- ❌ Não é possível filtrar por IP de rede neste dataset
- ✔ Essa limitação já indica o **tipo de incidente analisado** (email/endpoint)

---

## 2. Filtro por usuário

### Campo disponível no arquivo
Embora o campo `user.name` não exista explicitamente, há um **campo funcional equivalente**:

```
sender
```

Exemplo real:
```
sender: yani.zubair@tryhatme.com
```

### Filtro no Kibana Discover (KQL)
```kql
sender : "yani.zubair@tryhatme.com"
```

### Resultado esperado
- Isola todos os eventos associados a esse usuário
- Permite identificar padrões como:
  - envio de anexos
  - comportamento fora do horário
  - repetição de ações

**Conclusão SOC:**
✔ É possível isolar completamente a atividade de um usuário específico.

---

## 3. Ajuste do intervalo de tempo

### Campo utilizado
```
timestamp
```

Exemplo:
```
Jan 17, 2026 @ 02:47:10.304
```

### Ação no Discover
- Utilizar o **Time Picker**
- Exemplos:
  - Last 15 minutes
  - Last 1 hour
  - Intervalo customizado (02:30 → 03:00)

### Importância SOC
- Permite focar apenas no período suspeito
- Remove ruído antes e depois do evento

---

## Pergunta-chave SOC

> “Se isso fosse um incidente, eu conseguiria isolar os eventos?”

### Resposta baseada no arquivo
**Sim, parcialmente.**

- ✔ Isolamento por usuário (sender)
- ✔ Isolamento por intervalo de tempo
- ❌ Isolamento por IP não aplicável (não é tráfego de rede)

### Conclusão SOC
Mesmo sem IP, é possível conduzir uma **investigação inicial eficaz** para incidentes de email interno ou endpoint, utilizando filtros por usuário e tempo.


