# `README.md` — Resumo do Dia 125

# Resumo — Dia 125: Automatizando Relatório de Incidentes

## Objetivo

Automatizar a geração de um relatório de incidentes a partir dos alertas do Wazuh (`alerts.json`), resumindo as informações mais relevantes para facilitar a tomada de decisão por analistas e gestores.

## Conceitos estudados

* Leitura automática do arquivo `alerts.json`
* Filtragem de alertas críticos (`rule.level >= 10`)
* Identificação do IP mais recorrente
* Identificação do usuário mais afetado
* Geração automática de relatórios
* Classificação simples de risco baseada na quantidade de alertas

## Fluxo implementado

```
alerts.json
      ↓
 Script Bash
      ↓
Filtro (Level ≥ 10)
      ↓
Análise Estatística
      ↓
Relatório Automático
```

## Ferramentas utilizadas

* Bash
* jq
* Wazuh
* Linux

## Aprendizados

* Como transformar dados brutos em informação útil.
* Como gerar relatórios automaticamente para reduzir trabalho manual.
* Como identificar rapidamente padrões de ataque.
* Como apresentar resultados de forma objetiva para gestores.

## Resultado

Foi desenvolvido um script capaz de gerar automaticamente um relatório contendo estatísticas dos alertas críticos, IPs mais recorrentes, usuários mais afetados e uma classificação geral de risco.
