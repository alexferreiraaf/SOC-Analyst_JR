# Dia 73 — Checklist SOC de Parsing

Use este checklist antes de habilitar qualquer alerta em produção.

## Checklist de Ingestão

- [ ] source.ip foi extraído corretamente?
- [ ] user.name existe e não está vazio?
- [ ] event.action identifica claramente o evento?
- [ ] @timestamp está correto?
- [ ] Campos seguem o ECS?
- [ ] Parsing funciona para todos os formatos esperados?
- [ ] Não há campos críticos vazios?

## Insight SOC
Sem checklist, alertas entram em produção quebrados.
