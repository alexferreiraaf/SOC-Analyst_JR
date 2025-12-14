# 📘 Dia 60 — Buscas e Dashboards no Splunk (TryHackMe)

## 🎯 Objetivo do Dia

Consolidar o uso do **SPL aplicado a logs reais em JSON**, criando **buscas, dashboards e detecções** utilizadas por **SOC Level 1 e 2**, com foco em **email, endpoint e DNS**.

---

## 🧠 Tipos de Logs Trabalhados

- **Email Security** → `datasource=email`
- **Endpoint Windows (Sysmon)** → `datasource=sysmon`
  - Processos: `event.code=1`
  - Registry: `event.code=13`
  - DNS: `event.code=22`
- **Formato dos eventos:** `sourcetype=_json`

Filtro base utilizado em todas as análises:

```spl
sourcetype=_json
```

---

## 🔹 Comandos SPL Essenciais Aplicados

### `stats`

```spl
| stats count by host.name
```

Hosts com volume anormal de eventos podem indicar comprometimento.

---

### `top`

```spl
| top sender
```

Identificação de remetentes recorrentes em campanhas de phishing.

---

### `table`

```spl
| table timestamp sender recipient subject
```

Usado para investigação e relatórios.

---

### `eval`

```spl
| eval risco=if(match(content,"Bitcoin|inheritance|banking"),"Alto","Normal")
```

Classificação de emails suspeitos.

---

### `where`

```spl
| where count > 2
```

Filtro pós-processamento para detecções.

---

### `timechart`

```spl
| timechart count
```

Análise temporal de eventos e picos de atividade.

---

## 📊 Dashboard — SOC Overview

**SOC – Email, Endpoint & DNS**

Inclui:
- Emails inbound (volume)
- Top remetentes externos
- Processos criados por host
- Alterações de registry
- DNS queries suspeitas

---

## 🔥 Atividades Práticas

- Identificação do host mais ativo
- Detecção de emails suspeitos
- Análise de horários com maior concentração de eventos

---

## 🚨 Detecções Criadas

- Email inbound suspeito
- Execução de PowerShell
- DNS para domínios suspeitos

---

## 🏆 Desafio Avançado (SOC 2)

Dashboard interativo com filtros, linha do tempo e drilldown por host.

---

## 📦 Conclusão

Dia focado em SPL, dashboards e investigação SOC realista, com material pronto para portfólio.
