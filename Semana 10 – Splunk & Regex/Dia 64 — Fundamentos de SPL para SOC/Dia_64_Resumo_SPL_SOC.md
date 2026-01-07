# 📘 Dia 64 — Fundamentos de SPL para SOC

## 🎯 Objetivo do Dia
Desenvolver a base mental do SPL, entendendo como ler, interpretar e construir buscas simples no Splunk, com foco em investigações de SOC.

---

## 🧠 O que é SPL
SPL (Search Processing Language) é a linguagem do Splunk usada para:
- Buscar eventos
- Filtrar dados
- Transformar logs em informação
- Criar visualizações e alertas

No SOC, SPL é usado para investigação, threat hunting e criação de regras.

---

## 🔁 Pipeline do SPL
O SPL funciona como uma linha de montagem:

index → filtro → transformação → visualização

Regra de ouro:
- Tudo antes do `|` filtra
- Tudo depois do `|` transforma

Exemplo:
```spl
index=main action=login | table _time user src host
```

---

## 🔎 Tipos de comandos SPL

### Search / Filter
Reduzem o volume de eventos:
```spl
index=main
index=main action=login
index=main host=server01
```

### Transform
Analisam padrões e comportamentos:
- stats
- top
- timechart

---

## 🧩 Campos essenciais para SOC

| Campo | Uso |
|-----|-----|
| _time | Linha do tempo |
| host | Identificar host |
| src | Origem do ataque |
| dest | Destino |
| user | Conta envolvida |
| action | Tipo de evento |

Sem entender campos, não existe investigação.

---

## 🧠 Conceitos importantes
- Index: onde os logs ficam armazenados
- Sourcetype: tipo/estrutura do log
- Event: uma linha de log
- Field Extraction: campos extraídos automaticamente

---

## 🧪 Prática no Splunk

### Busca básica
```spl
index=main
```

### Filtrando logins
```spl
index=main action=login
```

### Filtrando host
```spl
index=main host=server01
```

### Filtrando usuário
```spl
index=main user=admin
```

### Limpando visualização
```spl
index=main action=login
| table _time user src host action
```

---

## 🧠 Mini-desafio SOC
```spl
index=main action=login
| table _time user src host
```

---

## 📦 Entregáveis do Dia
- dia64_resumo.md
- dia64_buscas.txt
- dia64_reflexao.txt

---

## ✅ Resultado esperado
- Leitura clara de SPL
- Entendimento de campos
- Base para stats, top e timechart
