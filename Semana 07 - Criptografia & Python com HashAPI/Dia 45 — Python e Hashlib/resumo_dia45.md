# 🧩 Dia 45 — Python e Hashlib

## 🎯 Objetivo

Dominar o uso do módulo `hashlib` para **gerar e comparar hashes de arquivos**, aplicando isso em segurança, verificação de integridade e análise de malware.

---

## 📘 Conceitos Fundamentais

### 🔹 O que é o módulo `hashlib`?

- Biblioteca **nativa do Python** usada para criar funções de hash.
- Suporta algoritmos:
  - `MD5`
  - `SHA1`
  - `SHA224`
  - `SHA256`
  - `SHA384`
  - `SHA512`

### 🔹 O que é o `hexdigest()`?

- Converte o valor binário do hash em **texto hexadecimal legível**.

```python
import hashlib
print(hashlib.sha256(b"teste").hexdigest())
# Saída: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
🔹 Por que usar hashes em segurança?
Aplicação	Finalidade
Integridade	Garantir que o arquivo não foi alterado
Senhas	Armazenar de forma segura
Malware	Comparar com bases de dados como VirusTotal
Logs SOC	Verificar repetição de binários suspeitos
💻 Prática Passo a Passo
🧩 Nível 1 — Fundamentos

Crie o arquivo gerador_hash.py:

import hashlib
from pathlib import Path

arquivo = Path("teste.txt")

if arquivo.exists():
    conteudo = arquivo.read_bytes()
    print(f"\n🔐 Hashes de {arquivo.name}:\n")
    print(f"MD5:    {hashlib.md5(conteudo).hexdigest()}")
    print(f"SHA1:   {hashlib.sha1(conteudo).hexdigest()}")
    print(f"SHA256: {hashlib.sha256(conteudo).hexdigest()}")
else:
    print("❌ Arquivo não encontrado!")

🧩 Nível 2 — Manipulação de Erros e CSV

Crie gerador_hash_csv.py:

import hashlib
import csv
from datetime import datetime
from pathlib import Path

arquivo = input("Digite o nome do arquivo: ")
path = Path(arquivo)

if not path.exists():
    print("❌ Arquivo não encontrado!")
else:
    conteudo = path.read_bytes()

    hashes = {
        "MD5": hashlib.md5(conteudo).hexdigest(),
        "SHA1": hashlib.sha1(conteudo).hexdigest(),
        "SHA256": hashlib.sha256(conteudo).hexdigest()
    }

    print(f"\n🔐 Hashes de {arquivo}:\n")
    for nome, valor in hashes.items():
        print(f"{nome}: {valor}")

    with open("hash_resultados.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([arquivo, datetime.now(), *hashes.values()])

    print("\n✅ Resultados salvos em hash_resultados.csv")


📄 Saída esperada (CSV):

Arquivo	Data/Hora	MD5	SHA1	SHA256
🧩 Nível 3 — Comparação de Hashes

Crie verifica_integridade.py:

import hashlib

def gerar_hash(nome_arquivo):
    with open(nome_arquivo, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

arq1 = input("Arquivo 1: ")
arq2 = input("Arquivo 2: ")

hash1 = gerar_hash(arq1)
hash2 = gerar_hash(arq2)

if hash1 == hash2:
    print("✅ Os arquivos são idênticos (mesmo conteúdo).")
else:
    print("⚠️ Os arquivos são diferentes!")

🧩 Nível 4 — Hashes de Senhas (Extra)

Crie hash_senha.py:

import hashlib

senha = input("Digite sua senha: ").encode()
hash_senha = hashlib.sha256(senha).hexdigest()
print(f"Hash armazenado: {hash_senha}")

login = input("Digite novamente sua senha: ").encode()
if hashlib.sha256(login).hexdigest() == hash_senha:
    print("🔓 Senha correta!")
else:
    print("🚫 Senha incorreta!")

🧩 Nível 5 — Mini-Projeto Final

Crie hash_scanner.py:

import hashlib, csv, os
from datetime import datetime

pasta = input("Digite o nome da pasta a verificar: ")

with open("hashes_diretorio.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Arquivo", "SHA256", "Fingerprint", "Data/Hora"])

    for arquivo in os.listdir(pasta):
        caminho = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho):
            with open(caminho, "rb") as f:
                h = hashlib.sha256(f.read()).hexdigest()
                writer.writerow([arquivo, h, h[:5], datetime.now()])
                print(f"{arquivo}: {h[:5]}...")

print("\n✅ hashes_diretorio.csv gerado com sucesso.")


📊 Saída esperada:

Arquivo	SHA256	Fingerprint	Data/Hora
🧠 Desafios
🔸 Básico

Gere MD5, SHA1 e SHA256 de três arquivos.

Modifique um deles e compare os hashes.

🔸 Intermediário

Gere um CSV com hashes de todos os arquivos de uma pasta.

Detecte quais foram alterados após uma modificação.

🔸 Avançado

Integre com a API do VirusTotal (será feito no Dia 47).

📚 Leituras Recomendadas

Documentação oficial do hashlib

OWASP Password Storage Cheat Sheet

Artigo: "Why MD5 and SHA1 are broken" (Google Project Zero)

📦 Entregáveis do Dia 45
Arquivo	Descrição
gerador_hash.py	Gera hashes básicos
gerador_hash_csv.py	Gera e salva hashes no CSV
verifica_integridade.py	Compara dois arquivos
hash_scanner.py	Mini-projeto de varredura
hash_resultados.csv	Resultados de hash
(opcional) hash_senha.py	Simulação de hash de senha
🧩 Desafio Bônus

Integre o hash_scanner.py com a API do VirusTotal (feito no Dia 47) para verificar se algum dos hashes aparece como suspeito em bases públicas.