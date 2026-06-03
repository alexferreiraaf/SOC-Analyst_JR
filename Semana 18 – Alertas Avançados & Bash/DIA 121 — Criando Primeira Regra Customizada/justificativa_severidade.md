## Severidade Escolhida
### Level 10

A severidade 10 foi escolhida por representar uma atividade potencialmente suspeita que merece investigação, mas que não caracteriza automaticamente um incidente crítico.

### Justificativa
Um login fora do horário pode ocorrer por diversos motivos legítimos:
- Manutenção programada
- Equipe de infraestrutura
- Trabalho remoto
- Plantão técnico

Por outro lado, também pode indicar:
- Credenciais comprometidas
- Acesso indevido
- Movimentação de atacante

Por isso o evento deve ser tratado como um alerta relevante e investigado.

### Por que não utilizar Level 12?
Level 12 é normalmente reservado para eventos com maior probabilidade de comprometimento.
Se todo login fora do horário fosse marcado como crítico:

- Haveria excesso de escalonamentos
- Aumentaria a fadiga de alertas
- Poderiam surgir muitos falsos positivos

Em um SOC real, o contexto determina a classificação final.