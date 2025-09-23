# 📅 Dia 1 – Visão geral: Modelo OSI + mapeamento TCP/IP

⏱ Total: ~2h

---

## 📖 Modelo OSI – 7 camadas

1. **Física**: meio físico (cabo, Wi-Fi, fibra), transmissão de bits (0 e 1).
   - Unidade: **bits**
   - Exemplos: cabo Ethernet, repetidor, hub.

2. **Enlace de Dados (Data Link)**: endereçamento **MAC**, controle de erros, **frames**, switches, protocolo **ARP** (resolve IP → MAC).
   - Unidade: **quadros (frames)**
   - Exemplo: Switch, Ethernet, PPP.

3. **Rede (Network)**: endereçamento **IP**, roteamento, encapsula pacotes.
   - Unidade: **pacotes**
   - Exemplo: Roteador, IPv4/IPv6, ICMP.

4. **Transporte (Transport)**: comunicação de ponta a ponta, **TCP (confiável)** vs **UDP (rápido)**.
   - Unidade: **segmentos** (TCP) ou **datagramas** (UDP).
   - Exemplo: TCP (handshake 3 vias), UDP (streaming).

5. **Sessão (Session)**: gerenciamento de sessões, login, abertura/fechamento de conexões, TLS.
   - Exemplos: protocolos de sessão, autenticação de usuários.

6. **Apresentação (Presentation)**: tradução, criptografia, compressão.
   - Exemplos: TLS/SSL, codificação JPEG, ASCII.

7. **Aplicação (Application)**: onde os aplicativos se comunicam.
   - Exemplos: HTTP, HTTPS, DNS, SMTP, FTP, SSH.

---

## 📖 Modelo TCP/IP – 4 camadas

1. **Acesso à Rede (Network Access)** = Física + Enlace.
2. **Internet** = Camada de Rede (IP, ICMP).
3. **Transporte** = TCP/UDP.
4. **Aplicação** = Sessão + Apresentação + Aplicação (HTTP, DNS, SMTP, SSH).

---

## 📝 Tabela comparativa OSI vs TCP/IP

| **Camada OSI** | **TCP/IP**    | **Exemplos**                   |
| -------------- | ------------- | ------------------------------ |
| Física         | Acesso à Rede | Cabo Ethernet, Wi-Fi, hub      |
| Enlace         | Acesso à Rede | Switch, MAC, ARP               |
| Rede           | Internet      | IP, ICMP, roteador             |
| Transporte     | Transporte    | TCP (porta 80), UDP (porta 53) |
| Sessão         | Aplicação     | Login, TLS handshake           |
| Apresentação   | Aplicação     | SSL/TLS, codificação Base64    |
| Aplicação      | Aplicação     | HTTP, HTTPS, DNS, SMTP, SSH    |

---

## 🎯 Mini-quiz + Flashcards

1. Em qual camada OSI funciona o **ARP**? → Camada 2 (Enlace).
2. Qual é a unidade de dados da Camada de Rede? → Pacote.
3. Em qual camada TCP/IP está o **ICMP**? → Internet.
4. TCP e UDP pertencem a qual camada OSI? → Camada 4 (Transporte).
5. Porta 80 está em qual camada OSI? → Camada 7 (Aplicação), mas usa TCP na camada 4.

(Complete até 10 flashcards no Anki ou Notion).

---

## ✍️ Reflexão prática

**Como eu, como SOC Júnior, uso o Modelo OSI para investigar um incidente?**

Exemplo de resposta:

Se um alerta no SIEM mostra várias tentativas na porta 22 (SSH), eu olho:

- **Camada de Aplicação**: qual protocolo? (SSH).
- **Transporte**: é TCP, porta 22.
- **Rede**: quais IPs de origem/destino?
- **Enlace**: MAC, se for rede interna.

Isso me ajuda a entender se é um ataque de brute force ou apenas falhas de autenticação legítimas.

---

## 📌 Resultado esperado do Dia 1

- Sei descrever cada camada OSI e TCP/IP.
- Tenho uma tabela comparativa pronta.
- Criei flashcards para revisar.
- Escrevi uma reflexão prática com aplicação no SOC.
