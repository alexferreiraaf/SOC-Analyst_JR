# 🧠 **Dia 24 — Permissões e Usuários**

⏱️ Duração total: ~2h30

---

## 🎓 **Teoria (40 min)**

### 🔹 Permissões `rwx`
- **r** (read) → leitura do arquivo ou listagem do diretório.  
- **w** (write) → alteração do arquivo ou criação/exclusão dentro do diretório.  
- **x** (execute) → execução de scripts/programas ou acesso ao diretório.

### 🔹 Dono, Grupo e Outros
Cada arquivo ou diretório possui três níveis de permissão:
1. **Dono (user)** — quem criou o arquivo.  
2. **Grupo (group)** — usuários que pertencem ao mesmo grupo.  
3. **Outros (others)** — todos os demais usuários do sistema.

### 🔹 Códigos Numéricos
| Permissão | Binário | Valor |
|------------|----------|--------|
| r (read)   | 100 | 4 |
| w (write)  | 010 | 2 |
| x (execute)| 001 | 1 |

Exemplo:
- `chmod 755` → dono (7 = rwx), grupo (5 = r-x), outros (5 = r-x)
- `chmod 644` → dono (6 = rw-), grupo (4 = r--), outros (4 = r--)

### 🔹 Criação e gerenciamento de usuários
- `whoami` → mostra o usuário atual.  
- `id` → exibe UID, GID e grupos.  
- `adduser nome` → cria um novo usuário.  
- `passwd nome` → altera a senha.  
- `deluser nome` → remove um usuário.

---

## 🧩 **Prática (50 min)**

### 🔸 Comandos utilizados:
```bash
whoami
id
ls -l
chmod 755 script.sh
chmod 644 relatorio.txt
chown aluno:alunos relatorio.txt
```

### 📸 **Prints simulados do terminal**
```
$ whoami
aluno

$ id
uid=1000(aluno) gid=1000(aluno) grupos=1000(aluno),27(sudo)

$ ls -l relatorio.txt
-rw-r--r-- 1 aluno alunos 230 out 11 10:15 relatorio.txt

$ chmod 755 script.sh
$ ls -l script.sh
-rwxr-xr-x 1 aluno alunos 124 out 11 10:20 script.sh
```

---

## ✍️ **Exercício Escrito — permissoes.md**

1. Diferença entre `chmod 777` e `chmod 644`.  
   → O `777` dá permissão total para todos; o `644` só permite que o dono edite.

2. Risco de usar `chmod 777`.  
   → Qualquer usuário pode modificar e apagar o arquivo.

3. Explicação do comando:
   ```bash
   chown aluno:alunos relatorio.txt
   ```
   → Muda o dono do arquivo para *aluno* e o grupo para *alunos*.

4. Significado de `rwx` e exemplo de `drwxr-xr--`.  
   → O `rwx` mostra leitura, escrita e execução.  
   `drwxr-xr--` → diretório onde o dono tem acesso total, grupo apenas leitura/execução e outros apenas leitura.

5. Tabela de exemplos:
| Permissão  | Numérico | Significado | Segurança |
|-------------|-----------|-------------|-------------|
| rwxr-xr-x | 755 | Todos executam, dono edita | Médio |
| rw-r--r-- | 644 | Somente dono edita | Alto |
| rwxrwxrwx | 777 | Todos fazem tudo | Baixo |

---

## ⚙️ **Script Bash — mudar_permissoes.sh**

```bash
#!/bin/bash
# Script: mudar_permissoes.sh
# Objetivo: alterar permissões de um arquivo para 644

if [ -z "$1" ]; then
    echo "Uso: $0 <nome_do_arquivo>"
    exit 1
fi

echo "🔹 Permissões atuais:"
ls -l "$1"

chmod 644 "$1"

echo "🔹 Novas permissões:"
ls -l "$1"
```

### 🧪 **Execução de exemplo**
```
$ ./mudar_permissoes.sh relatorio.txt
🔹 Permissões atuais:
-rwxrwxrwx 1 aluno alunos 230 out 11 10:45 relatorio.txt

🔹 Novas permissões:
-rw-r--r-- 1 aluno alunos 230 out 11 10:45 relatorio.txt
```

---

✅ **Conclusão:**  
Compreendemos como funcionam permissões no Linux, a diferença entre `chmod` numérico e simbólico, e como gerenciar usuários e grupos de forma segura.
