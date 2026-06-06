# Regra Customizada de Correlação para Brute Force

```xml
<group name="custom,ssh,bruteforce">
  <rule id="100200" level="10">
    <if_sid>5716</if_sid>
    <frequency>5</frequency>
    <timeframe>120</timeframe>
    <description>Possível ataque de força bruta SSH (5 falhas em 2 minutos)</description>
  </rule>
</group>
```

## Objetivo

Detectar cinco tentativas de autenticação SSH malsucedidas em um intervalo de 120 segundos.

## Funcionamento

- Herda a regra base através de `<if_sid>`.
- Monitora eventos repetidos utilizando `<frequency>`.
- Restringe a janela temporal com `<timeframe>`.
- Gera um alerta de maior severidade quando o padrão é identificado.

## Benefícios

- Redução de ruído causado por falhas isoladas.
- Detecção precoce de ataques de força bruta.
- Melhor priorização para a equipe SOC.
