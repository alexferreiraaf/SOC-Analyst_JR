# 📘 Dia 62 — Automação SOC com Python + Splunk (TryHackMe)

## 🎯 Objetivo do Dia
Aprender a **automatizar análises SOC** usando Python em conjunto com o Splunk do TryHackMe, mesmo sem acesso à API REST, simulando um fluxo real de SIEM + automação externa.

---

## 🚫 Limitações do Splunk no TryHackMe
- API REST (porta 8089) bloqueada
- Sem tokens ou permissões admin
- Alertas persistentes via Splunk indisponíveis

✅ Adaptação SOC realista:
- Splunk executa buscas
- Resultados são exportados
- Python processa e gera alertas
- Relatórios externos

---

## 🔁 Fluxo SOC Simulado
Splunk → Export JSON/CSV → Python → Alertas/Relatórios

---

## 🔍 Buscas SPL Utilizadas

### Logins falhos
sourcetype=_json | search action=login attempt=failed | stats count by user | sort -count

### Hosts mais ativos
sourcetype=_json | stats count by host.name | sort -count

### Execuções suspeitas (PowerShell)
sourcetype=_json datasource=sysmon event.code=1 | search process.name="powershell.exe" | stats count by host.name

---

## 📤 Exportação
Arquivos:
- logins_falhos.json
- hosts.json
- processos.json

---

## 🐍 Python — Processamento SOC

```python
import json

def carregar_resultados(arquivo):
    with open(arquivo) as f:
        return json.load(f)
```

### Geração de alertas
```python
dados = carregar_resultados("logins_falhos.json")
alertas = [d for d in dados if int(d["count"]) > 5]

with open("alertas_splunk.json", "w") as f:
    json.dump(alertas, f, indent=4)
```

---

## 📊 Dashboard Externo (Simulado)
```json
{
  "usuarios": [
    {"usuario": "admin", "falhas": 7},
    {"usuario": "alex", "falhas": 4}
  ]
}
```

---

## 🧠 Entrevista
“No TryHackMe, adaptei o fluxo SOC usando export manual do Splunk e automação em Python, simulando um SOC real.”

---

## 📦 Entregáveis
- Queries SPL
- JSONs exportados
- Scripts Python
- Alertas simulados
- Relatório SOC
