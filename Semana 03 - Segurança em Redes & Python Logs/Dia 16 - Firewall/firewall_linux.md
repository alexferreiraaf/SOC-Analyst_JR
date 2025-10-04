# Firewall no Linux (UFW)

## 1. Status inicial
```bash
sudo ufw status

Saída esperada (inicial):
Status: inactive

2. Ativar firewall
sudo ufw enable

Saída esperada:
Firewall is active and enabled on system startup

3. Configuração de regras
sudo ufw allow 22/tcp
sudo ufw deny 80/tcp
sudo ufw allow icmp

Saída após regras aplicadas:
Rules updated
Rules updated (v6)

4. Verificação
sudo ufw status verbose

Saída esperada:
22/tcp    ALLOW    Anywhere
80/tcp    DENY     Anywhere
ICMP      ALLOW    Anywhere

## 5. Testes de conectividade

- **Ping (ICMP)**
ping -c 4 8.8.8.8

*Deve funcionar (ICMP liberado).*

- **Curl (HTTP bloqueado)**
curl http://example.com

*Deve falhar, porta 80 bloqueada.*

- **SSH (permitido)**
ssh usuario@servidor
Deve conectar normalmente.

Criar regra para bloquear HTTP
netsh advfirewall firewall add rule name="Bloquear HTTP" dir=out action=block protocol=TCP localport=80

Saída esperada:
Ok.

Listar regras
netsh advfirewall firewall show rule name=all

## 4. Teste prático

- Acessar `http://example.com` → deve falhar (bloqueio HTTP).
- Acessar `https://example.com` → deve funcionar (HTTPS liberado).

*Print esperado:* tela do navegador com falha de conexão ao tentar acessar site **HTTP**.
---

### 📄 `regras_firewall.md`
```markdown
# Tabela de Regras — Firewall (Dia 16)

| Ambiente | Regra           | Ação     | Justificativa                        |
|----------|-----------------|----------|--------------------------------------|
| Linux    | allow 22/tcp    | Permitir | SSH remoto para administração        |
| Linux    | deny 80/tcp     | Bloquear | Proteger contra tráfego HTTP inseguro|
| Linux    | allow icmp      | Permitir | Testes básicos de conectividade      |
| Windows  | block TCP/80    | Bloquear | Evitar tráfego web não criptografado |
| Windows  | default allow https | Permitir | Garantir navegação segura          |

