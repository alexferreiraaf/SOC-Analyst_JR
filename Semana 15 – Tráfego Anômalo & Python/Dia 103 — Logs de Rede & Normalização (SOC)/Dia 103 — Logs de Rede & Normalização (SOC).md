# 📘 Dia 103 — Logs de Rede & Normalização (SOC)

## 🎯 Objetivo
Entender como logs de rede funcionam e como normalizá-los para uso eficiente em SIEM, alertas e correlação.

---

## 🔎 O que são Logs de Rede

Logs de rede mostram:

- Origem (src_ip)
- Destino (dest_ip)
- Portas
- Protocolo
- Ação (allow/deny)
- Volume de dados
- Timestamp

📌 Diferente dos pacotes (detalhe técnico), logs trazem **contexto e escala**.

---

## 🧠 Normalização

Normalizar = padronizar campos para um formato único.

Exemplo:

- `source_ip`, `client_ip` → `src_ip`

Sem normalização:
- Alertas falham
- Correlação quebra
- Dashboards ficam inconsistentes

---

## 🛠 Padrões Importantes

### 🔹 Splunk → CIM
Campos como:
- `src`
- `dest`
- `action`
- `src_port`

### 🔹 Elastic → ECS
Campos como:
- `source.ip`
- `destination.ip`
- `network.transport`
- `event.action`

---

## 🚨 Casos Práticos

- **Port Scan** → mesmo IP acessando várias portas
- **DDoS** → muitos IPs acessando mesmo destino
- **Tráfego normal** → padrão estável e previsível

---

## ✅ Resultado do Dia

Ao final, você:

✔️ Entende estrutura de logs de rede  
✔️ Identifica campos críticos  
✔️ Sabe normalizar eventos  
✔️ Está preparado para criar alertas confiáveis  
✔️ Está pronto para correlação em SIEM  
