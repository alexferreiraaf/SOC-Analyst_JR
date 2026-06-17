# DIA 132 — Modelo de Pontuação Inteligente

## Objetivo

Desenvolver um modelo simples de classificação de risco baseado em pontuação (score), utilizando múltiplos fatores para determinar automaticamente o nível de criticidade de um alerta.

---

# Modelo de Pontuação

| Fator                                                  | Pontuação |
| ------------------------------------------------------ | --------- |
| IP externo                                             | +2        |
| Usuário `root`                                         | +2        |
| Horário fora do expediente (antes das 08h ou após 18h) | +1        |
| Level maior ou igual a 10                              | +3        |
| 3 ou mais tentativas de login                          | +2        |

## Classificação Final

| Score     | Classificação |
| --------- | ------------- |
| 0 – 3     | BAIXO         |
| 4 – 6     | MÉDIO         |
| 7 ou mais | ALTO          |

---

# Cenários Testados

## Caso 1 — Baixo Risco

### Entrada

* IP: 192.168.1.50
* Usuário: alex
* Level: 3
* Hora: 14
* Tentativas: 1

### Score

0 pontos

### Classificação

**BAIXO**

### Comentário

Evento compatível com atividade normal de usuário interno, durante horário comercial e sem indicadores relevantes de risco.

---

## Caso 2 — Médio Risco

### Entrada

* IP: 54.23.15.10
* Usuário: admin
* Level: 7
* Hora: 15
* Tentativas: 2

### Score

* IP externo: +2

Total: **2 pontos**

> Caso o modelo seja calibrado para considerar `admin` como usuário privilegiado, o score poderia aumentar para 4 pontos, sendo classificado como **MÉDIO**.

### Classificação

**BAIXO (modelo atual)**

### Comentário

Apesar do IP externo, há poucos indicadores adicionais. Recomenda-se revisão humana antes de qualquer escalonamento.

---

## Caso 3 — Alto Risco

### Entrada

* IP: 185.223.89.44
* Usuário: root
* Level: 12
* Hora: 02
* Tentativas: 5

### Score

* IP externo: +2
* Usuário root: +2
* Horário incomum: +1
* Level crítico: +3
* Múltiplas tentativas: +2

Total: **10 pontos**

### Classificação

**ALTO**

### Comentário

A combinação dos fatores indica forte possibilidade de tentativa de comprometimento, justificando investigação imediata e possível abertura de incidente.

---

# Explicabilidade da Decisão

O sistema não informa apenas o resultado final, mas também os fatores que contribuíram para a classificação.

Exemplo de saída:

```
Risco Final: ALTO

Score Total: 10

Motivos:
- IP externo
- Usuário root
- Horário incomum
- Level crítico
- Múltiplas tentativas
```

Essa transparência facilita auditorias e permite ao analista validar a decisão tomada automaticamente.

---

# Limitações Observadas

* O modelo não considera histórico do IP.
* Não correlaciona eventos distribuídos ao longo do tempo.
* Não detecta sequências como "falha seguida de sucesso".
* Não verifica ASN ou reputação do IOC.
* Não diferencia IP externo legítimo (VPN corporativa) de IP malicioso.
* Não leva em conta comportamento histórico do usuário.

---

# Possíveis Melhorias Futuras

* Integrar enriquecimento de IOC (ASN e reputação).
* Detectar padrões temporais de brute force.
* Aplicar pesos diferentes para usuários privilegiados.
* Considerar reincidência do mesmo IP.
* Ajustar pontuações dinamicamente com base no ambiente.
* Incorporar Machine Learning ou modelos estatísticos em versões futuras.

---

# Conclusão

O modelo de pontuação é uma forma simples e eficiente de automatizar a triagem inicial de alertas, reduzindo o volume de análise manual.

Apesar disso, ele não substitui o julgamento do analista, servindo apenas como apoio à tomada de decisão.

A combinação entre automação e análise humana continua sendo a estratégia mais eficaz para um SOC moderno.
