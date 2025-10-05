# Dia 17 — NAT e VPN

## ⏱️ ~2h30

---

## 🌐 NAT (Network Address Translation)

### Definição
O **NAT** é um mecanismo que permite que múltiplos dispositivos de uma rede privada (endereços IP internos) acessem a Internet usando um único endereço IP público. Ele atua no roteador, traduzindo endereços de origem/destino nos pacotes.

### Tipos de NAT
- **Static NAT**: mapeamento 1:1 entre IP privado ↔ IP público.
- **Dynamic NAT**: mapeamento entre um pool de IPs públicos e privados.
- **PAT (Port Address Translation)**: vários IPs privados compartilham um único IP público, diferenciados pelas portas (conhecido como *NAT overload*).

### Vantagens
- Economia de endereços IPv4.
- Aumento de segurança (endereço interno não visível na Internet).
- Facilita conexões em redes domésticas e pequenas empresas.

### Limitações
- Pode quebrar alguns protocolos que não foram projetados para NAT.
- Aplicações P2P e VoIP podem ter problemas sem configuração extra (STUN, ALG).
- Não substitui firewall.

---

## 🔒 VPN (Virtual Private Network)

### Definição
A **VPN** cria um túnel criptografado entre dois pontos, permitindo que dados trafeguem de forma segura mesmo em redes públicas (como a Internet).

### Protocolos de VPN
- **PPTP**: antigo, rápido, mas inseguro.
- **L2TP/IPSec**: encapsulamento + criptografia.
- **IPSec**: muito usado em empresas, padrão de mercado.
- **OpenVPN**: flexível, seguro, usa SSL/TLS.
- **WireGuard**: moderno, simples, rápido.

### Tipos de VPN
- **Acesso Remoto**: conecta um usuário externo à rede da empresa.
- **Site-to-Site**: conecta filiais diferentes por meio de túneis permanentes.

### Vantagens
- Confidencialidade e integridade dos dados.
- Permite acesso seguro de qualquer lugar.
- Pode reduzir custos com links dedicados.

### Limitações
- Exige configuração e manutenção especializada.
- Consome recursos de criptografia.
- Depende da qualidade da conexão Internet.

---

## 🖥️ Exercício prático

### 1. Cenário NAT no roteador doméstico
- Dispositivos internos (PCs e smartphones) usam IPs privados, ex.: `192.168.1.x`.
- O roteador aplica **PAT**, traduzindo múltiplos IPs privados em **um IP público**.
- Usuários conseguem navegar na Internet sem precisar de IP público individual.

Exemplo:

PC1 (192.168.1.10) → NAT → IP público 200.10.10.5

PC2 (192.168.1.11) → NAT → IP público 200.10.10.5

---

### 2. Cenário VPN site-to-site
- Duas filiais de uma empresa:
  - **Filial A**: 192.168.10.0/24
  - **Filial B**: 192.168.20.0/24
- Um túnel VPN é configurado entre os dois roteadores.
- Usuários da Filial A acessam recursos da Filial B como se estivessem na mesma rede.

Exemplo:

PC_A (192.168.10.5) ↔ VPN ↔ PC_B (192.168.20.8)

## ✅ Reflexão
- O NAT ajuda a manter a Internet IPv4 funcional, mas é apenas uma solução temporária para falta de endereços.
- A VPN complementa a segurança de rede, garantindo privacidade e integridade dos dados.
- Em conjunto, **NAT + VPN** são amplamente utilizados tanto em redes domésticas quanto corporativas.