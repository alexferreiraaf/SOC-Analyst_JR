# Resumo — Dia 124: Bash para Extrair Alertas Críticos

## Objetivo

Aprender a automatizar a triagem de alertas críticos do Wazuh utilizando Bash e `jq`, criando um script capaz de filtrar eventos importantes a partir do arquivo `alerts.json`.

## Conceitos estudados

- Localização do arquivo `alerts.json`
- Uso do `jq` para manipular JSON
- Uso de `grep`, `awk` e pipes
- Redirecionamento de saída (`>` e `>>`)
- Automação da análise de alertas
- Priorização baseada em severidade

## Fluxo implementado

```

alerts.json
↓
Script Bash
↓
Filtro (level >= 10)
↓
Arquivo JSON com alertas críticos
↓
Resumo dos IPs mais recorrentes

```

## Ferramentas utilizadas

- Bash
- jq
- Wazuh
- Linux

## Aprendizados

- Como extrair apenas alertas relevantes.
- Como automatizar tarefas repetitivas no SOC.
- Como identificar rapidamente os IPs com maior quantidade de alertas.
- Como preparar dados para análises futuras ou relatórios.

## Resultado

Foi desenvolvido um script Bash capaz de filtrar automaticamente alertas críticos do Wazuh e apresentar estatísticas básicas sobre os principais IPs ofensores.