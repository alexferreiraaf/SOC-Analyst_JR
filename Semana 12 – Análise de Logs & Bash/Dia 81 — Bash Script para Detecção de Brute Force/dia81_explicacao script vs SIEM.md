# Dia 81 — Comparação: Script Bash vs Alerta de SIEM

## Qual a diferença entre esse script e um alerta de SIEM?

### Script Bash (Detecção Manual Automatizada)

O script Bash é uma automação **local**, executada diretamente no servidor, analisando arquivos de log específicos.

**Características:**
- Execução manual ou via cron
- Atua em um único host
- Não realiza correlação entre múltiplas fontes
- Ideal para resposta rápida e ambientes sem SIEM

**Uso em SOC:**
- Triagem inicial
- Investigação emergencial
- Confirmação de suspeitas
- Hardening e validação local

---

### Alerta de SIEM (Detecção Centralizada)

O alerta de SIEM é uma detecção **automática e contínua**, baseada em logs centralizados de vários sistemas.

**Características:**
- Execução automática
- Correlaciona múltiplas fontes
- Integração com alertas, tickets e SOAR
- Suporte a métricas e auditoria

**Uso em SOC:**
- Monitoramento contínuo
- Detecção em escala
- Priorização de incidentes
- Governança e compliance

---

## Comparação Direta

| Aspecto | Script Bash | Alerta SIEM |
|------|------------|------------|
| Execução | Manual | Automática |
| Escopo | Um servidor | Ambiente inteiro |
| Correlação | Não | Sim |
| Velocidade local | Muito alta | Média |
| Escalabilidade | Baixa | Alta |
| Governança | Não | Sim |

---

## Conclusão SOC

O script Bash não substitui um SIEM, mas é essencial para investigação local e resposta rápida.

Um SOC maduro utiliza:
- **SIEM para detecção**
- **Bash para investigação e resposta**

> Antes do alerta, vem a análise. Antes da automação, vem o entendimento.
