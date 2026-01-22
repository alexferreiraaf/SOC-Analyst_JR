# Análise SOC — Identificação de IP Atacante

## 📌 IP no topo

Quando um único IP lidera o ranking de falhas:

- Indica **origem centralizada**
- Característica típica de **script automatizado**
- Muito comum em ataques de **brute force SSH**

---

## 📌 Número alto de tentativas

### Em ambientes normais:
- Um usuário erra a senha **1 ou 2 vezes**
- Raramente ultrapassa **3 tentativas**
- Normalmente envolve **um único usuário legítimo**

### No cenário analisado:
- O número de tentativas é **muito superior ao esperado**
- Ocorre em **curto intervalo de tempo**
- Afeta **usuários comuns e privilegiados** (`root`, `admin`, etc.)

---

## 🚨 Conclusão SOC

- ✅ Há um **IP claramente atacante no topo da lista**
- ✅ O volume de tentativas é **anormal para um ambiente legítimo**

### Classificação:
- **Tipo:** Tentativa de brute force SSH  
- **Severidade:** Média → Alta  
- **Confiança:** Alta (padrão consistente de ataque)

### Ações recomendadas:
- Isolar o IP identificado
- Verificar se houve eventos de `Accepted password` após as falhas
- Considerar bloqueio no firewall / `fail2ban`
- Manter monitoramento contínuo do host

---

🧠 *Mentalidade SOC aplicada:*  
> Concentração, repetição e origem externa indicam ataque automatizado.
