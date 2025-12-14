# 📘 Dia 59 — Coleta, Investigação e Correlação de Logs no Splunk (TryHackMe)

## 🎯 Objetivo do Dia

Neste dia, o foco foi a **investigação prática em um SIEM realista**, utilizando os logs disponíveis no Splunk do TryHackMe.  
Ao final do estudo, foi possível analisar e correlacionar **email, endpoint e DNS**, simulando o trabalho diário de um **analista SOC**.

---

## 🧠 Tipos de Logs Analisados

- **Email (`datasource=email`)**
- **Endpoint Windows (`datasource=sysmon`)**
- **DNS (`event.code=22`)**

---

## 🔎 Filtro Base Utilizado

```spl
sourcetype=_json
```

---

## 📧 Investigação de Email

```spl
sourcetype=_json datasource=email direction=inbound
| search content="*Bitcoin*" OR content="*banking*" OR content="*inheritance*"
```

Emails internos com anexo:

```spl
sourcetype=_json datasource=email direction=internal attachment!="None"
```

---

## 🖥️ Investigação de Endpoint

Criação de processos:

```spl
sourcetype=_json datasource=sysmon event.code=1
```

Alterações de Registry:

```spl
sourcetype=_json datasource=sysmon event.code=13
```

---

## 🌐 Investigação DNS

```spl
sourcetype=_json datasource=sysmon event.code=22
```

---

## 🔗 Cadeia de Ataque

Email → Execução de PowerShell → DNS suspeito

MITRE ATT&CK:
- T1566.001
- T1059.001

---

## 🚨 Evento Mais Crítico

Email interno com anexo PowerShell (.ps1)

Ação SOC:
- Isolamento
- Bloqueio
- Investigação
- Erradicação

---

## 📊 Dashboard

SOC – Email & Endpoint Security

---

## 📦 Conclusão

Dia prático e realista, focado em correlação de eventos e resposta a incidentes.
