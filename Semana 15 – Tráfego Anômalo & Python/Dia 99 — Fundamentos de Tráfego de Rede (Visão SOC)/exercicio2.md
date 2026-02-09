## 🧠 Exercício 2 — Identificação de Portas Incomuns (Dados Fictícios)

### 🔎 Cenário simulado

Conexões observadas (base fictícia):

- 192.168.1.10 → 8.8.8.8:443 (chrome)
- 192.168.1.10 → 1.1.1.1:53 (systemd-resolved)
- 192.168.1.10 → 185.220.101.45:9001 (python)
- 192.168.1.10 → 185.220.101.45:9001 (python)
- 192.168.1.10 → 185.220.101.45:9001 (python)
- 192.168.1.10 → 45.67.89.10:4444 (unknown)
- 192.168.1.10 → 104.244.42.65:443 (chrome)

---

### 📌 Portas consideradas normais (baseline)

- 22 → SSH
- 80 → HTTP
- 443 → HTTPS
- 53 → DNS

---

### 🚨 Portas incomuns identificadas

| Porta | IP remoto | Processo local | Observação SOC |
|-----|----------|---------------|----------------|
| **9001** | 185.220.101.45 | python | Porta incomum, repetição alta |
| **4444** | 45.67.89.10 | unknown | Porta clássica de C2 / backdoor |

---

### 🧠 Análise SOC

- **Porta 9001**
  - Não é porta padrão
  - Associada a processo `python`
  - Comunicação repetitiva
  - Forte indicativo de beaconing

- **Porta 4444**
  - Muito usada por:
    - backdoors
    - shells reversos
    - C2
  - Processo desconhecido
  - Alta prioridade SOC

---

### 🎯 Conclusão do Exercício 2

📌 Portas que exigem investigação imediata:

  - 9001
  - 4444

  Classificação inicial:
- 9001 → ⚠️ Suspeita
- 4444 → 🚨 Altamente suspeita / potencialmente maliciosa