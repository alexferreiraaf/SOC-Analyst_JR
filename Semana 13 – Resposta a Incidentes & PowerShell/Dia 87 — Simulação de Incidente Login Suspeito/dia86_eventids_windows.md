# Event IDs Importantes do Windows (SOC)

## 🔐 Autenticação e Logon

- **4624** — Logon bem-sucedido  
- **4625** — Falha de logon (senha incorreta, usuário inexistente, brute force)
- **4634** — Logoff
- **4648** — Logon usando credenciais explícitas
- **4672** — Logon com privilégios administrativos

## 👤 Contas de Usuário

- **4720** — Conta criada
- **4722** — Conta habilitada
- **4723** — Tentativa de alteração de senha
- **4725** — Conta desabilitada
- **4726** — Conta excluída

## 🛡️ Segurança e Políticas

- **4719** — Política de auditoria alterada
- **4732** — Usuário adicionado a grupo privilegiado
- **4733** — Usuário removido de grupo privilegiado

## 🚨 Uso no SOC

Esses eventos são usados para:
- Detectar brute force
- Identificar movimentação lateral
- Monitorar abuso de privilégios
- Investigar comprometimento de contas
