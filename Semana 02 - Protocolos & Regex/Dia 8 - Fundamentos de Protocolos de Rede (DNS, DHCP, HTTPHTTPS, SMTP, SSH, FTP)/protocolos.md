# Protocolos — resumo e comandos de teste

| Protocolo | Porta(s) | Uso | Comando para testar |
|-----------|---------:|-----|---------------------|
| DNS       | 53 (UDP/TCP) | Resolução de nomes para IP | `nslookup google.com` / `dig google.com` |
| DHCP      | 67/68 UDP | Atribuição automática de IP/máscara/gateway/DNS | `dhclient -v` (Linux) / `ipconfig /renew` (Windows) |
| HTTP      | 80 TCP | Transferência de páginas web sem criptografia | `curl http://example.com` |
| HTTPS     | 443 TCP | HTTP sobre TLS — web segura | `curl -I https://example.com` |
| SMTP      | 25 / 465 / 587 TCP | Envio de e-mails (587 = STARTTLS) | `telnet smtp.gmail.com 587` ou `openssl s_client -starttls smtp -connect smtp.gmail.com:587` |
| SSH       | 22 TCP | Acesso remoto seguro e SFTP | `ssh user@host` / `ssh -v user@host` |
| FTP       | 21 TCP (control) | Transferência de arquivos (inseguro) | `ftp ftp.debian.org` ou `lftp` |
| IMAP      | 143 / 993 TCP | Recebimento de e-mails (993 = IMAP TLS) | testar cliente ou `openssl s_client -connect imap.example.com:993` |
| POP3      | 110 / 995 TCP | Recebimento de e-mails (995 = POP3 TLS) | `openssl s_client -connect pop3.example.com:995` |
