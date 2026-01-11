# 📘 Dia 65 — SPL Intermediário: stats, timechart e top

## 🎯 Objetivo do Dia
Aprender a transformar eventos em **padrões, anomalias e insights de segurança**, usando os comandos mais importantes do SPL para um analista SOC.

---

## 🧠 Por que `stats` é fundamental no SOC
O comando `stats` permite sair do nível de evento individual e enxergar **comportamento**.

Ele responde perguntas como:
- Quantas tentativas de login ocorreram?
- Qual usuário aparece mais?
- Qual IP ou host está fora do padrão?

### Sintaxe básica
```spl
| stats função(campo) by campo
```

Funções comuns:
- `count` → quantidade
- `dc()` → valores distintos
- `sum()` → soma
- `avg()` → média

Exemplo:
```spl
index=main action=login
| stats count by user
```

---

## 🔝 `top` — rankings rápidos para SOC
O `top` cria rankings automaticamente, facilitando a priorização.

Exemplo:
```spl
index=main | top 5 src
```

Usado para:
- IPs mais ativos
- Usuários mais barulhentos
- Hosts com maior volume de eventos

---

## ⏱️ `timechart` — comportamento ao longo do tempo
O `timechart` mostra quando os eventos acontecem.

Exemplo:
```spl
index=main action=login
| timechart count
```

Ou por usuário:
```spl
index=main action=login
| timechart count by user
```

SOC usa para:
- Detectar picos
- Ver ataques fora do horário normal
- Confirmar brute force

---

## 🧠 Conceitos SOC Importantes
- **Evento:** um log individual
- **Incidente:** padrão suspeito detectado com stats e timechart
- SOC sempre compara números com o que é considerado normal

---

## 🧪 Prática no Splunk

### Contar eventos por host
```spl
index=main
| stats count by host
```

### Tentativas de login por usuário
```spl
index=main action=login
| stats count by user
```

### Usuários distintos logando
```spl
index=main action=login
| stats dc(user)
```

### Top 5 IPs
```spl
index=main | top 5 src
```

### Logins ao longo do tempo
```spl
index=main action=login
| timechart count
```

---

## 🔥 Mini-simulações SOC

### Possível brute force
```spl
index=main "Failed password"
| stats count by src
| where count > 5
```

### Host suspeito
```spl
index=main
| stats count by host
| sort -count
```

---

## 🧠 Mini-desafio do Dia
```spl
index=main action=login
| top 5 user
```

Perguntas SOC:
- Algum usuário chama atenção?
- Isso pode gerar investigação ou alerta?

---

## ✅ Resultado esperado
Ao final do Dia 65, você:
- Usa stats com confiança
- Interpreta gráficos de timechart
- Cria rankings com top
- Pensa em padrões e não apenas em eventos
