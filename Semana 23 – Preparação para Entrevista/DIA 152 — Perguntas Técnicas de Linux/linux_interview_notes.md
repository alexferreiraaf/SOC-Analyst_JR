# Linux Interview Notes

## Navegação e Arquivos

```bash
ls
cd
cp
mv
rm
```

---

## Visualização de Arquivos

```bash
cat
less
head
tail
```

---

## Processos

```bash
ps aux
```

```bash
top
```

```bash
htop
```

---

## Busca

```bash
grep
```

```bash
find
```

---

## Logs Importantes

```bash
/var/log/auth.log
```

```bash
/var/log/syslog
```

```bash
/var/log/kern.log
```

---

## Comandos de Investigação

### Ver usuários logados

```bash
who
```

### Ver falhas SSH

```bash
grep "Failed password" /var/log/auth.log
```

### Ver processos

```bash
ps aux
```

### Ver uso de CPU

```bash
top
```

---

## Perguntas Frequentes

### Como ver processos rodando?

```bash
ps aux
```

### Onde ficam os logs no Linux?

```bash
/var/log/
```

### Como buscar texto em arquivos?

```bash
grep
```

### Qual comando mostra CPU em tempo real?

```bash
top
```

### Como detectar brute force SSH?

Procurando múltiplos eventos "Failed password" no auth.log.
