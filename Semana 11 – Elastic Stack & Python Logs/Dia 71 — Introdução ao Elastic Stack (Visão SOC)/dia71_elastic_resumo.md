# Dia 71 — Introdução ao Elastic Stack (Visão SOC)

## Objetivo do Dia
Compreender como o **Elastic Stack (ELK)** funciona em um **ambiente de SOC**, entendendo o fluxo real de logs, o papel de cada componente e como eventos se transformam em evidências de segurança.

Ao final do estudo, o analista deve ser capaz de:
- Explicar o ELK em entrevistas
- Navegar no Kibana com segurança
- Interpretar eventos como indícios de incidentes

---

## 1. O que é o Elastic Stack (ELK)

O Elastic Stack é um conjunto de ferramentas usado para:
- Coleta de logs
- Normalização e enriquecimento de dados
- Armazenamento e busca rápida
- Investigação de incidentes
- Visualização e dashboards SOC

### Fluxo real de logs (visão SOC):

Servidor / Firewall / Aplicação  
↓  
Logstash  
↓  
Elasticsearch  
↓  
Kibana  

---

## 2. Componentes do Elastic Stack

### Elasticsearch
- Banco de dados orientado a documentos (JSON)
- Permite buscas rápidas e correlação de eventos
- Base da investigação SOC

Exemplos de perguntas SOC:
- Quais IPs falharam login nas últimas 24h?
- Qual usuário acessou fora do horário padrão?

---

### Logstash
- Recebe logs brutos
- Extrai campos
- Normaliza dados para análise

Exemplo de transformação:
- Texto bruto → campos estruturados como `source.ip`, `user.name`, `http.response.status_code`

SOC trabalha com **campos**, não com texto cru.

---

### Kibana
- Interface visual do Elastic
- Usado para:
  - Investigação
  - Dashboards
  - Análise temporal
  - Monitoramento de incidentes

SOC usa Kibana para **consciência situacional**, não apenas para busca.

---

## 3. Elastic Stack vs Splunk (Visão Entrevista)

| Critério | Elastic Stack | Splunk |
|--------|---------------|--------|
| Licença | Open source (base) | Pago |
| Interface | Kibana | Splunk Web |
| Linguagem | KQL / Lucene | SPL |
| Uso em SOC | Muito comum | Muito comum |

**Ponto-chave de entrevista:**
> Os conceitos de SIEM são os mesmos, o que muda é a ferramenta.

---

## 4. Conceitos Essenciais para SOC

### Index
- Conjunto de dados relacionados
- Ex: logs-auth, logs-web, logs-windows

### Document
- Evento individual
- Ex: um login, uma requisição, um erro

### Field
Campos estruturados usados em investigação:
- `@timestamp`
- `source.ip`
- `user.name`
- `event.action`

### Timestamp
- Base de qualquer investigação
- Permite correlação, linha do tempo e detecção de anomalias

---

## 5. Mentalidade SOC no Kibana

Ao analisar eventos no Discover, o analista deve sempre se perguntar:
- Os eventos são recentes?
- Isso representa login, erro ou tráfego normal?
- Existe repetição ou padrão?
- Consigo isolar esses eventos se virar um incidente?

---

## Conclusão

O Elastic Stack não é apenas uma ferramenta, mas um **método de investigação**.

Ao dominar:
- Fluxo de logs
- Campos SOC
- Análise temporal

Você desenvolve a base necessária para atuar como **SOC Analyst Júnior** em ambientes reais.

> “SIEM não é ferramenta. É método de investigação.”
