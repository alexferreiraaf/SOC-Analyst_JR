# Resumo — Correlação de Eventos no Wazuh

## O que é Correlação?

Correlação é o processo de relacionar múltiplos eventos que, isoladamente, podem parecer normais, mas que juntos indicam uma atividade suspeita.

Exemplo:

```text
1 falha de login → Pode ser erro humano

5 falhas de login em 2 minutos → Possível ataque de força bruta
```

No SOC, a correlação ajuda a reduzir ruído e aumentar a precisão das detecções.

---

# Como o Wazuh Realiza Correlação

O Wazuh utiliza regras para identificar padrões de comportamento.

Os principais elementos utilizados são:

```xml
<frequency>5</frequency>
<timeframe>120</timeframe>
```

Onde:

* `frequency` = quantidade de eventos
* `timeframe` = janela de tempo em segundos

Exemplo:

```xml
<frequency>5</frequency>
<timeframe>120</timeframe>
```

Significa:

```text
Disparar alerta quando ocorrerem
5 eventos em até 120 segundos.
```

---

# Fluxo de Correlação

```text
Log SSH
    ↓
Decoder
    ↓
Regra Base
    ↓
Contagem de Eventos
    ↓
Frequency + Timeframe
    ↓
Alerta Correlacionado
    ↓
Dashboard Wazuh
```

---

# Evento x Alerta x Incidente

## Evento

É o registro bruto de uma atividade.

Exemplo:

```text
Failed password for user admin
```

---

## Alerta

É um evento que corresponde a uma regra.

Exemplo:

```text
Falha de login detectada.
```

---

## Incidente

É uma atividade que representa risco real ou tentativa comprovada de comprometimento.

Exemplo:

```text
5 falhas de login
+
Login bem-sucedido
+
IP externo
```

---

# Exemplo de Regra de Correlação

```xml
<rule id="100200" level="12">
    <if_sid>5716</if_sid>
    <frequency>5</frequency>
    <timeframe>120</timeframe>
    <description>
        Possível ataque de força bruta SSH
    </description>
</rule>
```

Essa regra gera um alerta quando o mesmo padrão de falha ocorre cinco vezes dentro de dois minutos.

---

# Vantagens da Correlação

* Redução de falsos positivos
* Priorização de eventos importantes
* Identificação de ataques automatizados
* Menos ruído para o analista
* Melhor utilização do tempo da equipe SOC

---

# Cuidados na Configuração

Configurações muito agressivas podem gerar excesso de alertas.

Exemplo:

```xml
<frequency>2</frequency>
<timeframe>600</timeframe>
```

Problema:

* Qualquer usuário que errar a senha duas vezes em dez minutos pode gerar alerta.

Configurações muito permissivas podem deixar ataques passarem despercebidos.

Exemplo:

```xml
<frequency>20</frequency>
<timeframe>60</timeframe>
```

Problema:

* Um atacante pode realizar várias tentativas sem atingir o limiar.

---

# Aplicação em SOC

A correlação é utilizada para detectar:

* Brute Force
* Password Spraying
* Reconhecimento de rede
* Múltiplas tentativas de acesso
* Comportamentos anômalos

O objetivo não é detectar eventos isolados, mas identificar padrões que indiquem atividade maliciosa.

---

# Conclusão

A correlação é uma das técnicas mais importantes em um SIEM.

Por meio de elementos como `frequency` e `timeframe`, o Wazuh consegue transformar eventos isolados em alertas de maior valor para o SOC.

Um analista SOC deve entender não apenas o alerta gerado, mas também a lógica que levou à sua criação, permitindo avaliar corretamente o risco e priorizar a resposta ao incidente.
