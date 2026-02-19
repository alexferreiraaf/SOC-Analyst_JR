# 🔐 Projeto SOC — Detecção de Brute Force em SSH

## 🎯 Objetivo

Este projeto detecta tentativas de ataque de força bruta (Brute Force) contra o serviço SSH analisando logs do sistema Linux.

O objetivo é simular um mecanismo básico de detecção utilizado em ambientes SOC (Security Operations Center).

---

## 🛡️ Ataque Detectado

O projeto detecta:

Brute Force em SSH

Esse ataque ocorre quando um IP realiza múltiplas tentativas de login com falha tentando adivinhar credenciais.

---

## 📂 Log Analisado

Arquivo analisado:

logs/auth.log

Origem típica:
- /var/log/auth.log (Ubuntu/Debian)
- Registros de tentativas de login SSH

---

## 📏 Regra de Detecção

Um IP é considerado suspeito quando:

Realiza 5 ou mais tentativas de login falhadas.

Critério técnico:

- Linha contém "Failed password"
- Extração do IP via regex
- Contador por IP
- Limiar configurável (default = 5)

---

## 📤 Saída do Sistema

O sistema gera:

1️⃣ Saída no terminal com IPs suspeitos  
2️⃣ Arquivo evidencias/alertas.txt  
3️⃣ Arquivo evidencias/ips_suspeitos.csv  
4️⃣ Arquivo evidencias/resumo.json  

---

## 🚀 Como Executar

```bash
python3 scripts/detector_bruteforce.py

