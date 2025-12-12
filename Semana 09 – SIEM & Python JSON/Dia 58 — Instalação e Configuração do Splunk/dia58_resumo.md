# 📘 Resumo — Dia 58: Instalação e Configuração do Splunk

## 🎯 Objetivo do Dia
- Instalar e iniciar o Splunk corretamente  
- Entender serviços principais: **splunkd** e **splunkweb**  
- Configurar entradas de log com **inputs.conf**  
- Executar buscas iniciais  
- Compreender **index**, **sourcetype** e **source**

---

## 🧠 Conceitos Fundamentais

### 🔥 O que é o Splunk?
O Splunk é uma plataforma completa de análise de logs, atuando como:
- Motor de indexação  
- Banco de dados otimizado para buscas  
- Search engine avançado (SPL)  
- Plataforma de dashboards, alertas e correlação  
- Ferramenta essencial para SOC e detecção de ameaças  

---

## 🧱 Componentes Principais

### **1️⃣ splunkd**
Serviço principal responsável por:
- Processar e indexar logs  
- Gerenciar buscas  
- Executar alertas  
- Manter processos internos  

### **2️⃣ splunkweb**
Interface visual acessada em:
```
http://localhost:8000
```
Permite visualizar dashboards, executar buscas e gerenciar dados.

### **3️⃣ inputs.conf**
Arquivo de configuração que define:
- Quais logs monitorar  
- Em qual *index* armazenar  
- Qual *sourcetype* aplicar  

Exemplo:
```
[monitor:///var/log/auth.log]
sourcetype = linux_secure
index = main
```

---

## 🧩 Conceitos-Chave

| Conceito     | Significado |
|--------------|-------------|
| **source**   | Arquivo ou origem real do log |
| **sourcetype** | Formato / tipo do log |
| **index**    | Local onde os dados são armazenados |
| **host**     | Máquina de origem |
| **_raw**     | Evento original |
| **_time**    | Timestamp do evento |

---

## 🧪 Atividade Prática

### ✔ 1. Instalar o Splunk  
Baixar no site oficial e iniciar com:
```
splunk start
```

### ✔ 2. Acessar o Splunk Web  
```
http://localhost:8000
```

### ✔ 3. Explorar seções:
- Search & Reporting  
- Add Data  
- Settings → Data Inputs  

### ✔ 4. Adicionar Log Local  
Windows:
```
C:\Windows\System32\winevt\Logs\Security.evtx
```
Linux:
```
/var/log/auth.log
```

### ✔ 5. Primeira busca:
```
index=_internal | stats count by source
```

---

## 🧪 Exercícios Práticos

### 🔍 1. Contar falhas de login

**Windows**
```
index=* sourcetype="WinEventLog:Security" EventCode=4625
| stats count by Account_Name, Workstation_Name
```

**Linux**
```
index=* "Failed password"
| stats count by user, host, src
```

### 🔍 2. Top 10 IPs com falhas
```
index=* "Failed password"
| stats count by src_ip
| sort -count
| head 10
```

### 🔍 3. Criar Dashboard  
Salvar busca como painel.

### 🔍 4. Criar alerta  
Mais de 5 falhas em 1 minuto.

### 🔍 5. Configurar inputs.conf manualmente
```
[monitor:///var/log/auth.log]
index=os
sourcetype=linux_secure
disabled=false
```

---

## 🔥 Desafios Avançados
- Configurar Splunk Universal Forwarder  
- Criar Field Extraction com regex  
- Criar um app completo no Splunk  
- Simular brute-force e monitorar em tempo real  

---

## 📌 Conclusão
O Dia 58 consolida a base essencial para operar como SOC Analyst Jr no Splunk, entendendo arquitetura, ingestão e consultas de logs.
