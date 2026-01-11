# 📘 Dia 66 — SPL Avançado para Detecção de Ameaças

## 🎯 Objetivo do Dia
Desenvolver a capacidade de **detectar ataques de força bruta**, reduzir falsos positivos e construir **queries prontas para alertas SOC**, pensando como analista N1/N2.

---

## 🧠 O que é Brute Force
Ataque em que um invasor tenta várias combinações de senha até obter acesso.

Indicadores clássicos:
- Muitas falhas consecutivas
- Mesmo IP tentando vários usuários
- Mesmo usuário recebendo muitas falhas
- Curto intervalo de tempo

---

## 🔎 Logs que indicam brute force

| Sistema | Indicador |
|------|----------|
| Linux | Failed password |
| Windows | Event ID 4625 |
| Apps | login failed / authentication error |

---

## 🧠 Regex no SOC
Regex é usado quando:
- Logs não são estruturados
- Mensagens variam
- É preciso detectar padrões no campo _raw

Exemplo:
```spl
| regex _raw="Failed\s+password"
```

---

## 🎯 Thresholds SOC
Threshold não é fixo:
- 3 falhas → comum
- 10 falhas → suspeito
- 50 falhas → ataque claro

SOC ajusta thresholds conforme o ambiente.

---

## 🧪 Prática Guiada

### Detectar falhas de login
```spl
index=main "Failed password"
```

### Brute force por IP
```spl
index=main "Failed password"
| stats count by src
| where count > 5
```

### Brute force por usuário
```spl
index=main "Failed password"
| stats count by user
| where count > 5
```

### Regex explícito
```spl
index=main
| regex _raw="Failed\s+password"
```

### Brute force por tempo
```spl
index=main "Failed password"
| timechart span=1m count
```

---

## 🔥 Simulações SOC

### IP externo suspeito
```spl
index=main "Failed password"
| stats count by src
| where count > 10
```

### Ataque silencioso
```spl
index=main "Failed password"
| stats count by src user
| where count > 3
```

---

## 🧠 Mini-desafio do Dia
```spl
index=main "Failed password"
| stats count by src user
| where count > 5
```

Perguntas SOC:
- Isso vira alerta?
- Qual severidade?
- É falso positivo ou ataque real?

---

## ✅ Resultado Esperado
Ao final do Dia 66, você:
- Detecta brute force com SPL
- Usa regex e stats com confiança
- Define thresholds realistas
- Cria queries prontas para alertas SOC
