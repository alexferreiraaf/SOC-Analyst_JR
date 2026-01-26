## 📄 dia86_eventids_windows.md

### 🔑 Principais Event IDs do Windows para SOC

| Event ID | Origem   | Descrição                               | Uso em SOC                                 |
| -------: | -------- | --------------------------------------- | ------------------------------------------ |
|     4624 | Security | Logon bem-sucedido                      | Identificar acessos legítimos ou suspeitos |
|     4625 | Security | Falha de logon                          | Detecção de brute force                    |
|     4634 | Security | Logoff                                  | Análise de sessões                         |
|     4648 | Security | Logon com credenciais explícitas        | Uso suspeito de credenciais                |
|     4672 | Security | Privilégios administrativos atribuídos  | Escalada de privilégio                     |
|     4688 | Security | Criação de processo                     | Execução suspeita                          |
|     4697 | Security | Serviço instalado                       | Persistência                               |
|     4703 | Security | Alteração de privilégios                | Manipulação de permissões                  |
|     4719 | Security | Alteração de política de auditoria      | Tentativa de evasão                        |
|     4720 | Security | Criação de usuário                      | Conta suspeita                             |
|     4728 | Security | Usuário adicionado a grupo privilegiado | Elevação de acesso                         |
|     4732 | Security | Alteração em grupo local                | Movimento lateral                          |
|     4768 | Security | Ticket Kerberos (TGT)                   | Ataques Kerberos                           |
|     4769 | Security | Ticket de serviço Kerberos              | Pass-the-Ticket                            |
|     4776 | Security | Validação de credenciais                | Ataques NTLM                               |

---

