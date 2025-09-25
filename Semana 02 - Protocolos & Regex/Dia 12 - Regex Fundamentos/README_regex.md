# Guia de Expressões Regulares (Regex)

Este guia reúne os **principais metacaracteres**, exemplos práticos e observações importantes para o uso de regex no dia a dia.

---

## 🔑 Metacaracteres principais

| Metacaractere | Função |
|---------------|--------|
| `.` | Corresponde a **qualquer caractere** (exceto quebra de linha). |
| `^` | Corresponde ao **início da linha/string**. |
| `$` | Corresponde ao **final da linha/string**. |
| `*` | Repete o elemento **0 ou mais vezes**. |
| `+` | Repete o elemento **1 ou mais vezes**. |
| `?` | Torna o elemento **opcional** (0 ou 1 vez). |
| `{n}` | Repete o elemento **exatamente n vezes**. |
| `{n,}` | Repete o elemento **n ou mais vezes**. |
| `{n,m}` | Repete o elemento **entre n e m vezes**. |
| `[]` | Define um **conjunto de caracteres permitidos**. |
| `[^ ]` | Define um **conjunto negado** (caracteres não permitidos). |
| `\d` | Qualquer **dígito** (0–9). |
| `\D` | Qualquer caractere **não numérico**. |
| `\w` | Qualquer caractere de palavra (letras, dígitos, `_`). |
| `\W` | Qualquer caractere que **não** seja `\w`. |
| `\s` | Qualquer espaço em branco (tab, espaço, quebra de linha). |
| `\S` | Qualquer caractere que **não** seja espaço em branco. |
| `|` | Operador **OU** (ex.: `cão|gato`). |
| `()` | Define **grupo de captura**. |
| `(?: )` | Define **grupo sem captura**. |

---

## 💻 Exemplos práticos

### 1. Encontrar e-mails
```bash
echo "contato@exemplo.com" | grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}"
```
**Saída:**
```
contato@exemplo.com
```

---

### 2. Encontrar números de telefone (formato brasileiro simples)
```bash
echo "(11) 99999-8888" | grep -E "\([0-9]{2}\) [0-9]{4,5}-[0-9]{4}"
```
**Saída:**
```
(11) 99999-8888
```

---

### 3. Validar endereços IPv4 (simplificado)
```bash
echo "192.168.1.100" | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}"
```
**Saída:**
```
192.168.1.100
```

---

## ⚠️ Observações Importantes

- Regex **não valida ranges numéricos complexos**:
  - O exemplo de IP acima aceita valores como `999.999.999.999`.  
  - Para validações rigorosas, é necessário lógica extra (ex.: scripts, bibliotecas).
- Usar regex **apenas quando necessário** — muitas vezes, funções nativas da linguagem são mais rápidas e seguras.
- Regex pode variar entre implementações (POSIX, PCRE, Python `re`, etc.).

---

📌 **Resumo:**  
Regex é uma ferramenta poderosa para **busca, extração e validação de padrões** em strings.  
Sempre teste suas expressões em casos reais antes de usá-las em produção.
