# Resumo — Dia 130: Resolver Lab Intermediário + Automação Aplicada

## Objetivo

Validar uma automação de classificação de alertas comparando sua decisão com a análise manual realizada por um analista SOC.

## Principais conceitos

- Triagem automática baseada em regras simples.
- Importância da análise contextual.
- Diferença entre classificação automática e investigação humana.
- Correlação de eventos para identificação de comprometimento.
- Limitações de scripts que analisam apenas eventos isolados.

## Fluxo de análise

1. Ler os eventos do cenário.
2. Identificar falhas de login.
3. Verificar se houve autenticação bem-sucedida.
4. Analisar ações executadas após o login.
5. Comparar a conclusão humana com a classificação do script.
6. Identificar melhorias para a automação.

## Aprendizado principal

Automações aceleram a triagem inicial, mas não substituem a capacidade do analista de correlacionar eventos, interpretar contexto e tomar decisões baseadas em evidências.

## Evolução técnica

Após este dia, o foco deixa de ser apenas criar scripts para extrair informações e passa a ser validar criticamente as decisões produzidas pela automação, identificando limitações e propondo melhorias para um SOC mais eficiente.