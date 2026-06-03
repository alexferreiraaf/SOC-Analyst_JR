# 🧠 Respostas dos Exercícios
## Exercício 1
### Por que não devemos editar regras padrão?
Porque atualizações do Wazuh podem sobrescrever as alterações.
Além disso:
- Facilita manutenção
- Evita erros de compatibilidade
- Mantém a instalação suportada
Por isso utilizamos:

```/var/ossec/etc/rules/local_rules.xml```

## Exercício 2
### Se remover ```<if_sid>```, o que acontece?
A regra deixa de herdar a lógica da regra base.
Consequências:
- Pode nunca disparar
- Pode gerar alertas incorretos
- Perde o contexto do evento original
A herança garante que a regra seja aplicada apenas quando a condição inicial já foi validada.

## Exercício 3
### Esse alerta deve ser crítico (Level 12)?
Não necessariamente.
Um login fora do horário pode ser:
- legítimo
- administrativo
- manutenção
O ideal é iniciar com severidade média/alta (Level 7–10) e aumentar apenas se houver contexto adicional que indique comprometimento.

## Exercício 4
### Como disparar apenas para o usuário root?

Exemplo conceitual:

```xml <rule id="100101" level="12">
  <if_sid>5715</if_sid>
  <field name="dstuser">root</field>
  <time>22:00 - 23:59</time>
  <description>Login SSH do usuário root fora do horário permitido</description>
</rule>
```
Nesse caso, somente logins do usuário root seriam analisados.