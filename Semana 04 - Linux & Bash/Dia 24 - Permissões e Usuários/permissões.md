# 🧩 permissões.md — Exercício Escrito

## 1️⃣ Diferença entre `chmod 777` e `chmod 644`

- `chmod 777` → dá **todas as permissões (leitura, escrita e execução)** para **dono, grupo e outros**.  
  Exemplo: qualquer usuário pode modificar ou excluir o arquivo.

- `chmod 644` → dá **leitura e escrita apenas para o dono**, e **somente leitura para grupo e outros**.  
  Exemplo: apenas o dono pode editar; os demais só conseguem visualizar.

---

## 2️⃣ Qual é o risco de usar `chmod 777`?

Usar `chmod 777` representa um **risco de segurança elevado**, pois qualquer usuário do sistema pode:
- Alterar o conteúdo do arquivo.
- Excluir o arquivo.
- Inserir código malicioso ou scripts executáveis.  
Em servidores, isso pode permitir a **execução de exploits** ou **acesso não autorizado a dados**.

---

## 3️⃣ O que faz o comando:
chown aluno:alunos relatorio.txt

Esse comando altera o **proprietário** e o **grupo** do arquivo `relatorio.txt`.  
- O **novo dono** será o usuário `aluno`.  
- O **novo grupo** será `alunos`.  
Após isso, as permissões passam a ser interpretadas com base nesse novo dono e grupo.

---

## 4️⃣ O que é `rwx` e como interpretar `drwxr-xr--`

- **rwx** representa as três permissões possíveis em arquivos e diretórios:
  - **r (read)** → ler o conteúdo.
  - **w (write)** → modificar o conteúdo.
  - **x (execute)** → executar (ou acessar diretórios).

Exemplo:  
`drwxr-xr--` pode ser lido assim:

| Letra | Significado |
|-------|--------------|
| d | Diretório |
| rwx | Dono pode ler, escrever e executar |
| r-x | Grupo pode ler e executar |
| r-- | Outros podem apenas ler |

Isso indica que apenas o dono tem controle total sobre o diretório.

---

## 5️⃣ Tabela de exemplos

| Permissão | Modo Numérico | Significado | Nível de Segurança |
|------------|----------------|--------------|--------------------|
| rwxr-xr-x | 755 | Todos executam, dono edita | Médio |
| rw-r--r-- | 644 | Somente dono edita | Alto |
| rwxrwxrwx | 777 | Todos fazem tudo | Baixo |
| rw------- | 600 | Apenas dono lê e escreve | Muito alto |
| rwxr-x--- | 750 | Dono total, grupo lê e executa | Alto |
| r--r--r-- | 444 | Todos apenas leem | Alto |

---

📘 **Resumo:**  
Entender permissões é essencial para a segurança em sistemas Linux. Configurar corretamente `chmod` e `chown` evita vazamentos de dados e acessos indevidos.
