# Dia 102 — Captura de Tráfego com tcpdump e Wireshark

## 🎯 Objetivo
Aprender a capturar, filtrar e analisar pacotes de rede para identificar:
- Reconhecimento (Port Scan)
- Brute Force
- Comportamentos suspeitos
- Ataques iniciais

---

## 📘 Conceito Central

- **Logs mostram o que aconteceu**
- **Pacotes mostram como aconteceu**

SOC usa captura de tráfego para:
- Validar alertas
- Coletar evidências
- Entender o comportamento real do ataque

---

## 🛠 Ferramentas

### 🔹 tcpdump
Uso em servidores e ambientes reais (CLI)

Principais comandos:
- `tcpdump -i eth0`
- `tcpdump -i eth0 tcp`
- `tcpdump -i eth0 port 22`
- `tcpdump -i eth0 -w captura.pcap`

Detectar SYN:
- `tcp[tcpflags] & tcp-syn != 0`


---

### 🔹 Wireshark
Uso para análise visual e investigação profunda.

Filtros essenciais:
- `tcp`
- `tcp.flags.syn == 1 && tcp.flags.ack == 0`
- `tcp.port == 22`
- `dns`
- `icmp`

Recursos importantes:
- Statistics → Conversations
- Statistics → Flow Graph

---

## 🚨 O que o SOC identifica

### Port Scan
- Muitos SYN
- Portas variadas
- Sem handshake completo

### Brute Force SSH
- Conexões repetidas
- Porta 22
- Intervalos curtos

### Tráfego Normal
- Handshake completo
- Conexões estáveis
- Portas comuns

---

## ✅ Resultado do Dia

Ao final do dia você:
- Usa tcpdump com filtros estratégicos
- Salva evidências em `.pcap`
- Analisa tráfego no Wireshark
- Identifica recon e brute force
- Explica tecnicamente um ataque em entrevista
