# Dia 82 — Análise de Qualidade da Detecção SOC

## Objetivo
Avaliar se a detecção de brute force em SSH possui **qualidade suficiente** para gerar um alerta confiável em ambiente SOC, reduzindo falsos positivos e priorizando riscos reais.

---

## Contexto da Detecção
A detecção foi refinada considerando:
- Usuários críticos (root, admin)
- Horários suspeitos (fora do expediente)
- Exclusão de IPs locais/confiáveis
- Volume mínimo de tentativas

Esses critérios seguem boas práticas de SOC N1/N2.

---

## Avaliação por Critério

### 1. IP Externo
**Status:** Atendido  
IPs identificados não pertencem à rede interna nem loopback.

**Impacto SOC:**  
Ataques externos possuem maior probabilidade de serem maliciosos e exigem resposta mais rápida.

---

### 2. Usuário Crítico
**Status:** Atendido  
As tentativas focam usuários privilegiados como `root` e `admin`.

**Impacto SOC:**  
Comprometimento dessas contas gera impacto alto no ambiente.

---

### 3. Horário Suspeito
**Status:** Atendido  
Eventos concentrados durante madrugada (00h–06h).

**Impacto SOC:**  
Atividades fora do horário comercial aumentam a probabilidade de automação maliciosa.

---

### 4. Volume de Tentativas
**Status:** Atendido  
Quantidade de falhas excede o comportamento esperado de erro humano.

**Impacto SOC:**  
Volume elevado em curto intervalo caracteriza brute force.

---

## Análise Final SOC

A detecção analisada:
- ❌ Não é ruído
- ❌ Não é erro isolado
- ✅ É comportamento anômalo consistente
- ✅ Possui contexto suficiente para alerta

---

## Classificação do Incidente

- **Tipo:** Tentativa de Brute Force SSH  
- **Severidade:** Média → Alta  
- **Confiança:** Alta  

---

## Ação Recomendada

- Bloqueio temporário do IP atacante
- Implementação ou ajuste de fail2ban
- Hardening de SSH (desabilitar root login, mudar porta, MFA se possível)
- Monitoramento contínuo

---

## Conclusão SOC

> Uma boa detecção não é a que gera mais alertas,  
> é a que gera **alertas certos**.

Este refinamento transforma volume de logs em **decisão operacional confiável**, alinhada à realidade de SOCs profissionais.
