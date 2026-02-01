# Coletor SOC — Eventos Críticos Windows

Ferramenta PowerShell para coleta padronizada de eventos críticos
do Windows Security Log, voltada para uso em SOC e Resposta a Incidentes.

## Eventos Coletados
- 4625 — Falhas de logon
- 4624 — Logon bem-sucedido
- 4688 — Criação de processos
- 4672 — Privilégios elevados
- 4720 — Criação de usuários

## Funcionalidades
- Coleta automatizada
- Evidências separadas por tipo
- Timeline consolidada
- Preservação de evidências
- Base para SIEM / IR

## Uso
1. Executar PowerShell como Administrador
2. Permitir execução:
