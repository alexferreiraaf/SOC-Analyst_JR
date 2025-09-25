# Protocolos de Rede — Resumo Detalhado

| Protocolo | Porta(s) | Função (resumo) |
|-----------|----------|-----------------|
| **DNS** | 53 (UDP/TCP) | Tradução de nomes em IPs (resolução de nomes). |
| **DHCP** | 67 (server) / 68 (client) UDP | Atribuição automática de IP, máscara, gateway e DNS. |
| **HTTP** | 80 TCP | Transferência de páginas web sem criptografia. |
| **HTTPS** | 443 TCP | HTTP sobre TLS — web segura (certificados). |
| **SMTP** | 25 / 465 / 587 TCP | Envio de emails (587 com STARTTLS, 465 SMTPS). |
| **IMAP** | 143 / 993 TCP | Recebimento de e-mail (993 é IMAP sobre TLS). |
| **POP3** | 110 / 995 TCP | Recebimento de e-mail (995 é POP3 sobre TLS). |
| **SSH** | 22 TCP | Acesso remoto seguro (shell remoto, SFTP). |
| **FTP** | 21 TCP (control) | Transferência de arquivos (inseguro); SFTP usa SSH. |
| **DNS-over-HTTPS (DoH)** | 443 TCP | Resolução DNS via HTTPS (privacidade). |
