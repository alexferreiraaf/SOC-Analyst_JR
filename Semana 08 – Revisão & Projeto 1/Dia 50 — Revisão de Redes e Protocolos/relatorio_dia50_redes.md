# Relatório Técnico: Revisão de Redes e Protocolos (Dia 50)
**Data:** 19 de Novembro de 2025
**Assunto:** Análise de Camadas OSI, Diagnóstico de Rede e Captura de Tráfego

## 1. O Modelo OSI e Ferramentas de Monitoramento
O Modelo OSI (Open Systems Interconnection) divide a comunicação de rede em 7 camadas lógicas. Para um Analista de SOC, entender em qual camada um ataque ou falha está ocorrendo é vital para a resposta ao incidente.



Abaixo, o detalhamento das camadas e as ferramentas/protocolos aplicáveis para monitoramento:

| Camada (OSI) | Função Principal | Protocolos Típicos | Ferramenta/Filtro de Análise (SOC) |
| :--- | :--- | :--- | :--- |
| **7. Aplicação** | Interface com o usuário final e serviços de rede. | HTTP, DNS, SSH, FTP | **Wireshark:** `http`, `dns` <br> **Logs:** IIS/Apache logs, Syslog. |
| **6. Apresentação** | Tradução de dados, criptografia e compressão. | SSL/TLS, JPEG, ASCII | **Wireshark:** Análise de Handshake TLS (`ssl.handshake`). |
| **5. Sessão** | Estabelecimento e gerenciamento de sessões. | RPC, NetBIOS, SMB | **Firewall:** Logs de duração de sessão. |
| **4. Transporte** | Controle de fluxo, correção de erros e portas. | TCP, UDP | **Nmap:** Scan de portas. <br> **Tcpdump:** `tcp port 80`. |
| **3. Rede** | Endereçamento lógico (IP) e roteamento. | IPv4, IPv6, ICMP | **Traceroute**, **Ping**. <br> **Wireshark:** `ip.src`, `ip.dst`. |
| **2. Enlace** | Endereçamento físico (MAC) e acesso ao meio. | Ethernet, ARP, VLAN | **Wireshark:** `eth.addr`, `arp`. <br> **Switch:** Logs de Port Security. |
| **1. Física** | Transmissão de bits brutos (sinais elétricos/luz). | Cabos (UTP/Fibra), Wi-Fi | **Testadores de cabo**, Verificação de LED nas interfaces. |

---

## 2. Análise Comparativa: TCP vs. UDP

### Diferença Fundamental
* **TCP (Transmission Control Protocol):** Orientado a conexão. Garante que os dados cheguem na ordem correta e sem erros.
* **UDP (User Datagram Protocol):** Não orientado a conexão ("fire and forget"). Envia dados sem verificar se o receptor está pronto ou se o pacote chegou.

### 🧩 Desafio: Por que o UDP é favorito em ataques DDoS?
O UDP é frequentemente utilizado em ataques de Negação de Serviço (DDoS), especificamente em ataques de **Amplificação e Reflexão**, pelos seguintes motivos:
1.  **Sem Handshake:** O atacante não precisa estabelecer uma conexão real (não precisa fazer o 3-way handshake), o que consome menos recursos da máquina atacante.
2.  **Spoofing Fácil:** Como não há verificação de conexão, é trivial falsificar o endereço IP de origem (IP Spoofing). O atacante envia uma requisição UDP fingindo ser a vítima.
3.  **Fator de Amplificação:** Protocolos baseados em UDP (como DNS e NTP) muitas vezes devolvem respostas muito maiores do que a pergunta. O atacante envia uma pergunta pequena (ex: 64 bytes) e a vítima recebe uma resposta gigante (ex: 3000 bytes), saturando o link.

---

## 3. Análise Avançada: O 3-Way Handshake

Ao analisar o tráfego TCP no Wireshark (filtro `tcp.flags.syn == 1 || tcp.flags.ack == 1`), o processo de estabelecimento de conexão confiável ocorre em três etapas:



[Image of TCP 3-way handshake diagram]


1.  **SYN (Synchronize):** O cliente (origem) envia um pacote com a flag SYN ativada para o servidor, indicando "Quero iniciar uma conexão" e definindo um número de sequência inicial.
2.  **SYN-ACK (Synchronize-Acknowledge):** O servidor recebe o SYN, e se a porta estiver aberta, responde com um pacote contendo as flags SYN e ACK. Isso significa "Recebi seu pedido (ACK) e também quero conectar (SYN)".
3.  **ACK (Acknowledge):** O cliente recebe o pacote do servidor e envia um pacote final com a flag ACK. A conexão está **ESTABLISHED** (estabelecida) e a transferência de dados pode começar.

---

## 4. Resultados do Laboratório Prático (Espaço para Prints/Dados)

### Diagnóstico de Conectividade
* **Latência Média (Google):** `13.2ms`
* **Perda de Pacotes:** `0%`

### Roteamento (Traceroute)
* **Total de Saltos até Cloudflare:** `9`
* **IPs Intermediários Notáveis:** `192.168.5.1, 10.88.88.2, 192.168.204.20, 45.238.98.12, 172.168.16.115, 172.168.16.103, 104.16.124.96`

### Portas Abertas (Netstat)
* **Portas "Listening" identificadas:** `151, 32, 4096, 128, 70, 64`
* **Processos suspeitos?** `Não`

### Análise de Captura (.pcap)
* **Total de pacotes ICMP capturados:** `32`
* **IP mais frequente na captura:** `8.8.8.8`
* **Houve retransmissão TCP?** `Não`