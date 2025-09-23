# 📘 Fundamentos de IPv4

### 🔹 O que é um endereço IP?
- **IPv4**: endereço lógico de **32 bits**, dividido em **4 octetos** (0–255).  
  - Exemplo: `192.168.1.10`  

---

### 🔹 Diferença entre IPv4 e IPv6
- **IPv4**  
  - 32 bits → ~4,3 bilhões de endereços  
  - Formato decimal: `192.168.0.1`  
- **IPv6**  
  - 128 bits → número praticamente ilimitado de endereços  
  - Formato hexadecimal: `2001:db8::1`

---

### 🔹 Classes de IP
Embora hoje usemos **CIDR**, é útil conhecer:

| Classe | Intervalo de Endereços | Máscara Padrão | Uso |
| ------ | ---------------------- | -------------- | --- |
| A | 0.0.0.0 – 127.255.255.255 | /8 (255.0.0.0) | Redes muito grandes |
| B | 128.0.0.0 – 191.255.255.255 | /16 (255.255.0.0) | Redes médias |
| C | 192.0.0.0 – 223.255.255.255 | /24 (255.255.255.0) | Redes pequenas |
| D | 224.0.0.0 – 239.255.255.255 | Multicast | Comunicação em grupo |
| E | 240.0.0.0 – 255.255.255.255 | Experimental | Uso futuro |

---

### 🔹 Endereços especiais
- **Rede**: identifica a rede (ex: `192.168.1.0`)  
- **Broadcast**: envia para todos os hosts (ex: `192.168.1.255`)  
- **Loopback**: teste local (`127.0.0.1`)  
- **Privados**:  
  - `10.0.0.0/8`  
  - `172.16.0.0/12`  
  - `192.168.0.0/16`  

---

### 🔹 Máscara de Sub-rede
Define quantos bits pertencem à **rede** e quantos ao **host**.  

| Prefixo | Máscara Decimal | Endereços Totais | Hosts Válidos | Exemplo de Uso |
| ------- | --------------- | ---------------- | ------------- | -------------- |
| /24 | 255.255.255.0 | 256 | 254 | Redes LAN comuns |
| /30 | 255.255.255.252 | 4 | 2 | Links ponto-a-ponto |

---

📌 Esse resumo cobre a base para entender **endereçamento IPv4** e **subnetting**.
