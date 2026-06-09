# Resumo — Dia 129: Automação de Triagem Inicial

## Objetivo

Criar um mecanismo simples para classificar automaticamente alertas do Wazuh utilizando regras de negócio e contexto.

## Principais conceitos

- Triagem inicial de incidentes.
- Classificação baseada em `rule.level`.
- Ajuste do risco considerando:
  - Usuário privilegiado (`root` ou `admin`);
  - IP externo;
  - Horário incomum.
- Utilização de um sistema de pontuação (score) para definir a prioridade.

## Fluxo da automação

1. Ler o último alerta do `alerts.json`.
2. Definir um risco base conforme o nível (`level`).
3. Somar pontos conforme o contexto.
4. Calcular o score final.
5. Classificar o alerta como:
   - BAIXO
   - MÉDIO
   - ALTO

## Aprendizado principal

A severidade do alerta, por si só, não é suficiente para determinar o risco. Uma boa triagem considera informações adicionais, como tipo de usuário, origem do acesso e horário da atividade, reduzindo falsos positivos e melhorando a priorização dos incidentes.