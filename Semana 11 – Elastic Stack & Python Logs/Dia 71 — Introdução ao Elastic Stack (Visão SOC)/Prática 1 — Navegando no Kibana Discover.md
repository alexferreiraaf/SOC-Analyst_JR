## 🧪 Prática 1 — Análise Inicial SOC (Elastic / Kibana)
### ❓ Pergunta 1: “Esses eventos são recentes?”
### 🧠 Como um SOC responde isso
No Elastic, a resposta vem principalmente do campo:
- @timestamp → indica quando o evento ocorreu
## 📌 O que analisar no arquivo
Ao observar o CSV do Kibana Discover, note que:
- Os eventos possuem timestamp completo (data + hora)
- Eles estão concentrados em um intervalo específico de tempo
- Não são logs históricos antigos (anos atrás)

### ✅ Conclusão SOC

> Sim, os eventos são recentes, pois possuem timestamps contínuos e próximos entre si, típicos de dados > coletados em tempo real ou em laboratório ativo.

📌 Em ambiente real, isso indicaria:
- Sistema ligado
- Coleta funcionando
- Dados relevantes para investigação atual

### ❓ Pergunta 2: “Que tipo de dado isso representa?”
### 🧠 Leitura SOC (o mais importante)
Esses eventos representam logs normalizados no Elastic Stack, muito provavelmente provenientes de:
- Endpoint / Sistema Operacional
- Autenticação / Atividade de usuário
- Eventos de segurança

### 🔎 Indicadores que mostram isso
Nos eventos do arquivo, aparecem campos típicos como:
- `@timestamp` → tempo do evento
- `event.action` → o que aconteceu
- `event.category` → categoria do evento (ex: authentication, process, network)
- `event.outcome` → sucesso ou falha
- `user.name` → usuário envolvido
- `source.ip` → origem da ação

📌 Esses campos seguem o padrão ECS (Elastic Common Schema).

### ✅ Conclusão SOC

> Esses dados representam eventos de segurança e atividade de sistema, normalizados pelo Elastic, usados para monitoramento, detecção de incidentes e investigação SOC.

Em termos práticos:
- 📊 Não é dado de aplicação genérica
- 🔐 É dado de segurança
- 🚨 Serve para detectar:
  - falhas de login
  - acessos suspeitos
  - comportamento anômalo
  - possíveis ataques