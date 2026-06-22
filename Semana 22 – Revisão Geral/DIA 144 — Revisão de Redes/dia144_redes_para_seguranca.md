# DIA 144 — Redes para Segurança

## Objetivo

Revisar conceitos fundamentais de redes aplicados à Segurança da Informação e operações SOC.

---

# Modelo TCP/IP

| Camada     | Função                  | Exemplos         |
| ---------- | ----------------------- | ---------------- |
| Aplicação  | Interação com usuário   | HTTP, HTTPS, DNS |
| Transporte | Comunicação entre hosts | TCP, UDP         |
| Internet   | Endereçamento           | IP, ICMP         |
| Rede       | Transmissão física      | Ethernet         |

---

# Protocolos Importantes

## HTTP

Porta: 80

Utilização:

* Navegação Web

Riscos:

* Malware
* Phishing
* Exploração Web

---

## HTTPS

Porta: 443

Utilização:

* Navegação segura

Riscos:

* Malware escondido em tráfego criptografado

---

## DNS

Porta: 53

Utilização:

* Resolução de nomes

Riscos:

* DNS Tunneling
* Comunicação C2

---

## TCP

Características:

* Confiável
* Orientado à conexão

Handshake:

SYN
SYN-ACK
ACK

---

## UDP

Características:

* Rápido
* Não confiável

Usado por:

* DNS
* VoIP
* Streaming

---

## ICMP

Utilização:

* Diagnóstico de rede

Exemplos:

* Ping
* Traceroute

Possíveis abusos:

* Ping Flood
* Reconhecimento

---

# Portas Críticas

| Porta | Serviço | Risco                      |
| ----- | ------- | -------------------------- |
| 22    | SSH     | Brute Force                |
| 25    | SMTP    | Spam / Phishing            |
| 53    | DNS     | DNS Tunneling              |
| 80    | HTTP    | Ataques Web                |
| 443   | HTTPS   | Malware                    |
| 3389  | RDP     | Acesso Remoto Comprometido |

---

# IP Público vs Privado

## Privados

10.0.0.0/8

172.16.0.0 - 172.31.255.255

192.168.0.0/16

---

## Públicos

Qualquer outro endereço.

Exemplos:

185.223.89.44

8.8.8.8

---

# Comandos Úteis

ip a

ss -tuln

nslookup

ping

traceroute

---

# Indicadores de Ataque

* Brute Force SSH
* DNS Tunneling
* Conexões para IPs suspeitos
* Portas incomuns abertas
* Alto volume de consultas DNS

---

# Resumo

O entendimento de protocolos, portas e endereçamento IP é fundamental para identificar atividades maliciosas em ambientes corporativos e realizar investigações iniciais em um SOC.
