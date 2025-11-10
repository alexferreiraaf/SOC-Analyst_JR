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
