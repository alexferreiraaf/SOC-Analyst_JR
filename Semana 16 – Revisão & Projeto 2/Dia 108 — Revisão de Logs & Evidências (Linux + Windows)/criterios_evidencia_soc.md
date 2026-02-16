# Critérios de Evidência — SOC

## 🎯 O que foi considerado evidência válida

- Logs contendo IP suspeito (203.0.113.50)
- Eventos com timestamp preciso
- Correlação entre Linux e Windows
- Login bem-sucedido após múltiplas falhas
- Identificação clara de usuário afetado

Esses elementos sustentam narrativa técnica e impacto potencial.

---

## 🚫 O que foi descartado

- Logs sem relação com o IP investigado
- Eventos fora do período analisado
- Registros duplicados sem valor adicional
- Eventos sem contexto ou relevância

---

## 🧠 Justificativa Técnica

Evidência válida deve:

- Ser relevante para o incidente
- Ter integridade preservada
- Permitir rastreabilidade temporal
- Sustentar análise reproduzível

---

## 📌 Conclusão

A correlação entre tentativas de brute force no Linux e login bem-sucedido no Windows caracteriza incidente com possível comprometimento de credencial.

As evidências coletadas sustentam relatório técnico e possível escalonamento para resposta avançada.
