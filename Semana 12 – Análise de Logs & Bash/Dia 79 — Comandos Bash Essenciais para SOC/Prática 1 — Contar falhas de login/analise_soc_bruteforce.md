## 🧠 Pergunta SOC
### ❓ “Isso é normal para o ambiente?”
### 🔴 Resposta curta (SOC):

- Não, isso não é normal.

# 🔍 Análise SOC — Justificativa Técnica (Brute Force SSH)

## 📘 Comportamento esperado em um ambiente normal

### Falhas de login:
- Ocorrem **esporadicamente**
- Geralmente **1 ou 2 tentativas**
- Normalmente do **mesmo usuário legítimo**

### Normalmente **não**:
- Se repetem em sequência
- Vêm de IP externo desconhecido
- Atingem vários usuários diferentes

---

## 🚨 O que foi observado no log analisado

- ✅ **Múltiplas falhas de autenticação**
- ✅ **Mesmo IP repetido**
- ✅ **Usuários comuns atacados** (`root`, `admin`, `test`)
- ✅ **Ocorrendo em curto intervalo de tempo**
- ✅ **Horário suspeito (madrugada)**

---

## 🧠 Conclusão SOC

📌 O comportamento observado é **anômalo** e **compatível com ataque de brute force em SSH**.

### Classificação do Incidente
- **Tipo:** Tentativa de ataque
- **Severidade:** Média → Alta (dependendo de sucesso posterior)

### 🔧 Ações Recomendadas
- Continuar investigação
- Identificar o IP atacante
- Verificar se houve eventos de `Accepted password` após as falhas
- Considerar bloqueio do IP (Firewall / Fail2Ban)
