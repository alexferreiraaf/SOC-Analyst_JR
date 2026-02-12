## 🧠 Exercício 3 — Análise de Muitas Conexões Simultâneas

### 🔎 Contagem de conexões por IP (dados fictícios)

| IP remoto | Quantidade de conexões |
|---------|------------------------|
| 8.8.8.8 | 2 |
| 1.1.1.1 | 1 |
| **185.220.101.45** | **3** |
| **45.67.89.10** | **4** |
| 104.244.42.65 | 1 |

---

### 🚨 IPs que dominam o tráfego

- **45.67.89.10**
  - Maior número de conexões
  - Porta 4444
  - Processo desconhecido

- **185.220.101.45**
  - Conexões constantes
  - Porta 9001
  - Processo python

---

### 🧠 Análise SOC

- Muitas conexões para o mesmo IP em curto período:
  - Indica:
    - beaconing
    - C2
    - exfiltração
    - ou malware ativo

---

### 🎯 Conclusão do Exercício 3

📌 IP que domina o tráfego e merece prioridade máxima:

 - 45.67.89.10

yaml
Copiar código

📌 Classificação SOC inicial:

- 45.67.89.10 → 🚨 MALICIOSO (potencial C2)
- 185.220.101.45 → ⚠️ SUSPEITO (monitorar + enriquecer)

---

### 📌 Próximos passos SOC recomendados

- Consultar IPs no VirusTotal
- Identificar binário/processo local
- Avaliar bloqueio em firewall
- Escalar para L2 se confirmado