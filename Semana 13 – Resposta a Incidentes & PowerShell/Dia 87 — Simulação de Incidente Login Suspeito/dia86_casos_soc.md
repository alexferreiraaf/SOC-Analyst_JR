# Casos Comuns Analisados por um SOC

## Caso 1 — Brute Force
- Vários eventos 4625 do mesmo IP
- Curto intervalo de tempo
- Ação: Bloqueio de IP e ajuste de políticas

## Caso 2 — Conta Comprometida
- Evento 4624 após múltiplos 4625
- Logon fora do horário normal
- Ação: Reset de senha e isolamento

## Caso 3 — Escalada de Privilégios
- Evento 4672 identificado
- Usuário sem perfil administrativo
- Ação: Investigação imediata

## Caso 4 — Criação de Conta Suspeita
- Evento 4720 sem ticket aprovado
- Ação: Desabilitar conta e auditoria

## Caso 5 — Alteração de Políticas
- Evento 4719 detectado
- Possível tentativa de evasão
- Ação: Revisão de mudanças e rollback
