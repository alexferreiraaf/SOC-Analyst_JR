# Análise SOC — Dia 79

## Conclusão

Foi identificado um IP externo com alto volume de falhas de login SSH,
caracterizando tentativa de brute force.

### Classificação
- Tipo: Ataque de força bruta SSH
- Severidade: Média a Alta
- Confiança: Alta

### Ações recomendadas
- Bloquear IP atacante
- Verificar sucessos após falhas
- Aplicar hardening SSH
- Monitorar o host
