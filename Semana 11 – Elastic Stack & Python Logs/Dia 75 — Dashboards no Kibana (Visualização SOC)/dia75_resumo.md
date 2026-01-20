# Dia 75 — Dashboards no Kibana (Visualização SOC)

## 🎯 Objetivo do Dia
Aprender a criar **dashboards SOC no Kibana** com foco em:
- detecção rápida de comportamentos suspeitos
- monitoramento contínuo de incidentes
- redução de MTTD e MTTR
- visualização clara e acionável

Dashboards não servem para investigação profunda, mas para **alertar visualmente o SOC**.

---

## 🧠 Conceito Central SOC
> Um bom dashboard responde perguntas simples e críticas em poucos segundos.

---

## 📊 Tipos de Dashboards SOC

| Tipo | Uso |
|----|----|
| Operacional | Monitoramento diário |
| Investigativo | Acompanhamento de incidente |
| Executivo | Visão de status |

---

## 📈 Visualizações-Chave

### Total de eventos por tempo
- Line Chart
- Campo: `@timestamp`
- Métrica: Count

### Falhas de login por IP
- Filtro: `event.action:"login_failed"`
- Bar Chart

### Usuários mais atacados
- Campo: `user.name`
- Bar Chart

### Origem geográfica
- Campo: `source.geo.country_name`
- Map

### Tabela investigativa
- Campos: `@timestamp`, `user.name`, `source.ip`, `event.action`

---

## 🧩 Estrutura Recomendada

```
[ Timeline ]
[ Falhas por IP ] [ Falhas por Usuário ]
[ Mapa de Origem ]
[ Tabela Detalhada ]
```

---

## 🚨 Simulação SOC
Pico de falhas → identificar IP → validar usuário → verificar origem → investigar.

---

## ❌ Erros Comuns
- Gráficos inúteis
- Métricas sem ação
- Excesso de informações

---

## ✅ Boas Práticas
- Dashboards objetivos
- Métricas acionáveis
- Clareza visual

---

## 🏁 Conclusão
Dashboards SOC aceleram decisões e reduzem tempo de resposta.
