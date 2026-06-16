# DIA 130 — Validação da Automação

## 1. Análise Manual do Caso

### Tentativas de Login

- Total de falhas: 2
- Total de sucessos: 1

### Houve sucesso?

Sim. Após duas tentativas falhas, foi registrado um login bem-sucedido para o usuário `root`.

### Origem

- **IP:** 185.223.89.44
- **Tipo:** Externo (não pertence a faixa de IPs privados)

### Ações Pós-Login

Após o login bem-sucedido foram identificadas duas ações de criação de usuários (`add_user`), indicando possível tentativa de persistência no ambiente.

### Classificação Final

**ALTO / Incidente Confirmado**

Justificativa:

- Login do usuário `root`;
- Origem externa;
- Horário incomum (02:14 da manhã);
- Falhas seguidas de sucesso;
- Criação de novos usuários após autenticação.

Todos esses fatores aumentam significativamente a probabilidade de comprometimento.

---

## 2. Resultado do Script

### Classificação

ALTO

### Justificativa do Script

O script classificou o evento com base em:

- Level elevado;
- Usuário privilegiado (`root`);
- IP externo.

Entretanto, a decisão ocorreu apenas por regras estáticas, sem compreender toda a sequência dos eventos.

---

## 3. O Script Acertou?

**Sim, mas parcialmente.**

O resultado final foi correto, porém a classificação ocorreu por coincidência das regras implementadas.

O script não identificou explicitamente que houve:

- Falhas consecutivas;
- Login bem-sucedido logo após;
- Criação de usuários;
- Possível persistência.

Um analista humano chegou à mesma conclusão utilizando contexto e correlação.

---

## 4. Onde a Automação Falhou?

A automação atual não possui capacidade de:

- Correlacionar eventos ao longo do tempo;
- Detectar sequência "failed_login → success_login";
- Identificar atividades de persistência após autenticação;
- Relacionar múltiplos eventos do mesmo IP;
- Considerar histórico do usuário;
- Avaliar comportamento anômalo.

Ela trabalha apenas com regras simples sobre um único evento.

---

## 5. Melhorias Propostas

- [x] Detectar sequência de eventos (falha seguida de sucesso)
- [x] Detectar criação de usuários após login privilegiado
- [x] Detectar horário fora do expediente
- [x] Diferenciar IP interno e externo
- [x] Implementar correlação temporal
- [x] Agrupar eventos por IP e usuário
- [x] Calcular score baseado em múltiplos indicadores
- [ ] Integrar reputação de IP
- [ ] Consultar listas de IOC externas

---

## 6. Decisão Final do Analista

### Classificação Final

**Incidente Crítico (Alto Risco)**

### Escalonamento Necessário?

**Sim.**

### Ações Recomendadas

- Bloquear imediatamente o IP ofensivo.
- Revogar sessões ativas do usuário comprometido.
- Resetar credenciais do usuário `root`.
- Investigar os usuários criados durante o incidente.
- Verificar movimentação lateral em outros servidores.
- Escalar para SOC N2 / Blue Team.
- Preservar evidências para análise forense.

---

## Conclusão

Este laboratório demonstra que a automação é excelente para acelerar a triagem inicial, porém não substitui o julgamento humano. A correlação entre eventos e a análise contextual continuam sendo essenciais para identificar incidentes reais e reduzir falsos positivos.