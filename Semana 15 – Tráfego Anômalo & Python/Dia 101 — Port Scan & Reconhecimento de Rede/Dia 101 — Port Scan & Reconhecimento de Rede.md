# 📅 Dia 101 — Port Scan & Reconhecimento de Rede

## 🎯 Objetivo
Entender como ataques de **reconhecimento** acontecem, como aparecem nos logs/tráfego e como um SOC identifica um **port scan antes da exploração**.

---

## 🔎 Conceitos Principais

### 🔹 Reconhecimento
Fase inicial de quase todo ataque.  
O atacante busca descobrir:
- IPs ativos
- Portas abertas
- Serviços
- Versões
- Sistema operacional

SOC pergunta:
> “Alguém está mapeando minha superfície de ataque?”

---

### 🔹 Port Scan
Teste automatizado de múltiplas portas para identificar serviços expostos.

Resultado possível:
- Aberta
- Fechada
- Filtrada

---

## 🚨 Tipos Comuns de Scan

- **TCP Connect Scan** → conexão completa (barulhento)
- **SYN Scan (half-open)** → mais furtivo (muitos SYN, poucos ESTAB)
- **UDP Scan** → UDP sem resposta / ICMP excessivo
- **Scan distribuído** → vários IPs testando poucos ports

---

## 📊 Comportamento Suspeito

| Normal | Port Scan |
|--------|-----------|
| Poucas portas | Muitas portas |
| Intervalo regular | Muito rápido |
| Acesso específico | Sequencial |
| Origem conhecida | Externa/desconhecida |

Port scan é **padrão repetitivo**, não evento isolado.

---

## 🧠 Indicadores SOC

- Muitas portas em segundos
- Muitos `SYN` sem `ESTAB`
- Tentativas em portas incomuns
- Mesmo IP testando múltiplos serviços

---

## 🛡 Resposta SOC

1. Classificar (interno/externo, rápido/lento)
2. Coletar evidências
3. Decidir: monitorar, alertar, bloquear ou escalar

🚨 Escalonar imediatamente se envolver:
- SSH (22)
- RDP (3389)
- Banco de dados
- Infraestrutura crítica

---

## ✅ Resultado Esperado

Ao final do dia você deve:
- Reconhecer port scan pelo comportamento
- Diferenciar scan rápido, lento e distribuído
- Entender como SOC detecta recon antes do ataque
- Saber quando monitorar e quando gerar alerta
