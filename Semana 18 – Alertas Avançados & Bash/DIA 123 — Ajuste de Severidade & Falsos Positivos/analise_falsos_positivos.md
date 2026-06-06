# Análise sobre Falsos Positivos e Ajuste de Severidade

## Quando reduzir o nível de severidade?

A severidade deve ser reduzida quando o contexto indicar baixa probabilidade de ataque real, por exemplo:

- Usuário digitando a senha incorretamente.
- Administrador realizando manutenção autorizada.
- Scripts internos executando autenticações automáticas.
- Testes realizados pela própria equipe de infraestrutura.

Nesses casos, apesar da regra ser acionada corretamente, não há evidências suficientes para caracterizar um incidente.

---

## Quando aumentar o nível de severidade?

A severidade deve ser elevada quando houver fatores que aumentem o risco, tais como:

- Origem externa desconhecida.
- Ataques direcionados ao usuário root.
- Grande volume de tentativas em curto período.
- Login bem-sucedido após diversas falhas.
- Atividades ocorrendo fora do horário normal da organização.

Esses cenários indicam maior probabilidade de comprometimento e exigem resposta rápida.

---

## Quando classificar como Falso Positivo (FP)?

Um alerta pode ser tratado como falso positivo quando:

- Existe justificativa operacional conhecida.
- O comportamento observado é esperado para aquele ambiente.
- A investigação confirma ausência de atividade maliciosa.
- Não há impacto para confidencialidade, integridade ou disponibilidade.

Importante destacar que um falso positivo não significa erro da ferramenta, mas sim que a regra detectou corretamente um comportamento que, naquele contexto específico, é legítimo.

---

## Considerações Finais

A calibração adequada das regras reduz o excesso de alertas, melhora a produtividade do SOC e permite que incidentes realmente críticos recebam prioridade durante a investigação.