# 📘 Resumo — Variáveis, Tipos e Operadores

## 🔹 Variáveis

* São usadas para armazenar valores na memória.
* Podem mudar de valor ao longo do programa.

Exemplo:

```python
x = 10      # variável inteira
y = 3.14    # variável float
nome = "Ana" # variável string
```

---

## 🔹 Tipos de Dados Comuns

| Tipo  | Descrição                        | Exemplo              |
| ----- | -------------------------------- | -------------------- |
| int   | Número inteiro                   | `42`                 |
| float | Número decimal (ponto flutuante) | `3.14`               |
| str   | Cadeia de caracteres (texto)     | `"Olá"`              |
| bool  | Valores lógicos                  | `True`, `False`      |
| list  | Lista de valores                 | `[1, 2, 3]`          |
| dict  | Dicionário (pares chave\:valor)  | `{"chave": "valor"}` |
| tuple | Tupla (imutável)                 | `(1, 2, 3)`          |
| set   | Conjunto (valores únicos)        | `{1, 2, 3}`          |

---

## 🔹 Operadores

### Aritméticos

| Operador | Descrição       | Exemplo  | Resultado |
| -------- | --------------- | -------- | --------- |
| `+`      | Adição          | 5 + 3    | 8         |
| `-`      | Subtração       | 5 - 3    | 2         |
| `*`      | Multiplicação   | 5 \* 3   | 15        |
| `/`      | Divisão (float) | 5 / 2    | 2.5       |
| `//`     | Divisão inteira | 5 // 2   | 2         |
| `%`      | Módulo (resto)  | 5 % 2    | 1         |
| `**`     | Exponenciação   | 2 \*\* 3 | 8         |

### Relacionais

| Operador | Descrição      | Exemplo | Resultado |
| -------- | -------------- | ------- | --------- |
| `==`     | Igual a        | 5 == 5  | True      |
| `!=`     | Diferente de   | 5 != 3  | True      |
| `>`      | Maior que      | 5 > 3   | True      |
| `<`      | Menor que      | 3 < 5   | True      |
| `>=`     | Maior ou igual | 5 >= 5  | True      |
| `<=`     | Menor ou igual | 3 <= 5  | True      |

### Lógicos

| Operador | Descrição                                  | Exemplo        | Resultado |
| -------- | ------------------------------------------ | -------------- | --------- |
| `and`    | Verdadeiro se ambos forem verdadeiros      | True and False | False     |
| `or`     | Verdadeiro se pelo menos um for verdadeiro | True or False  | True      |
| `not`    | Inverte o valor lógico                     | not True       | False     |

### Atribuição

| Operador | Exemplo   | Equivalente a |
| -------- | --------- | ------------- |
| `=`      | x = 5     | Atribui valor |
| `+=`     | x += 3    | x = x + 3     |
| `-=`     | x -= 3    | x = x - 3     |
| `*=`     | x \*= 3   | x = x \* 3    |
| `/=`     | x /= 3    | x = x / 3     |
| `//=`    | x //= 3   | x = x // 3    |
| `%=`     | x %= 3    | x = x % 3     |
| `**=`    | x \*\*= 2 | x = x \*\* 2  |
