# Contagem de Eventos Críticos

## Método utilizado

Os eventos críticos foram filtrados utilizando o seguinte comando:

```bash
jq 'select(.rule.level >= 10)' alerts.json | wc -l
```

## Critério adotado

Foram considerados críticos todos os eventos com:

- `rule.level >= 10`

## Objetivo

Permitir que o analista priorize rapidamente os eventos de maior risco e reduza o tempo de triagem durante uma investigação.

## Exemplo de saída

```

Total de alertas críticos: 27

```