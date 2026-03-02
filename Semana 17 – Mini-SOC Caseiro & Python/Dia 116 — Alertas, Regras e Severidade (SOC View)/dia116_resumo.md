# Dia 116 — Alertas, Regras e Severidade (SOC View)

## Objetivo

Entender como o Wazuh transforma logs em alertas e como um analista SOC prioriza eventos.

Fluxo:
Log → Decoder → Rule → Level → Alert

---

## Conceitos-chave

- Nem todo log vira alerta.
- A regra define a severidade.
- Level alto não significa incidente automático.
- Evento ≠ Alerta ≠ Incidente.

---

## Prática

- Seleção de 3 alertas (baixo, médio e alto).
- Análise de rule.id, level, timestamp e origem.
- Classificação como informativo, suspeito ou incidente.
- Priorização baseada em risco e impacto.

---

## Resultado

Capacidade de:
- Ler e interpretar alertas.
- Entender o papel das regras.
- Diferenciar ruído de ameaça real.
- Priorizar como SOC Júnior.