# DIA 131 — Enriquecimento de IOC

## 1. IOC Identificado

**Tipo:** Endereço IP

**IOC:** `185.223.89.44`

---

## 2. Dados de Enriquecimento

### País
- Rússia (cenário simulado para o laboratório)

### ASN
- Hosting Provider

### Tipo
- Datacenter / VPS

### Histórico / Reputação
- Associado a atividades de scanning e tentativas de brute force em serviços SSH.
- Pode ser utilizado por atacantes para automatizar ataques devido à facilidade de criação e descarte de máquinas virtuais.

> **Observação:** Essas informações representam um cenário de estudo e devem sempre ser verificadas em fontes confiáveis durante uma investigação real.

---

## 3. Cruzamento com os Logs

### Tipo de evento

Possível ataque de força bruta seguido de comprometimento.

### Usuário envolvido

`root`

### Horário

02:14 da manhã

### Volume observado

- 2 tentativas de login com falha
- 1 login realizado com sucesso
- 2 eventos posteriores de criação de usuários

---

## 4. Análise de Risco

### Antes do enriquecimento

As evidências já indicavam comportamento altamente suspeito:

- Login do usuário root
- Horário incomum
- IP externo
- Sequência de falhas seguida de sucesso
- Ações administrativas após autenticação

**Classificação inicial:** Alto risco.

---

### Após o enriquecimento

Com a informação de que o endereço pertence a um datacenter e possui histórico relacionado a ataques automatizados, aumenta significativamente a confiança na hipótese de comprometimento.

O enriquecimento não prova que ocorreu um ataque, mas fortalece a análise baseada em evidências.

**Classificação revisada:** Alto risco / Possível incidente confirmado.

---

## 5. Conclusão Final

### Classificação

🚨 ALTO RISCO

### Necessita escalonamento?

**Sim.**

### Justificativa

A combinação de diversos fatores aumenta significativamente a criticidade do evento:

- Origem externa;
- Conta privilegiada (`root`);
- Horário atípico;
- Tentativas de autenticação malsucedidas seguidas de sucesso;
- Criação de novos usuários após o login;
- IOC pertencente a provedor de hospedagem com histórico relacionado a ataques.

A recomendação é abrir incidente, bloquear temporariamente o IP, revisar logs adicionais do servidor, validar a legitimidade do acesso e realizar troca imediata das credenciais comprometidas.