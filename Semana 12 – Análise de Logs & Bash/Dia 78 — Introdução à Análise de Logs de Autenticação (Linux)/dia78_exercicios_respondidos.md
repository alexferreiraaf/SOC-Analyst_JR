# Dia 78 — Análise de Logs de Autenticação Linux (Respostas)

Este documento contém as respostas dos **Exercícios Práticos do Dia 78**, com base no arquivo `auth.log` fornecido para o laboratório.

---

## 🔸 Exercício 1 — Identificação manual

**Perguntas e respostas:**

### ✔️ Qual IP mais aparece?
- **45.77.89.100**
- Motivo: aparece em diversas tentativas consecutivas de login SSH falho, direcionadas a múltiplos usuários.

### ✔️ Qual usuário é mais atacado?
- **admin** e **root**
- Motivo: ambos são alvos comuns em ataques automatizados de brute force, pois costumam existir em sistemas Linux.

### ✔️ Horário dos eventos?
- Principalmente durante a **madrugada (00:01)** e início da manhã (**09:02**).
- SOC Insight: ataques costumam ocorrer fora do horário comercial para reduzir chance de detecção imediata.

---

## 🔸 Exercício 2 — Diferenciando erro de senha x brute force

É possível diferenciar **erro humano** de **ataque de brute force** analisando padrões no log:

### 🧠 Erro de senha (legítimo):
- Poucas tentativas
- Mesmo usuário
- Intervalos grandes entre tentativas
- IP conhecido ou interno

### 🚨 Brute force:
- Muitas tentativas em curto período
- Mesmo IP tentando vários usuários
- Usuários comuns ou inválidos (`admin`, `root`, `test`)
- Mensagens como `invalid user`
- Pode haver sucesso após várias falhas (cenário crítico)

**Conclusão:**  
No arquivo analisado, o comportamento do IP `45.77.89.100` caracteriza **brute force automatizado**.

---

## 🔸 Exercício 3 — Campos essenciais para investigação SOC

Os campos mínimos que um analista SOC precisa identificar em logs de autenticação Linux são:

- **Horário**  
  → Quando o evento ocorreu (linha do tempo do ataque)

- **Usuário**  
  → Conta alvo do ataque (`admin`, `root`, etc.)

- **IP de origem**  
  → Origem da tentativa de acesso (possível atacante)

- **Ação**  
  → Resultado da tentativa:
  - `Failed password`
  - `Accepted password`
  - `invalid user`

Sem esses campos, a investigação fica incompleta e a detecção pode falhar.

---

## 🏁 Conclusão SOC

A análise do `auth.log` demonstra claramente um cenário de **brute force em SSH**, permitindo:

- identificação do atacante
- identificação do alvo
- entendimento do horário
- decisão de resposta (bloqueio, rate limit, escalonamento)

> “Quem entende o log, entende o ataque.” 🛡️🐧
