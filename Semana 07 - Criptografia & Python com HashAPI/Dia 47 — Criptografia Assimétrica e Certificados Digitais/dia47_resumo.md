# Dia 47 — Resumo: Criptografia Assimétrica, Assinaturas Digitais e Certificados

## 🎯 Objetivo
Entender o funcionamento da criptografia assimétrica (RSA), assinaturas digitais e certificados digitais X.509, além de executar um laboratório prático com OpenSSL e Python.

---

## 🔐 1. Criptografia Assimétrica
Sistema baseado em **duas chaves**:

- **Chave Pública** → compartilhada  
- **Chave Privada** → secreta  

📌 O que é cifrado com a chave pública só pode ser decifrado com a privada — e vice-versa.

### Ciclos de Uso
| Finalidade | Ação | Chave usada | Verificação |
|------------|------|-------------|-------------|
| Criptografia | Cifrar | Pública | Privada |
| Assinatura Digital | Assinar | Privada | Pública |

---

## ✍️ 2. Assinatura Digital
Garante:

- **Autenticidade**
- **Integridade**
- **Não-repúdio**

A assinatura é feita sobre o **hash** da mensagem.

---

## 📄 3. Certificados Digitais (X.509)
Certificado = “RG digital” contendo:

- Dono
- Chave pública
- Validade
- Emissor (CA)
- Assinatura da CA

Extensões comuns: `.crt`, `.cer`, `.pem`

---

## 🧪 4. Laboratório com OpenSSL

### 🔹 Gerar chaves
```
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
```

### 🔹 Criptografar e Descriptografar
```
echo "Mensagem confidencial SOC" > mensagem.txt
openssl rsautl -encrypt -inkey public.pem -pubin -in mensagem.txt -out mensagem.enc
openssl rsautl -decrypt -inkey private.pem -in mensagem.enc -out mensagem_decifrada.txt
```

### 🔹 Assinar e Verificar
```
openssl dgst -sha256 -sign private.pem -out assinatura.bin mensagem.txt
openssl dgst -sha256 -verify public.pem -signature assinatura.bin mensagem.txt
```

### 🔹 Criar Certificado X.509
```
openssl req -new -x509 -key private.pem -out certificado.crt -days 365
openssl x509 -in certificado.crt -text -noout
```

---

## 🐍 5. Criptografia com Python (Opcional)
Utilização da biblioteca `cryptography` para gerar chaves RSA, cifrar/decifrar e assinar/verificar.

---

## 🧠 6. Exercícios Propostos
### Nível 1
- Gerar chaves extras  
- Testar decifrar com chave errada  
- Assinar arquivo e verificar integridade  

### Nível 2
- Analisar certificado  
- Converter PEM ↔ DER  

### Nível 3
Criar script `assinatura_verificacao.py` fazendo:
- Assinatura
- Verificação automática

### Nível 4 — Pipeline Final
1. Criar arquivo sigiloso  
2. Gerar hash  
3. Assinar  
4. Enviar  
5. Verificar do outro lado  

---

## 📦 Entregáveis do Dia 47
- `dia47_rsa_certificados.md`
- `private.pem`
- `public.pem`
- `mensagem.txt`
- `mensagem.enc`
- `assinatura.bin`
- `certificado.crt`
- *(opcional)* `assinatura_verificacao.py`

