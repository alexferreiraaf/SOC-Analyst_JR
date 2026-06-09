# Análise de Cenário — Login Suspeito

## Descrição do cenário

Durante o monitoramento do ambiente foram identificadas cinco tentativas consecutivas de autenticação SSH com falha, seguidas posteriormente por um login realizado com sucesso.

Esse padrão pode indicar uma tentativa de ataque de força bruta com descoberta da credencial correta.

---

## Regra criada

### Rule ID

100200

### Objetivo

Detectar cinco falhas de autenticação SSH em até 120 segundos.

### Configuração

- Frequency: 5
- Timeframe: 120 segundos
- Severidade: Level 10

---

## Regra complementar

### Rule ID

100201

### Objetivo

Elevar a criticidade quando ocorrer um login bem-sucedido após múltiplas falhas recentes.

### Severidade

Level 12

---

## Justificativa técnica da severidade

### Level 10

Utilizado para indicar atividade altamente suspeita compatível com tentativa de brute force.

Embora ainda não exista evidência de comprometimento, a recorrência das falhas exige atenção prioritária.

### Level 12

Aplicado quando há falhas seguidas de autenticação bem-sucedida.

Esse comportamento aumenta significativamente a probabilidade de comprometimento da conta monitorada.

---

## Avaliação do risco

Os principais fatores analisados são:

- Quantidade de falhas consecutivas.
- Janela de tempo reduzida.
- Existência de login posterior com sucesso.
- Origem do endereço IP.
- Tipo de usuário envolvido (administrativo ou comum).
- Horário do evento.

---

## Decisão operacional

### Cenário 1

- IP externo
- Usuário root
- 6 falhas
- 1 login bem-sucedido

**Decisão:**

- Escalar imediatamente para o SOC N2.
- Abrir incidente.
- Solicitar bloqueio do IP.
- Iniciar investigação de comprometimento.

---

### Cenário 2

- IP interno
- Usuário comum
- 5 falhas
- Login realizado pelo próprio colaborador

**Decisão:**

- Classificar inicialmente como atividade suspeita.
- Confirmar com o usuário.
- Caso justificado, registrar como falso positivo e encerrar.

---

## Conclusão

A análise não deve considerar apenas a quantidade de eventos, mas principalmente o contexto em que ocorreram.

Falhas repetidas seguidas de sucesso representam um forte indicador de comprometimento potencial e devem receber prioridade elevada na triagem do SOC.