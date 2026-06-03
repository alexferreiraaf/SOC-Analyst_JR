# 📌 Conclusão
A criação de regras customizadas permite adaptar o Wazuh à realidade do ambiente monitorado.
Neste laboratório foi criada uma regra para detectar logins SSH fora do horário permitido utilizando:
- ```local_rules.xml```
- Herança com ```if_sid```
- Controle de horário com ```time```
- Definição consciente de severidade
O principal aprendizado é que a qualidade de uma regra não está apenas em gerar alertas, mas em gerar alertas úteis para o SOC.