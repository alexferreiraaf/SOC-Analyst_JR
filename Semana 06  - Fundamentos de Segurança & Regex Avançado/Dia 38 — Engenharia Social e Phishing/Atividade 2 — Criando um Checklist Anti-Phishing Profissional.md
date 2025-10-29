# 🛡️ Atividade 2 — Checklist Anti-Phishing Profissional

Um checklist serve como guia rápido para **detecção e validação de e-mails suspeitos**.  
Antes de clicar em qualquer link ou abrir anexos, um analista SOC deve seguir os passos abaixo:

---

## ✅ **Checklist Anti-Phishing (10 Itens)**

1. **Domínio** — O domínio do remetente corresponde exatamente ao site oficial da organização?  
   (Ex.: `@banco.com` ≠ `@banco-seguro.com`)

2. **Erros de ortografia e gramática** — Há erros sutis que indicam tradução automática ou texto não profissional?

3. **E-mail corporativo** — O remetente usa um endereço institucional (ex.: `@empresa.com.br`) ou genérico (`@gmail.com`)?

4. **HTTPS e certificado válido** — O link fornecido usa HTTPS e o certificado pertence à organização legítima?

5. **Urgência / chantagem** — A mensagem pressiona o usuário com frases como “última chance”, “conta será bloqueada” ou “ação imediata”?

6. **Solicitação de dados sensíveis** — O e-mail pede senhas, CPF, tokens ou informações de pagamento?

7. **Reputação do IP / domínio** — O IP de origem aparece em blacklists conhecidas (Spamhaus, AbuseIPDB)?

8. **Anexos** — Há anexos executáveis, scripts, ou arquivos compactados (`.exe`, `.js`, `.zip`, `.bat`)?

9. **Links ocultos em imagens** — As imagens ou botões contêm hiperlinks diferentes do texto visível?

10. **Cabeçalhos inconsistentes** — Há divergência entre o domínio do `From:` e o domínio em `Return-Path:` ou `Reply-To:`?

---

📌 **Dica prática:**  
Antes de qualquer ação, **analise o cabeçalho completo** e **valide os domínios via WHOIS** e **VirusTotal**.  
Evite abrir anexos ou clicar em links até a origem ser confirmada.
