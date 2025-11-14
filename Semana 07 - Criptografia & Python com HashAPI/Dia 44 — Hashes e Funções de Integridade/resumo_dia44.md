# 🧩 Dia 44 — Hashes e Funções de Integridade

## 🎯 Objetivo

Dominar o conceito, funcionamento e aplicação de **funções hash** para garantir **integridade, autenticidade e segurança** de informações.  
Aprender a **gerar, comparar e automatizar verificações de hash** em múltiplas plataformas.

---

## 📘 PARTE 1 — Teoria Detalhada

### 🔹 1. O que é um Hash

Um **hash** é uma função matemática **unidirecional** que transforma uma entrada (texto, arquivo, senha, etc.) em uma **impressão digital única**.  
Mesmo pequenas mudanças na entrada geram resultados totalmente diferentes — o chamado **efeito avalanche**.

| Entrada | Hash (SHA256) |
| -------- | -------------- |
| senha123 | ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f |
| Senha123 | 26f9f61a0c21999825b9b45d334938a3a4e6da09c7b2a3f2c0a639943d69e0a5 |

---

### 🔹 2. Características das Funções Hash

| Propriedade | Descrição |
| ------------ | ---------- |
| **Unidirecional** | Não é possível reverter o hash para o dado original. |
| **Determinística** | A mesma entrada sempre gera o mesmo resultado. |
| **Uniforme** | Distribui resultados de forma homogênea. |
| **Resistente a colisões** | Difícil encontrar duas entradas com o mesmo hash. |
| **Sensível** | Pequenas mudanças → grandes diferenças. |

---

### 🔹 3. Principais Algoritmos

| Algoritmo | Bits | Segurança | Uso Comum |
| ---------- | ---- | ---------- | ---------- |
| **MD5** | 128 | ❌ Inseguro (colisões) | Checksums antigos |
| **SHA-1** | 160 | ⚠️ Quebrado | Assinaturas antigas |
| **SHA-256** | 256 | ✅ Seguro | Integridade, Blockchain |
| **SHA-512** | 512 | ✅ Muito seguro | Arquivos sensíveis |
| **BLAKE2 / SHA3** | variável | 🔒 Alta segurança moderna | Criptografia moderna |

---

### 🔹 4. Aplicações Práticas

| Aplicação | Exemplo |
| ---------- | -------- |
| **Verificação de integridade** | Conferir se o arquivo baixado não foi alterado |
| **Armazenamento de senhas** | Guardar hash em vez da senha real |
| **Detecção de malware** | Comparar hash com base do VirusTotal |
| **Blockchain** | Blocos conectados via SHA256 |

---

## 🧪 PARTE 2 — Prática Passo a Passo

### 💻 1. Teste Manual de Hash

#### 🪟 Windows (PowerShell)

```powershell
Get-FileHash arquivo.txt -Algorithm MD5
Get-FileHash arquivo.txt -Algorithm SHA1
Get-FileHash arquivo.txt -Algorithm SHA256
Get-FileHash arquivo.txt -Algorithm SHA512
🐧 Linux / macOS
md5sum arquivo.txt
sha1sum arquivo.txt
sha256sum arquivo.txt
sha512sum arquivo.txt


📌 Exercício 1:
Gere os 4 hashes de um mesmo arquivo e salve em hash_comparativo.csv.
Depois, altere 1 letra e observe como o hash muda completamente.

💻 2. Hashing de múltiplos arquivos

Crie a pasta teste_hash/ com vários .txt e execute:

Get-ChildItem -Path .\teste_hash\ -File | ForEach-Object {
    $hash = Get-FileHash $_.FullName -Algorithm SHA256
    "$($_.Name),$($hash.Hash)" | Out-File -Append hashes.csv
}


📌 Exercício 2:
Adicione um arquivo idêntico a outro e confirme que o hash será o mesmo.

💻 3. Automatizando com Python

Crie gerador_hashes.py:

import hashlib, os, csv

def gerar_hash(arquivo, algoritmo="sha256"):
    h = hashlib.new(algoritmo)
    with open(arquivo, "rb") as f:
        for bloco in iter(lambda: f.read(4096), b""):
            h.update(bloco)
    return h.hexdigest()

with open("hashes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Arquivo", "Hash (SHA256)"])
    for arquivo in os.listdir("."):
        if os.path.isfile(arquivo):
            hash_valor = gerar_hash(arquivo)
            writer.writerow([arquivo, hash_valor])

print("✅ Arquivo 'hashes.csv' gerado com sucesso.")


📌 Exercício 3:
Teste em uma pasta com 5 arquivos, altere um e compare os hashes antes e depois.

💻 4. Comparação de integridade

Crie comparador_hash.py:

import hashlib

def hash_arquivo(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(4096), b""):
            h.update(bloco)
    return h.hexdigest()

orig = hash_arquivo("arquivo_original.txt")
novo = hash_arquivo("arquivo_modificado.txt")

if orig == novo:
    print("✅ Arquivos idênticos!")
else:
    print("⚠️ Arquivos diferentes!")

🧠 PARTE 3 — Desafios Práticos
🔸 Nível 1 – Básico

Gere hashes SHA256 de 3 arquivos.

Altere apenas 1 caractere e observe a diferença.

🔸 Nível 2 – Intermediário

Crie um comparador de hashes CSV.

Destaque arquivos que foram modificados.

🔸 Nível 3 – Avançado

Use a API do VirusTotal para consultar o hash SHA256 e verificar se o arquivo é malicioso.
(Dica: use a biblioteca requests — será aprofundado no Dia 47.)

🧩 Mapa Mental Recomendado

Inclua:

O que é hash

Tipos de algoritmos

Aplicações práticas

Exemplos

Ferramentas

Ferramentas sugeridas:
Miro
, Draw.io
, Notion Map View

📦 Entregáveis do Dia 44

hashes.csv — tabela de comparação

gerador_hashes.py — script automático

comparador_hash.py — script de verificação

mapa_hash_integridade.png — mapa mental

dia44_hash_integridade.md — resumo completo do estudo

🐧 Linux / macOS
md5sum arquivo.txt
sha1sum arquivo.txt
sha256sum arquivo.txt
sha512sum arquivo.txt


📌 Exercício 1:
Gere os 4 hashes de um mesmo arquivo e salve em hash_comparativo.csv.
Depois, altere 1 letra e observe como o hash muda completamente.

💻 2. Hashing de múltiplos arquivos

Crie a pasta teste_hash/ com vários .txt e execute:

Get-ChildItem -Path .\teste_hash\ -File | ForEach-Object {
    $hash = Get-FileHash $_.FullName -Algorithm SHA256
    "$($_.Name),$($hash.Hash)" | Out-File -Append hashes.csv
}


📌 Exercício 2:
Adicione um arquivo idêntico a outro e confirme que o hash será o mesmo.

💻 3. Automatizando com Python

Crie gerador_hashes.py:

import hashlib, os, csv

def gerar_hash(arquivo, algoritmo="sha256"):
    h = hashlib.new(algoritmo)
    with open(arquivo, "rb") as f:
        for bloco in iter(lambda: f.read(4096), b""):
            h.update(bloco)
    return h.hexdigest()

with open("hashes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Arquivo", "Hash (SHA256)"])
    for arquivo in os.listdir("."):
        if os.path.isfile(arquivo):
            hash_valor = gerar_hash(arquivo)
            writer.writerow([arquivo, hash_valor])

print("✅ Arquivo 'hashes.csv' gerado com sucesso.")


📌 Exercício 3:
Teste em uma pasta com 5 arquivos, altere um e compare os hashes antes e depois.

💻 4. Comparação de integridade

Crie comparador_hash.py:

import hashlib

def hash_arquivo(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(4096), b""):
            h.update(bloco)
    return h.hexdigest()

orig = hash_arquivo("arquivo_original.txt")
novo = hash_arquivo("arquivo_modificado.txt")

if orig == novo:
    print("✅ Arquivos idênticos!")
else:
    print("⚠️ Arquivos diferentes!")

🧠 PARTE 3 — Desafios Práticos
🔸 Nível 1 – Básico

Gere hashes SHA256 de 3 arquivos.

Altere apenas 1 caractere e observe a diferença.

🔸 Nível 2 – Intermediário

Crie um comparador de hashes CSV.

Destaque arquivos que foram modificados.

🔸 Nível 3 – Avançado

Use a API do VirusTotal para consultar o hash SHA256 e verificar se o arquivo é malicioso.
(Dica: use a biblioteca requests — será aprofundado no Dia 47.)

🧩 Mapa Mental Recomendado

Inclua:

O que é hash

Tipos de algoritmos

Aplicações práticas

Exemplos

Ferramentas

Ferramentas sugeridas:
Miro
, Draw.io
, Notion Map View

📦 Entregáveis do Dia 44

hashes.csv — tabela de comparação

gerador_hashes.py — script automático

comparador_hash.py — script de verificação

mapa_hash_integridade.png — mapa mental

dia44_hash_integridade.md — resumo completo do estudo