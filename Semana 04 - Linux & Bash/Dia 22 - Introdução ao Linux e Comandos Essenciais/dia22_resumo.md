# 🐧 Dia 22 — Introdução ao Linux e Comandos Essenciais

## 📘 Resumo Teórico

Neste dia, foi feita a introdução ao sistema operacional **Linux**, com foco na estrutura de diretórios, permissões, comandos básicos e operação via terminal.

### 🔹 Tópicos estudados

- **Estrutura de diretórios**:
  - `/` → raiz do sistema.
  - `/home` → pastas dos usuários.
  - `/etc` → arquivos de configuração.
  - `/var` → logs e dados variáveis.
  - `/usr` → programas e bibliotecas do sistema.

- **Conceitos fundamentais**:
  - **root** → superusuário com permissões totais.
  - **usuário comum** → acesso limitado.
  - **kernel** → núcleo do sistema.
  - **shell** → interface entre o usuário e o kernel (ex: Bash).

- **Comandos básicos aprendidos**:
  - `pwd` → mostra o diretório atual.
  - `ls -l` → lista arquivos detalhadamente.
  - `cd /caminho` → muda de diretório.
  - `mkdir nome` → cria diretório.
  - `rmdir nome` → remove diretório vazio.
  - `rm -rf nome` → remove diretório e conteúdo.
  - `cp origem destino` → copia arquivos.
  - `mv origem destino` → move/renomeia arquivos.
  - `cat arquivo` → mostra conteúdo de arquivo.
  - `grep "texto" arquivo` → busca texto dentro de arquivo.
  - `chmod` e `chown` → alteram permissões e proprietário.

---

## 💻 Comandos executados no terminal

### Estrutura e navegação

```bash
pwd
ls -la /
cd /home
mkdir teste_linux
cd teste_linux
Criação e manipulação de arquivos
echo "Aprendendo Linux no curso" > anotacoes.txt
cat anotacoes.txt
cp anotacoes.txt backup.txt
mv backup.txt ~/Documentos/
Permissões e propriedades
ls -l
chmod 755 anotacoes.txt
chown usuario:usuario anotacoes.txt
Busca e filtros
grep "Linux" anotacoes.txt
🧠 Reflexão

O aprendizado do Linux é fundamental para profissionais de Cybersegurança. A compreensão da estrutura de diretórios, permissões e comandos básicos é essencial para:

Investigar logs.

Automatizar tarefas.

Analisar arquivos de configuração e vulnerabilidades.

Operar em servidores e sistemas baseados em Unix.

Esse foi o primeiro contato prático com o terminal, consolidando o entendimento sobre como o sistema operacional funciona “por baixo dos panos”.
📅 Conclusão:
Dia 22 concluído com sucesso. A base de Linux está formada — a partir daqui, o uso do terminal se tornará natural, principalmente para tarefas de análise e automação em segurança da informação.