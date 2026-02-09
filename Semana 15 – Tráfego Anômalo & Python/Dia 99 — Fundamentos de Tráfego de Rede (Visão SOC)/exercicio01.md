## 🧠 Exercício 1 — Identificação de IPs Externos (Dados Fictícios)

### 🔎 Cenário simulado

Saída fictícia baseada no comando `ss -tunap` com tráfego misto (normal + suspeito):

- Conexões observadas:
  - 192.168.1.10 → 8.8.8.8:443
  - 192.168.1.10 → 8.8.8.8:443
  - 192.168.1.10 → 1.1.1.1:53
  - 192.168.1.10 → 185.220.101.45:9001
  - 192.168.1.10 → 185.220.101.45:9001
  - 192.168.1.10 → 185.220.101.45:9001
  - 192.168.1.10 → 104.244.42.65:443

---

### 📌 Identificação de IPs externos

IPs que **não pertencem à rede local (192.168.x.x)**:

- 8.8.8.8
- 1.1.1.1
- 185.220.101.45
- 104.244.42.65

---

### 🔁 IPs que se repetem

| IP Externo | Quantidade de conexões |
|-----------|------------------------|
| 8.8.8.8 | 2 |
| 1.1.1.1 | 1 |
| **185.220.101.45** | **3** |
| 104.244.42.65 | 1 |

---

### 🚨 Análise SOC

- **8.8.8.8** → DNS Google → tráfego esperado
- **1.1.1.1** → DNS Cloudflare → tráfego esperado
- **104.244.42.65** → HTTPS comum (possível CDN ou serviço web)
- **185.220.101.45**:
  - IP externo desconhecido
  - Porta incomum (9001)
  - Alta repetição
  - Frequência constante

---

### 🧠 Conclusão SOC

📌 **IP que merece investigação prioritária:**

  - 185.220.101.45

  
📌 **Motivos:**
- IP externo não conhecido
- Porta incomum
- Repetição em curto intervalo
- Possível padrão de beaconing

---

### 🎯 Próxima ação SOC recomendada

- Consultar o IP no VirusTotal
- Verificar processo associado
- Monitorar frequência
- Avaliar bloqueio preventivo

Classificação inicial: **⚠️ SUSPEITO**
