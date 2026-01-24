# Checklist SOC — Qualidade da Detecção (Brute Force SSH)

Este checklist deve ser usado **antes de escalar um alerta** para garantir qualidade, contexto e redução de falsos positivos.

---

## 🌐 1. IP Externo?
- [ ] IP não pertence à rede interna
- [ ] IP não é localhost (127.0.0.1)
- [ ] IP não está em whitelist conhecida
- [ ] Origem geográfica inesperada (se disponível)

---

## 👤 2. Usuário Crítico?
- [ ] Usuário privilegiado (root, admin, administrator)
- [ ] Conta sensível do sistema
- [ ] Usuário aparece repetidamente nos logs

---

## ⏰ 3. Horário Suspeito?
- [ ] Fora do horário comercial
- [ ] Madrugada (00h–06h)
- [ ] Final de semana ou feriado

---

## 🔢 4. Volume Suficiente?
- [ ] Mais de X falhas (ex: >5 ou >10)
- [ ] Tentativas concentradas em curto intervalo
- [ ] Padrão repetitivo e sequencial

---

## 🚨 Decisão SOC Final

- ✅ Todos os critérios atendidos → **Brute force confirmado**
- ⚠️ Parcial → Monitorar
- ❌ Poucos critérios → Ruído

---

> Detecção boa é contextual e acionável.
