# Windows Interview Notes

## Event Viewer

Abrir:

```cmd
eventvwr.msc
```

---

## Logs Importantes

| Log         | Função       |
| ----------- | ------------ |
| Security    | Autenticação |
| System      | Sistema      |
| Application | Aplicações   |

---

## Event IDs Importantes

| Event ID | Descrição                   |
| -------- | --------------------------- |
| 4624     | Login com sucesso           |
| 4625     | Login falhou                |
| 4672     | Privilégios administrativos |
| 4688     | Processo criado             |

---

## Investigação

### Filtrar logins falhos

Filtrar Event ID:

```text
4625
```

Analisar:

* Usuário
* Horário
* IP de origem

---

## Perguntas Frequentes

### O que significa Event ID 4625?

Tentativa de login falhou.

### Onde ficam os logs de login?

Windows Logs → Security

### Como detectar brute force?

Grande quantidade de eventos 4625 em curto período.

### O que significa Event ID 4624?

Login realizado com sucesso.

### O que significa Event ID 4672?

Usuário recebeu privilégios especiais ou administrativos.
