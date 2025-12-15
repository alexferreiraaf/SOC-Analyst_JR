# 📘 Dia 61 — Python & JSON: Estrutura e Manipulação (Resumo SOC)

## 🎯 Objetivo do Dia

Consolidar o uso de **JSON com Python** no contexto de **SOC**, focando em leitura, escrita, conversão, filtragem, normalização, correlação e enriquecimento de logs.

---

## 🔹 O que é JSON e por que é crítico no SOC

JSON é o formato padrão para:

* Logs de SIEMs (Splunk, Wazuh, ELK)
* APIs de reputação (VirusTotal, IPInfo, AbuseIPDB)
* Integração entre sistemas de segurança
* Normalização e enriquecimento de eventos

💡 Vantagens:

* Leve
* Estrutura simples
* Totalmente compatível com Python
* Ideal para automação SOC

---

## 🔹 Estrutura de um JSON

### Exemplo — Log de autenticação

```json
{
  "user": "root",
  "src_ip": "192.168.4.22",
  "status": "FAILED",
  "timestamp": "2025-11-14T01:22:10"
}
```

### Exemplo — Log enriquecido

```json
{
  "src_ip": "8.8.8.8",
  "country": "US",
  "org": "Google LLC",
  "threat_score": 2
}
```

---

## 🔹 Biblioteca `json` (Python)

| Função         | Uso                                   |
| -------------- | ------------------------------------- |
| `json.load()`  | Lê JSON de arquivo                    |
| `json.loads()` | Lê JSON em string                     |
| `json.dump()`  | Salva JSON em arquivo                 |
| `json.dumps()` | Converte objeto Python em string JSON |

---

## 🔹 CSV ↔ JSON no SOC

* Ferramentas legadas → CSV
* APIs modernas → JSON

📌 Função do analista SOC:

> Converter → Normalizar → Enriquecer → Correlacionar → Exportar

---

## 🔹 JSON com listas (logs reais)

```json
[
  {"ip": "10.0.0.1", "falhas": 3},
  {"ip": "10.0.0.2", "falhas": 8}
]
```

Muito comum em:

* Alertas
* Relatórios
* Exportações de SIEM

---

## ⭐ Atividades Práticas — Conceitos-chave

### ✅ Atividade 1 — CSV → JSON

* Uso de `csv.DictReader`
* Conversão estruturada para JSON
* Base para ingestão em SIEM

### ✅ Atividade 2 — Filtro SOC PRO

* Leitura de logs JSON
* Filtro por critério (`falhas > 3`)
* Geração de `alertas.json`

### ✅ Atividade 3 — Visualização

* Uso de `pprint`
* Leitura rápida e clara de alertas

---

## 🔥 Exercícios Fundamentais para SOC

### 1️⃣ Função genérica para carregar JSON

Permite reutilização e modularização do código.

### 2️⃣ Detecção de IPs repetidos

Base para:

* Brute force
* Scanning
* Comportamento anômalo

### 3️⃣ Correlação entre múltiplos arquivos

Detecta IPs presentes em:

* auth.json
* syslog.json
* firewall.json

➡️ Simula correlação real de SIEM

### 4️⃣ Cálculo de risco

```python
risco = falhas * 2
```

Base para score de severidade

### 5️⃣ Normalização de campos

Exemplo:

```json
{"IP-SOURCE": "10.0.0.5"}
```

⬇️

```json
{"src": "10.0.0.5"}
```

Essencial para correlação entre ferramentas diferentes

---

## 🧩 Desafio Avançado — SOC 1 → SOC 2

Sistema completo de **enriquecimento de logs**:

* Leitura de logs JSON
* Enriquecimento via API (GeoIP / Organização)
* Geração de `logs_enriquecidos.json`
* Relatório resumido:

  * Top 5 países
  * Top 5 organizações
  * IPs mais ativos

💡 Simula pipelines reais de SOC

---

## 🏆 MegaDesafio (Opcional)

Criar um **CLI SOC**:

```bash
python analisador.py --input logs.json --output alertas.json --threshold 4
```

Com:

* `argparse`
* Funções modulares
* Uso profissional em automações

---

## 🧠 Competências SOC Desenvolvidas

✔ Manipulação avançada de JSON
✔ Automação de análise de logs
✔ Correlação de eventos
✔ Normalização de dados
✔ Enriquecimento com fontes externas
✔ Pensamento SOC Nível 2

---

📌 **Resumo final**: JSON é a espinha dorsal da automação em SOC. Dominar sua estrutura e manipulação com Python é um divisor de nível entre **iniciante** e **analista SOC operacional**.
