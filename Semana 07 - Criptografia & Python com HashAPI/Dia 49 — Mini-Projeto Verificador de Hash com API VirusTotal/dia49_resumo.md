# Resumo — Dia 49  
## Mini‑Projeto: Verificador de Hash com API VirusTotal

### 🎯 Objetivo do Dia  
Desenvolver um script completo para análise de arquivos usando **hash SHA256** e consulta à **API do VirusTotal**, registrando resultados, gerando relatórios e simulando automação SOC.

---

## 📌 O que você aprendeu

### 🔐 1. Geração de Hash SHA256  
- Uso do módulo `hashlib`.
- Entendimento de integridade e impressão digital de arquivos.
- Hash como ponto central da análise antivírus.

---

### 🌐 2. Consumo da API VirusTotal  
- Autenticação via **API Key**.  
- Requisições HTTP (`requests`).  
- Tratamento dos retornos:  
  - 200 → Hash encontrado  
  - 404 → Hash nunca analisado  
  - 429 → Limite de requisições atingido  

---

### 📊 3. Interpretação da Análise  
Extração das estatísticas:  
- `malicious`  
- `suspicious`  
- `harmless`  
- `undetected`  

Classificação final automática:  
- **Malicioso**  
- **Suspeito**  
- **Limpo**

---

### 🗂️ 4. Salvando Relatórios  
Foram gerados:  
- `resultado_vt.json` — Detalhado  
- `relatorio_vt.csv` — Resumo da análise  
Com informações adicionais:  
- Data/hora  
- Resultado textual  
- Link direto para o relatório no VirusTotal  

---

### 🧪 5. Exercícios Práticos  
- Processar múltiplos arquivos.  
- Tratar erros de rede e limites da API.  
- Enriquecer CSV com metadados.  

---

### 🚨 6. Exercício Avançado – Integração com Logs  
Processo SOC realista:  
- Ler `logs.txt`.  
- Extrair nomes de executáveis (regex).  
- Gerar hash.  
- Consultar VirusTotal.  
- Consolidar tudo em relatório final.

---

### 📁 Estrutura Final do Projeto

```
Projeto_VirusTotal/
├── verificador_hash_vt.py
├── verificador_multiplos.py
├── resultado_vt.json
├── relatorio_vt.csv
├── chave.key
├── logs.txt
└── README_semana7.md
```

---

## 🚀 Desafio Final  
Criar um **dashboard de terminal** com menu interativo:  
- 1: Analisar arquivo  
- 2: Ver histórico  
- 3: Sair  
Usando **colorama** para exibir o resultado com cores:  
- 🔴 Vermelho → Malicioso  
- 🟡 Amarelo → Suspeito  
- 🟢 Verde → Limpo  

---

## 📘 Conclusão  
O Dia 49 marcou o aprendizado completo de:  
- Hashes  
- Consumo de API  
- Automação SOC  
- Geração de relatórios  
- Integração entre sistemas  

Você concluiu um **mini-projeto realista**, aplicável no dia a dia de um analista de segurança.

