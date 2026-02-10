# 📅 Dia 100 — DoS e DDoS (Resumo SOC)

## 🎯 Objetivo
Aprender a **identificar DoS/DDoS pelo comportamento do tráfego**, antes do serviço cair, pensando como SOC.

---

## 🔹 DoS x DDoS
- **DoS**: um único IP causando indisponibilidade  
- **DDoS**: vários IPs (botnet), mais difícil de mitigar  
📌 SOC foca no **impacto**, não no atacante.

---

## 🔥 Tipos de Ataque (o que o SOC vê)

### Volumétrico
- Muito tráfego (UDP / ICMP)
- Banda e CPU saturadas  
➡️ Sinal: **explosão de pacotes**

### Protocolo
- Abuso do TCP (SYN Flood)
- Muitas conexões incompletas  
➡️ Sinal: **SYN-SENT / SYN-RECV em excesso**

### Aplicação (Layer 7)
- HTTP/HTTPS flood
- Tráfego parece legítimo  
➡️ Sinal: **requisições repetidas ao mesmo endpoint**

---

## 🚨 O que muda no tráfego durante ataque
- 🔺 Volume
- 🔺 Frequência
- 🔺 Conexões simultâneas
- 🔻 Qualidade do serviço

📌 Ataque = **mudança de padrão**, não número isolado.

---

## 🧪 Detecção Conceitual com `ss`

  ```ss -tunap```

 ### SOC observa:

- Estados de conexão
- IPs repetidos
Portas
Impacto no serviço

🚨 Muitos `SYN-SENT`, UDP excessivo ou `TIME-WAIT` exagerado = alerta.

### ❌ Não confundir com ataque

- Backup
- Atualização
- Pico legítimo
- Teste interno

📌 Pergunta-chave:
> Isso estava previsto?

### 🛡️ Resposta SOC (ordem correta)

1. Confirmar impacto
2. Identificar tipo de ataque
3. Coletar evidências
4. Acionar firewall / rate limit / infra / anti-DDoS

### ✅ Resultado do Dia

Você consegue:
- Diferenciar DoS de DDoS pelo tráfego
- Identificar tipo de ataque rapidamente
- Evitar falso positivo
- Pensar como SOC em indisponibilidade