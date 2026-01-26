Justificativa de Severidade — Alta

Este incidente é classificado como Severidade Alta porque apresenta características claras de ataque automatizado (brute force em SSH), e não de erro humano.

Fatores observados:
- Alto volume de falhas de login em curto intervalo de tempo
- Origem externa desconhecida
- Tentativas direcionadas a usuários privilegiados (root, admin)
- Persistência do ataque, indicando tentativa ativa de comprometimento

Mesmo sem confirmação de acesso bem-sucedido, o risco é elevado, pois o objetivo do ataque é obter acesso administrativo ao servidor, o que pode resultar em comprometimento total do sistema.

Conclusão SOC:
Ataque confirmado em andamento ou recorrente. Classificação: Severidade Alta. Ação imediata recomendada.
