# Top 5 IPs Ofensores

## Comando utilizado

```bash
jq -r 'select(.rule.level >= 10) | .data.srcip // empty' alerts.json \
| sort \
| uniq -c \
| sort -nr \
| head -5
```

## Exemplo de resultado

| Quantidade | Endereço IP |
|------------|------------|
| 18 | 185.220.100.10 |
| 11 | 45.227.10.55 |
| 7 | 203.0.113.25 |
| 5 | 192.168.1.15 |
| 4 | 10.0.0.20 |

## Interpretação

Os IPs com maior quantidade de alertas devem ser priorizados durante a investigação, pois podem indicar atividades automatizadas, tentativas de brute force ou comportamentos maliciosos recorrentes.

A análise deve considerar também:

- Horário dos eventos;
- Tipo de regra acionada;
- Usuário alvo;
- Existência de autenticações bem-sucedidas após as falhas.