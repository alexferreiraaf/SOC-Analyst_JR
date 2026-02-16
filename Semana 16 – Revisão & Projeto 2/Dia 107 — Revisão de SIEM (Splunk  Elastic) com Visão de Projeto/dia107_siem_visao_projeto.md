# Dia 107 — SIEM com Visão de Projeto

## 🎯 Papel do SIEM no SOC

O SIEM é o motor central de detecção do SOC. Ele não é apenas uma ferramenta de consulta de logs, mas o sistema responsável por:

- Centralizar logs de múltiplas fontes
- Normalizar dados
- Correlacionar eventos
- Gerar alertas acionáveis
- Apoiar investigação e resposta a incidentes

Sem SIEM, o SOC perde capacidade de escala e correlação.

---

## 🔎 Log x Evento x Alerta x Incidente

- **Log** → Dado bruto (ex: registro no firewall)
- **Evento** → Log interpretado (ex: falha de login)
- **Alerta** → Regra disparada no SIEM
- **Incidente** → Alerta validado com impacto confirmado

---

## 🧠 IOC x Evento

- **IOC (Indicator of Compromise)** → IP malicioso, hash suspeito, domínio conhecido
- **Evento** → Ação registrada no ambiente

IOC é inteligência conhecida.
Evento é comportamento observado.

---

## 🛠️ Splunk (Visão SOC)

- Indexação de dados
- Investigação via SPL
- Criação de alertas por:
  - Volume
  - Frequência
  - Padrão
  - Contexto

Casos comuns:
- Brute force
- Port scan
- Login fora do horário
- IP malicioso

---

## 🛠️ Elastic Stack (Visão SOC)

- Beats/Agents para coleta
- Elasticsearch para armazenamento
- Kibana para visualização
- Regras e Machine Learning para detecção

---

## ⚖️ Comparação Splunk x Elastic

| Critério | Splunk | Elastic |
|----------|---------|----------|
| Curva inicial | Rápida | Média |
| Linguagem | SPL | KQL |
| Uso em SOC | Muito alto | Muito alto |
| Custo | Alto | Flexível |

---

## 🧠 Conclusão

O SIEM conecta:

Coleta → Correlação → Alerta → Investigação → Resposta → Relatório

Ele é o núcleo operacional do SOC.
