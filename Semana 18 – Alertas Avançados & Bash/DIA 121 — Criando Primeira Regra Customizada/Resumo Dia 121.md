# Dia 121 — Criando Primeira Regra Customizada no Wazuh

## 🎯 Objetivo

Aprender a criar regras customizadas no Wazuh utilizando o arquivo `local_rules.xml`, permitindo adaptar a detecção de eventos ao contexto do negócio sem alterar regras padrão do sistema.

---

# 🧠 Conceito da Regra Criada

O objetivo da regra é detectar logins SSH realizados fora do horário permitido.

Exemplo de cenário:

- Horário normal da empresa: 08:00 às 18:00
- Login às 02:00 da manhã
- O evento deve gerar um alerta para investigação

---

# 📄 Arquivo: local_rules.xml

```xml
<group name="custom,ssh,">

  <rule id="100100" level="10">
    <if_sid>5715</if_sid>
    <time>22:00 - 23:59</time>
    <description>Alerta: Login SSH fora do horário permitido</description>
  </rule>

</group>
```

## 🔄 Fluxo da Regra
```
Login SSH bem-sucedido
        ↓
auth.log
        ↓
Decoder SSH
        ↓
Regra Base (5715)
        ↓
Regra Customizada (100100)
        ↓
Validação do horário
        ↓
Alerta gerado
        ↓
Dashboard Wazuh
```

## 📌 Explicação da Regra

```<group name="custom,ssh,">```

Agrupa a regra dentro da categoria customizada SSH.
