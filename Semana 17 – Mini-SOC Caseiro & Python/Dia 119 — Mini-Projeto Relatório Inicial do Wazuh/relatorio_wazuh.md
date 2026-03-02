# Relatório Inicial de Incidente — Wazuh

## 1. Resumo Executivo

Foi identificado comportamento suspeito relacionado a múltiplas tentativas falhas de autenticação via SSH, caracterizando possível ataque de brute force.

---

## 2. Detecção

A detecção ocorreu por meio do SIEM Wazuh, que gerou alertas de severidade elevada com base em regras de autenticação SSH.

---

## 3. Evidências

- IP suspeito: 185.220.101.45
- Total de tentativas: 37
- Período: 10:12 até 10:24
- Agente afetado: server01

---

## 4. Timeline do Incidente

- 10:12 — Primeira tentativa falha de login SSH
- 10:14 — Aumento significativo de falhas consecutivas
- 10:18 — Alerta de severidade 12 gerado
- 10:24 — IP classificado como suspeito após correlação

---

## 5. Impacto

Até o momento, não há evidências de comprometimento bem-sucedido.
Impacto classificado como potencial tentativa de acesso não autorizado.

---

## 6. Recomendações

- Bloquear IP no firewall
- Implementar fail2ban
- Revisar política de senhas
- Habilitar autenticação por chave SSH
- Monitoramento reforçado por 24h

---

## 7. Status do Incidente

Incidente em fase de contenção.
Monitoramento ativo mantido.