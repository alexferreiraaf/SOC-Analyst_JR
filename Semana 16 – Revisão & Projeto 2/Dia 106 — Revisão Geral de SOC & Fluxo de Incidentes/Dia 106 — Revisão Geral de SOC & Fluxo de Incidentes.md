# Dia 106 — Revisão Geral de SOC & Fluxo de Incidentes

## 🎯 Objetivo
Entender como funciona o fluxo completo de um SOC e o papel do analista dentro do processo de tratamento de incidentes.

---

## 🔄 O Fluxo de um Incidente no SOC

1. **Coleta de Logs**
   - Fontes: auth.log, Event Viewer, Firewall, IDS/IPS
   - Sem coleta correta → não existe detecção

2. **Detecção**
   - Regras no SIEM ou scripts
   - Baseada em padrões e thresholds
   - Detecção ≠ incidente

3. **Alerta**
   - Regra disparada
   - Indica possível problema
   - Ainda precisa de validação

4. **Investigação**
   - Análise de contexto
   - Verificação de falso positivo
   - Correlação de eventos
   - Avaliação de impacto

5. **Resposta**
   - Bloqueio de IP
   - Reset de senha
   - Isolamento de máquina
   - Monitoramento

6. **Relatório**
   - O que aconteceu
   - Evidências
   - Impacto
   - Ações tomadas
   - Recomendações

---

## 📚 Conceitos Fundamentais

- **Evento:** Algo aconteceu (ex: falha de login)
- **IOC:** Indicador suspeito (IP, hash, domínio)
- **Alerta:** Regra disparada
- **Incidente:** Ameaça confirmada

---

## 🧑‍💻 SOC N1 vs SOC N2

| SOC N1 | SOC N2 |
|--------|--------|
| Monitora alertas | Investiga profundamente |
| Faz triagem | Executa contenção |
| Documenta | Erradica ameaça |

---

## 🧠 Caso Prático — Brute Force SSH

Fluxo resumido:

1. Logs do `auth.log` registram falhas
2. SIEM detecta múltiplas tentativas
3. Alerta é gerado
4. Analista investiga IP e contexto
5. Confirma tentativa de brute force
6. IP é bloqueado
7. Incidente é documentado

---

## 🏁 Resultado do Dia

Ao final do Dia 106:

- Você entende o SOC como um **pipeline estruturado**
- Sabe diferenciar evento, alerta e incidente
- Entende o papel do SOC N1
- Consegue explicar um incidente do início ao fim
- Está mais preparado para entrevistas técnicas conceituais
