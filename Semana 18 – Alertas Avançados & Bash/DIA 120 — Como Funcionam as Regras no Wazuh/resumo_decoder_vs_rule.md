# Decoder vs Rule no Wazuh

## O que é um Decoder?

O Decoder é o componente responsável por interpretar o formato de um log.

Sua função é extrair informações importantes do evento, como:

- Usuário
- Endereço IP
- Processo
- Ação realizada
- Data e hora

Sem um decoder, o Wazuh não consegue entender corretamente o conteúdo do log.

Exemplo:

Log original:

```
Failed password for root from 192.168.1.50 port 22 ssh2
```

Após o decoder:

- user: root
- srcip: 192.168.1.50
- action: failed password

---

## O que é uma Rule?

A Rule (Regra) é responsável por analisar as informações extraídas pelo decoder.

Ela define:

- O que é suspeito
- O nível de severidade
- A descrição do alerta

Exemplo:

Se o log contém:

```
Failed password
```

A regra pode gerar:

```
Rule ID: 5710
Level: 5
Description: SSH authentication failed
```

---

## Diferença Principal

| Decoder | Rule |
|----------|----------|
| Interpreta o log | Analisa o evento |
| Extrai campos | Aplica lógica |
| Não gera alerta | Pode gerar alerta |
| Entende formato | Classifica risco |

---

## Fluxo Completo

Log → Decoder → Rule → Alert

O decoder entende o evento.

A regra decide se ele merece atenção.

O alerta é o resultado final apresentado ao analista SOC.