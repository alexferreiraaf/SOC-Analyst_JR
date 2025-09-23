# Network Commands Notes

Anotações sobre interpretação de saídas de comandos de rede.

## 1. TTL (Time To Live)
- Campo presente em cabeçalhos IP e em respostas de comandos como `ping`.
- Indica o número máximo de saltos (roteadores) que um pacote pode atravessar antes de ser descartado.
- A cada roteador, o valor de TTL é decrementado em 1.
- Se o TTL chegar a zero, o pacote é descartado e retorna um erro ICMP "Time Exceeded".
- Também pode ser usado para identificar o sistema operacional remoto, pois diferentes SOs usam valores iniciais de TTL (ex.: Windows 128, Linux/Unix 64, Cisco 255).

## 2. Status HTTP
- Códigos numéricos retornados por servidores web quando há uma requisição HTTP/HTTPS.
- Indicam o resultado da requisição:
  - **1xx** – Informacional (ex.: 100 Continue).
  - **2xx** – Sucesso (ex.: 200 OK).
  - **3xx** – Redirecionamento (ex.: 301 Moved Permanently, 302 Found).
  - **4xx** – Erro do cliente (ex.: 404 Not Found, 403 Forbidden).
  - **5xx** – Erro do servidor (ex.: 500 Internal Server Error, 503 Service Unavailable).
- São úteis para diagnosticar problemas de disponibilidade ou configuração em servidores web.

## 3. Resposta DNS
- O DNS (Domain Name System) é responsável por traduzir nomes de domínio (ex.: `google.com`) para endereços IP (ex.: `142.250.190.78`).
- Uma resposta DNS pode conter:
  - **A record (IPv4)** – associa o domínio a um endereço IPv4.
  - **AAAA record (IPv6)** – associa o domínio a um endereço IPv6.
  - **CNAME (Canonical Name)** – redireciona para outro nome de domínio.
  - **MX (Mail Exchange)** – indica servidores de e-mail para o domínio.
  - **NS (Name Server)** – servidores responsáveis pela zona DNS.
- A interpretação da resposta DNS ajuda a verificar se o domínio está resolvendo corretamente e se não há erros de configuração.

---

Essas informações ajudam a interpretar saídas de comandos como `ping`, `tracert/traceroute`, `curl`, `dig` e `nslookup`.
