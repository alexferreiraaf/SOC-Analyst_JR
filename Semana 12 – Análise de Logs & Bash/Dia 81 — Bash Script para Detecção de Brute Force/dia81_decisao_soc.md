# 🚨 Decisão SOC — Detecção de Brute Force SSH (Dia 81)

## 📍 Contexto
Durante a análise automatizada dos logs de autenticação SSH, foi executado o script `detect_bruteforce.sh`, cujo objetivo é identificar IPs com múltiplas falhas de login em curto intervalo de tempo.

O relatório apontou comportamento suspeito compatível com **brute force em SSH**.

---

## 🔎 Evidências Identificadas

- Múltiplas falhas de autenticação (`Failed password`)
- Repetição de tentativas a partir do mesmo IP
- Ataques direcionados a usuários comuns e privilegiados (`root`, `admin`, `test`)
- Alto volume de tentativas em curto período
- Horário suspeito (fora do expediente / madrugada)

### 📌 IP crítico identificado
- **45.77.89.100** — 38 tentativas de login falhas

---

## 🧠 Análise Técnica SOC

Com base nos critérios de segurança e no padrão observado:

- O volume de falhas excede o comportamento esperado de erro humano
- O padrão é típico de script automatizado
- Há risco potencial de comprometimento caso ocorra sucesso posterior

---

## 🚨 Classificação do Incidente

- **Tipo:** Tentativa de Brute Force SSH
- **Severidade:** Média → Alta
- **Confiança:** Alta
- **Status:** Confirmado

---

## 🛡️ Ações Recomendadas

### ✅ Ações imediatas
- Bloqueio do IP atacante no firewall
- Aplicação de rate limit ou regra específica no SSH

### ✅ Ações corretivas
- Ativação ou ajuste do `fail2ban`
- Revisão das políticas de autenticação SSH

### ✅ Ações preventivas
- Desabilitar login direto de root
- Utilizar autenticação por chave SSH
- Monitoramento contínuo de tentativas futuras

---

## 🧾 Conclusão SOC

O incidente foi identificado com sucesso por meio de automação em Bash, demonstrando eficácia na triagem inicial e na resposta rápida a ataques de força bruta.

> **Conclusão:** Brute force SSH confirmado. Ação corretiva aplicada e monitoramento recomendado.

---

**Analista SOC:** Alex  
**Data da análise:** Dia 81
