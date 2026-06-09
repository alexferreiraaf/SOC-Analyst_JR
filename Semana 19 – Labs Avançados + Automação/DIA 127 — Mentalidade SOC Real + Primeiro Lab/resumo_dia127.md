# Resumo — Dia 127: Mentalidade SOC Real + Primeiro Lab

## Objetivo
Aprender a identificar comportamentos suspeitos relacionados a autenticações SSH, diferenciando erros comuns de possíveis comprometimentos de segurança.

## Conceitos principais

- Múltiplas falhas de login podem indicar tentativa de brute force.
- Falhas seguidas de um login bem-sucedido representam um cenário de maior risco.
- O contexto é essencial para classificar um alerta:
  - Origem do IP (interno ou externo)
  - Usuário envolvido
  - Horário da atividade
  - Existência de login bem-sucedido após as falhas

## Regra customizada

Foi criada uma regra no `local_rules.xml` para detectar:

- 5 falhas de login em até 2 minutos.
- Possível comprometimento quando há falhas seguidas de sucesso.

## Fluxo da detecção

```
Tentativas de login
        ↓
Logs em /var/log/auth.log
        ↓
Wazuh Decoder
        ↓
Wazuh Rule
        ↓
Alerta no Dashboard
        ↓
Análise pelo SOC
```

## Aprendizados

- Contexto vale mais que quantidade de eventos.
- Nem toda falha é incidente.
- Falha + sucesso merece investigação prioritária.
- Severidade deve refletir o risco do cenário.

## Resultado esperado

Ao final do laboratório o analista consegue:

- Detectar brute force.
- Identificar possível comprometimento.
- Justificar a severidade aplicada.
- Decidir quando escalar um incidente para níveis superiores.