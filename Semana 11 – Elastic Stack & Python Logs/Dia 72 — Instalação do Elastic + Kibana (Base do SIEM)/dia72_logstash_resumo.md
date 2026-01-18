# Dia 72 — Logstash e Parsing (Visão SOC)

## Objetivo
Compreender o papel do Logstash na ingestão de logs e como o parsing impacta diretamente a detecção, investigação e alertas em um SOC.

---

## Papel do Logstash no SOC
O Logstash atua como o **tradutor** entre logs brutos e dados estruturados.

Sem parsing:
- Logs chegam como texto
- Campos não existem
- Alertas falham

Com parsing:
- IP, usuário e ação viram campos
- Detecção se torna possível

---

## Pipeline Básico
Todo pipeline possui:
- input: origem do log
- filter: parsing e normalização
- output: destino (Elasticsearch)

---

## Insight SOC
> Não existe detecção confiável sem parsing confiável.
