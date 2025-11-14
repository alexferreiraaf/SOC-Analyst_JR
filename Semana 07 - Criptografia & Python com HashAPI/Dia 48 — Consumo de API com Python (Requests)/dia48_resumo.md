# 📘 Resumo do Dia 48 — Consumo de API com Python (Requests)

## 🎯 Objetivo
Aprender a consumir APIs HTTP usando a biblioteca `requests`, enviar requisições, tratar respostas JSON, lidar com erros e salvar resultados em arquivos.

---

## 🔹 Conceitos Principais

### **O que é uma API?**
- Interface que permite comunicação entre sistemas.
- APIs REST usam HTTP para enviar e receber dados.

### **Métodos mais importantes**
- **GET** – obter dados  
- **POST** – enviar dados  
- **PUT/PATCH** – atualizar  
- **DELETE** – remover recursos

---

## 💻 Estrutura Básica de Requisição

Uso do `requests.get()`, leitura de:
- `status_code`
- `.json()`
- `.text`
- `.headers`

---

## 📦 Salvando Respostas

Uso de `json.dump()` para salvar arquivos `.json` com resultados de APIs.

---

## 🧪 Exercícios

### **1. Consulta IP Público**
- Criar script `consulta_api.py`
- Consumir API: `https://api.ipify.org?format=json`
- Exibir IP, tempo de resposta e content-type

### **2. Dados de Usuário no GitHub**
- Consumir: `https://api.github.com/users/<usuario>`
- Exibir login, followers, public_repos e created_at
- Salvar em `github_usuario.json`

### **3. Tratamento de Erros**
- Uso de `try/except`
- Captura de falhas de rede
- `.raise_for_status()` para detectar erros HTTP

---

## 🚀 Desafio Avançado — Enriquecedor de IP
Criar `enriquecedor_ip.py` que:
- Lê IPs de `ips.txt`
- Consulta `https://ipinfo.io/{IP}/json`
- Salva campos (ip, city, region, country, org)
- Gera `enriquecimento_ips.csv`

---

## 🧠 Desafio Final
Script `verifica_status_apis.py` que testa:
- IPify
- GitHub
- IPinfo

Registra no CSV:
- Status  
- Tempo de resposta  
- Tamanho da resposta  

---

## 📦 Entregáveis do Dia
- `consulta_api.py`
- `resultado_api.json`
- `github_usuario.json`
- `enriquecedor_ip.py`
- `enriquecimento_ips.csv`
- `status_apis.csv`
