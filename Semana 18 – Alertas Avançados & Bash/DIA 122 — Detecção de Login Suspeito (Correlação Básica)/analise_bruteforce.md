# Análise de Brute Force SSH — Dia 122

## Resumo da Detecção

Foi criada uma regra de correlação no Wazuh para identificar possíveis ataques de força bruta contra o serviço SSH.

A regra monitora eventos de falha de autenticação e dispara um alerta quando são identificadas:

* 5 falhas de login
* Em um intervalo de até 120 segundos

Configuração utilizada:

```xml
<rule id="100200" level="12">
    <if_sid>5716</if_sid>
    <frequency>5</frequency>
    <timeframe>120</timeframe>
    <description>Possível ataque de força bruta SSH (5 falhas em 2 minutos)</description>
</rule>
```

---

# Por que utilizar Level 12?

A severidade 12 foi escolhida porque a regra não detecta apenas uma falha isolada, mas sim um padrão compatível com tentativa de ataque.

Uma única senha incorreta pode ser erro humano.

Cinco falhas consecutivas em um curto período de tempo indicam comportamento significativamente mais suspeito.

Fatores considerados:

* Repetição do evento
* Curto intervalo de tempo
* Possível tentativa automatizada
* Alvo sendo um serviço crítico (SSH)

Por esses motivos, a regra foi classificada como crítica.

---

# Quando eu escalaria esse alerta?

O alerta deve ser escalado quando houver evidências adicionais que aumentem o risco do evento.

Exemplos:

* IP de origem externo
* Usuário privilegiado (root, administrador)
* Tentativas contra múltiplos usuários
* Grande volume de eventos
* Horário incomum
* Login bem-sucedido após as falhas

Exemplo de cenário para escalonamento imediato:

```text
IP externo
6 falhas em 90 segundos
1 login bem-sucedido logo em seguida
```

Nesse caso existe possibilidade de comprometimento de credenciais.

---

# Quando eu classificaria como falso positivo?

Nem todo alerta de brute force representa um ataque real.

Exemplos de possíveis falsos positivos:

* Usuário digitando a senha errada repetidamente
* Script interno mal configurado
* Ferramenta de monitoramento realizando testes
* Equipe de infraestrutura realizando validações

Antes de classificar como incidente é necessário validar:

* Origem do IP
* Usuário envolvido
* Horário da atividade
* Histórico do host
* Existência de login bem-sucedido posterior

---

# Diferença entre Evento e Ataque

## Evento Isolado

```text
1 falha de login
```

Possível erro humano.

Normalmente não representa incidente.

---

## Evento Correlacionado

```text
5 falhas em 120 segundos
```

Indica comportamento suspeito.

Justifica investigação.

---

## Possível Ataque

```text
5 falhas em 120 segundos
+
IP externo
+
Login bem-sucedido posterior
```

Alta probabilidade de comprometimento.

Deve ser tratado como incidente de segurança.

---

# Processo de Investigação SOC

Ao receber esse alerta, o analista deve verificar:

1. Endereço IP de origem
2. Usuário atacado
3. Quantidade de tentativas
4. Janela temporal
5. Existência de login bem-sucedido
6. Histórico do mesmo IP
7. Impacto potencial

---

# Conclusão

A utilização de `<frequency>` e `<timeframe>` permite transformar eventos isolados em detecções baseadas em comportamento.

Essa abordagem reduz falsos positivos e aumenta a capacidade do SOC de identificar ataques reais.

A regra criada representa um exemplo clássico de correlação básica utilizada em ambientes corporativos para detectar tentativas de brute force contra serviços SSH.
