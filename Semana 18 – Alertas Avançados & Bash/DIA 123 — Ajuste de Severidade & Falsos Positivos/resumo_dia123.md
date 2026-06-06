# Resumo – Dia 123: Ajuste de Severidade e Falsos Positivos

## Objetivo

Aprender a calibrar corretamente a severidade dos alertas no Wazuh e identificar falsos positivos, tomando decisões baseadas em contexto e risco, como um analista SOC.

## Principais Conceitos

- Severidade (Level) não representa automaticamente o impacto real do incidente.
- Um mesmo evento pode ter classificações diferentes dependendo do contexto.
- Falsos positivos são alertas legítimos gerados por atividades benignas.
- A análise deve considerar:
  - Origem do IP (interno ou externo)
  - Usuário envolvido
  - Horário da atividade
  - Quantidade de eventos
  - Existência de sucesso após falhas

## Escala Geral de Severidade

| Level | Classificação |
|---------|--------------|
| 0–3 | Informativo |
| 4–7 | Atividade suspeita |
| 8–10 | Alto risco |
| 11–15 | Crítico |

## Aprendizados

- Evitar configurar todos os alertas como críticos.
- Reduzir ruído operacional através de uma boa calibração.
- Diferenciar erros de usuários legítimos de possíveis ataques.
- Justificar tecnicamente o nível atribuído a cada regra.

## Conclusão

A correta definição da severidade melhora a priorização de incidentes, reduz fadiga de alertas e aumenta a eficiência operacional do SOC.