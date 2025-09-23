# 📘 Regex Notes

## 🔹 Metacaracteres básicos
- `.` → qualquer caractere
- `^` → início da string
- `$` → fim da string
- `*` → 0 ou mais repetições
- `+` → 1 ou mais repetições
- `?` → opcional
- `{n,m}` → entre n e m repetições
- `[]` → conjunto de caracteres
- `|` → OU lógico
- `()` → agrupamento

---

## 🔹 Patterns úteis em SOC

### 📧 E-mails
```
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

### 🌐 IPv4
```
(?:[0-9]{1,3}\.){3}[0-9]{1,3}
```

---

✅ Esses padrões são úteis para extrair **e-mails** e **endereços IPv4** em logs de segurança, relatórios ou saídas de comandos.
