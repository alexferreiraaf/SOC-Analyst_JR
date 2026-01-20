# Dia 74 — Simulações SOC no Kibana Discover (KQL)

## 🧠 Contexto Geral
Simulações realizadas com base em eventos já parseados no Elastic Stack (ECS), utilizando o Kibana Discover como ferramenta principal de triagem SOC.

---

## 🔍 Prática 1 — Primeira investigação

### KQL
```kql
event.action:"login_failed"
```

### Análise SOC
- Alto volume de eventos em curto período
- Usuários afetados: admin, root, test, unknown
- IPs recorrentes: 192.168.1.50, 10.10.10.8, 45.77.89.100

**Conclusão:** Indícios claros de brute force.

---

## 🔍 Prática 2 — Investigando um IP suspeito

### KQL
```kql
source.ip:"192.168.1.50"
```

### Análise SOC
- ~30 eventos em poucos minutos
- Apenas falhas de login
- Nenhum login bem-sucedido
- Sem evidência de lateral movement

**Conclusão:** Ataque ativo sem sucesso.

---

## 🔍 Prática 3 — Detecção de brute force (usuário admin)

### KQL
```kql
event.action:"login_failed" and user.name:"admin"
```

### Análise SOC
- Conta privilegiada
- Muitas falhas consecutivas
- Mesmo IP de origem

**Risco:** Alto  
**Ação recomendada:** Escalada imediata.

---

## 🔍 Prática 4 — Exclusão de ruído

### KQL
```kql
event.action:"login_failed" and not source.ip:"192.168.0.*"
```

### Resultado
- Eventos internos removidos
- Foco apenas em IPs externos

**Benefício:** Redução de falsos positivos.

---

## 🚨 Simulação SOC — Alerta de Brute Force

### Etapas
1. Validação do alerta no Discover
2. Identificação do IP ofensivo
3. Contagem de tentativas (>20 em <10 min)
4. Verificação de login bem-sucedido (nenhum)

**Decisão SOC:**  
- Tipo: Brute Force  
- Severidade: Alta  
- Ação: Investigação + bloqueio preventivo

---

## 🧩 Exercícios Práticos

### 🔹 KQL — Logins fora do horário
```kql
event.action:"login_failed" and not @timestamp:[now-8h TO now-18h]
```

### 🔹 KQL — Usuário específico
```kql
user.name:"admin"
```

### 🔹 KQL — IP externo
```kql
source.ip:"45.77.89.100"
```

---

## 🧠 Triagem SOC — Reflexão

O Discover permite validar rapidamente:
- Volume
- Repetição
- Origem
- Usuário
- Janela temporal

Facilitando a distinção entre erro humano e ataque real.

---

## ✅ Checklist SOC de Investigação

- Tempo correto selecionado
- IP identificado
- Usuário analisado
- Evento repetido
- Sucesso posterior verificado
- IP interno ou externo
- Ação definida

---

## 🏁 Conclusão

Simulações demonstram domínio de:
- KQL
- Investigação no Discover
- Validação de alertas
- Tomada de decisão SOC

> SIEM não é ferramenta, é método de investigação.
