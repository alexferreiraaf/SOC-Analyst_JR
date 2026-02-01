# Dia 89 — Decisão SOC

## Classificação do Evento
Incidente de segurança confirmado.

---

## Justificativa

- Foram identificadas múltiplas falhas de logon (4625) do mesmo IP
- Ocorreu logon bem-sucedido subsequente (4624)
- O acesso ocorreu fora do horário comercial
- LogonType 10 indica acesso remoto via RDP
- Houve execução de processo após o login (4688)
- Privilégios administrativos foram concedidos (4672)

---

## Decisão SOC

O evento não é um alerta isolado.
Trata-se de um incidente crítico com indícios de comprometimento de credencial.

---

## Ações Recomendadas

- Bloquear IP de origem
- Desabilitar ou resetar credencial do usuário
- Iniciar resposta a incidentes conforme NIST 800-61
- Preservar evidências para análise posterior
