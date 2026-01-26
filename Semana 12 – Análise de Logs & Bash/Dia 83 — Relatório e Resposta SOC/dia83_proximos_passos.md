# Dia 83 — Próximos Passos (Resposta SOC)

## 🔴 Ação imediata (contenção)

Objetivo: **parar o ataque imediatamente**.

- Bloquear temporariamente os IPs atacantes no firewall ou via `iptables`
- Aplicar bloqueio automático com **fail2ban**, se disponível
- Aumentar o nível de monitoramento do serviço SSH
- Verificar imediatamente se houve **login bem-sucedido após as falhas**

> SOC mindset: conter primeiro, investigar depois.

---

## 🟠 Ação corretiva (mitigação)

Objetivo: **corrigir a fragilidade explorada**.

- Restringir acesso SSH por IP (allowlist)
- Desabilitar login SSH para usuários privilegiados (`root`)
- Forçar autenticação por **chave SSH**
- Revisar logs históricos para tentativas anteriores
- Alterar a porta padrão do SSH (medida complementar)

> SOC mindset: reduzir a superfície de ataque.

---

## 🟢 Ação preventiva (evitar recorrência)

Objetivo: **impedir que o incidente volte a ocorrer**.

- Criar alerta automático para brute force SSH
- Definir threshold claro (ex: >5 falhas em 5 minutos)
- Implementar hardening SSH
- Documentar o incidente e atualizar playbooks SOC
- Treinar usuários e equipe técnica

> SOC mindset: aprender com o incidente.
