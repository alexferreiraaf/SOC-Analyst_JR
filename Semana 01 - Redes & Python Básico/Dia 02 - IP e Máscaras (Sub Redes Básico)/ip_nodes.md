Aqui está um **resumo organizado** para sua leitura dirigida sobre Fundamentos de IPv4:
# 📘 Fundamentos de IPv4

### 🔹 O que é um endereço IP?

* **IPv4**: endereço lógico de **32 bits**, dividido em **4 octetos** (0–255).

  * Exemplo: `192.168.1.10`

---

### 🔹 Diferença entre IPv4 e IPv6

* **IPv4**

  * 32 bits → \~4,3 bilhões de endereços
  * Formato decimal: `192.168.0.1`
* **IPv6**

  * 128 bits → número praticamente ilimitado de endereços
  * Formato hexadecimal: `2001:db8::1`

---

### 🔹 Classes de IP

Embora hoje usemos **CIDR**, é útil conhecer:

* **Classe A**: `0.0.0.0 – 127.255.255.255` (rede grande, /8)
* **Classe B**: `128.0.0.0 – 191.255.255.255` (médio porte, /16)
* **Classe C**: `192.0.0.0 – 223.255.255.255` (pequenas redes, /24)
* **Classe D**: `224.0.0.0 – 239.255.255.255` (multicast)
* **Classe E**: `240.0.0.0 – 255.255.255.255` (experimental)

---

### 🔹 Endereços especiais

* **Rede**: identifica a rede (ex: `192.168.1.0`)
* **Broadcast**: envia para todos os hosts (ex: `192.168.1.255`)
* **Loopback**: teste local (`127.0.0.1`)
* **Privados**:

  * `10.0.0.0/8`
  * `172.16.0.0/12`
  * `192.168.0.0/16`

---

### 🔹 Máscara de Sub-rede

Define quantos bits pertencem à **rede** e quantos ao **host**.

* **Exemplo /24** → `255.255.255.0`

  * Total: 256 endereços
  * Hosts válidos: 254 (`.1` a `.254`)
* **Exemplo /30** → `255.255.255.252`

  * Total: 4 endereços
  * Hosts válidos: 2 (`.1` e `.2`)
