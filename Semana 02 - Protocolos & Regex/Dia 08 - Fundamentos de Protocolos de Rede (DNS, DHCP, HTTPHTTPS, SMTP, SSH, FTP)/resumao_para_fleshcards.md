# Protocolos de Rede — Resumo

| Protocolo | Porta(s) | Função | Comando prático |
|-----------|----------|--------|-----------------|
| **DNS**   | 53 UDP/TCP | Resolver nomes → IP | `nslookup google.com` |
| **DHCP**  | 67/68 UDP  | Entregar IP automático | `ipconfig /renew` |
| **HTTP**  | 80 TCP     | Comunicação web sem criptografia | `curl http://google.com` |
| **HTTPS** | 443 TCP    | Comunicação web segura (TLS) | `curl -I https://google.com` |
| **SMTP**  | 25/465/587 TCP | Enviar e-mails | `telnet smtp.gmail.com 587` |
| **SSH**   | 22 TCP     | Acesso remoto seguro | `ssh user@host` |
| **FTP**   | 21 TCP     | Transferência de arquivos | `ftp ftp.debian.org` |
