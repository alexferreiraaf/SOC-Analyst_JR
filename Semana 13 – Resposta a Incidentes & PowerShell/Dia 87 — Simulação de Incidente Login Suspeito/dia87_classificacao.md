# 📌 Classificação do Incidente — Dia 87

## Tipo de Incidente
Comprometimento de Endpoint com comunicação externa suspeita.

## Severidade
**Alta**

## Justificativa
- Comunicação contínua com IP externo não reconhecido
- Execução de binário com nome semelhante a processo legítimo
- Persistência configurada via registro do Windows
- Indícios claros de beaconing para servidor C2

## Impacto Potencial
- Exfiltração de dados
- Movimentação lateral
- Comprometimento de credenciais

## Status
🚨 Incidente confirmado
