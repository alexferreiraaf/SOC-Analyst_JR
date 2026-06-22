# Networking Interview Notes

## Modelo TCP/IP

| Camada         | Função          |
| -------------- | --------------- |
| Application    | HTTP, DNS, SMTP |
| Transport      | TCP, UDP        |
| Internet       | IP              |
| Network Access | Ethernet        |

---

## TCP vs UDP

### TCP

* Orientado à conexão
* Confiável
* Controle de entrega
* Utilizado por:

  * SSH (22)
  * HTTP (80)
  * HTTPS (443)

### UDP

* Sem conexão
* Mais rápido
* Sem garantia de entrega
* Utilizado por:

  * DNS (53)
  * Streaming
  * VoIP

---

## Portas Importantes

| Porta | Serviço |
| ----- | ------- |
| 22    | SSH     |
| 25    | SMTP    |
| 53    | DNS     |
| 80    | HTTP    |
| 443   | HTTPS   |
| 3389  | RDP     |

---

## IPs Privados

* 10.0.0.0/8
* 172.16.0.0 – 172.31.255.255
* 192.168.0.0/16

---

## DNS

DNS (Domain Name System) traduz nomes em endereços IP.

Exemplo:

google.com → 142.250.x.x

---

## Comandos Importantes

### Ver conexões

```bash
ss -tulnp
```

```bash
netstat -tulnp
```

### Testar DNS

```bash
nslookup google.com
```

```bash
dig google.com
```

### Testar conectividade

```bash
ping google.com
```

### Ver rota

```bash
traceroute google.com
```

---

## Perguntas Frequentes

### Qual a diferença entre TCP e UDP?

TCP é confiável e orientado à conexão. UDP é mais rápido, porém não garante entrega.

### O que faz a porta 443?

HTTPS (tráfego web criptografado).

### O que é DNS?

Sistema responsável por resolver nomes em endereços IP.

### O que é traceroute?

Ferramenta que mostra o caminho percorrido pelos pacotes na rede.

### Um servidor recebendo conexões na porta 22 significa o quê?

O serviço SSH está ativo.
