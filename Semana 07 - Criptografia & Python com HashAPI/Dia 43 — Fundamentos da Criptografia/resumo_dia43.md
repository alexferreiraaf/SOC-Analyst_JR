# 🧠 Dia 43 — Fundamentos da Criptografia

## 🎯 Objetivo Geral
Compreender como a **criptografia protege dados**, quando aplicar **cada tipo** e realizar **testes práticos** com ferramentas reais — como **OpenSSL**, **Python** e **hashes** — para garantir **confidencialidade, integridade, autenticidade e não repúdio**.

---

## 🔹 Parte 1 — Teoria

### O que é Criptografia
Criptografia é o processo de **converter dados legíveis (plaintext)** em **dados ilegíveis (ciphertext)**, garantindo proteção em armazenamento e transmissão.  
O processo inverso é a **descriptografia**.

### Princípios Fundamentais (CIA + A)

| Princípio | Descrição | Exemplo |
|------------|------------|----------|
| **C – Confidencialidade** | Somente quem tem autorização pode ler a mensagem. | Senhas enviadas via HTTPS |
| **I – Integridade** | Garante que o dado não foi alterado. | Hash SHA256 de um arquivo |
| **A – Autenticidade** | Confirma a identidade do remetente. | Certificado SSL |
| **N – Não repúdio** | Impede o remetente de negar a autoria. | Assinatura digital |

---

## 🔹 Parte 2 — Tipos de Criptografia

| Tipo | Característica | Algoritmos Famosos | Aplicações |
|------|-----------------|--------------------|-------------|
| **Simétrica** | Usa a mesma chave para cifrar e decifrar. | AES, DES, 3DES, Blowfish | VPNs, discos criptografados |
| **Assimétrica** | Usa par de chaves: pública + privada. | RSA, ECC | Certificados digitais |
| **Hash** | Irreversível; gera resumo dos dados. | MD5, SHA1, SHA256, SHA512 | Verificar integridade, senhas |

---

## 🔹 Parte 3 — Prática com OpenSSL

### 🧩 Criptografia Simétrica (AES-256-CBC)
```bash
openssl enc -aes-256-cbc -salt -in segredo.txt -out segredo.enc
openssl enc -aes-256-cbc -d -in segredo.enc -out segredo_decriptado.txt
✔️ Mesmo conteúdo após descriptografia.

🧩 Criptografia Assimétrica (RSA)
openssl genrsa -out chave_privada.pem 2048
openssl rsa -in chave_privada.pem -pubout -out chave_publica.pem
openssl rsautl -encrypt -inkey chave_publica.pem -pubin -in segredo.txt -out segredo_rsa.enc
openssl rsautl -decrypt -inkey chave_privada.pem -in segredo_rsa.enc -out segredo_rsa_decriptado.txt


✔️ RSA usa par de chaves e garante segurança e autenticidade.

🧩 Hashing (SHA256 e MD5)
sha256sum segredo.txt
md5sum segredo.txt
openssl dgst -sha256 segredo.txt


✔️ Hashes mudam completamente mesmo com pequenas alterações (efeito avalanche).

🐍 Parte 4 — Prática com Python
Gerar Hash de Texto
import hashlib
texto = "Segredo123"
print("MD5:", hashlib.md5(texto.encode()).hexdigest())
print("SHA256:", hashlib.sha256(texto.encode()).hexdigest())

Verificar Integridade de Arquivos
import hashlib

def gerar_hash(arquivo):
    h = hashlib.sha256()
    with open(arquivo, 'rb') as f:
        for bloco in iter(lambda: f.read(4096), b""):
            h.update(bloco)
    return h.hexdigest()

if gerar_hash("segredo.txt") == gerar_hash("segredo_decriptado.txt"):
    print("✅ Arquivos idênticos!")
else:
    print("⚠️ Arquivos alterados!")

🧩 Desafios Práticos
🔸 Nível 1 — Básico

Gere hashes de 3 arquivos diferentes e crie uma tabela comparativa.

Descubra qual arquivo foi alterado após mudar 1 letra.

🔸 Nível 2 — Intermediário

Crie um script Python que:

Peça um arquivo.

Gere hash (MD5 e SHA256).

Salve em hashes.csv.

Adicione função que compare dois arquivos e indique se são iguais.

🔸 Nível 3 — Avançado

Gere par de chaves RSA (com cryptography).

Use a chave pública para criptografar e a privada para descriptografar.

Valide integridade com SHA256.

🧭 Mapa Mental Recomendado

Inclua:

Tipos de criptografia (Simétrica, Assimétrica, Hash)

Exemplos e casos de uso

Vantagens e desvantagens
Ferramentas: Excalidraw, Miro, MindMeister

📦 Entregáveis do Dia 43
Arquivo	Descrição
criptografia_simetrica_openssl.txt	Testes com AES
criptografia_assimetrica_rsa.txt	Testes com RSA
hash_integridade.py	Script Python de integridade
hashes.csv	Resultado dos hashes
mapa_criptografia.png	Mapa mental
dia43_criptografia_basica.md	Resumo completo do estudo

✅ Conclusão:
O Dia 43 consolida os fundamentos práticos da criptografia, preparando o terreno para assinaturas digitais, PKI e certificados SSL/TLS.