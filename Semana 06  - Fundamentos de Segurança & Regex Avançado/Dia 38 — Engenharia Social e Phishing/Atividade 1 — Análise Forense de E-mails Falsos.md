# Perguntas do exercício — respostas (com base nos e-mails de laboratório)

## O domínio é legítimo?
`portal-seguranca.example` e `labcorp.test` são **domínios fictícios** usados no laboratório.  
Em ambiente real, domínios desconhecidos ou com TLDs suspeitos devem ser considerados **não legítimos até verificação** (verificar SPF/DKIM/DMARC, WHOIS e reputação).

## Há URLs encurtadas?
Nos exemplos fornecidos **não há URL encurtada**. Há, porém, uma URL com TLD `.invalid` (uso seguro para laboratório).  
Em geral, **URLs encurtadas** (bit.ly, tinyurl, etc.) **aumentam o risco** — sempre expanda e verifique antes de clicar.

## Há urgência ou ameaças?
**Sim.** O primeiro e-mail usa urgência ("redefina sua senha dentro das próximas 24 horas") para pressionar ação imediata — uma técnica clássica de engenharia social / phishing.

## O e-mail contém anexos executáveis?
O segundo e-mail contém um anexo `Fatura_Abril_2025.pdf` codificado em base64.  
- Em laboratório esse anexo é **placeholder**.  
- Em ambiente real, verifique se o PDF contém **objetos executáveis** (macros, links para payloads) ou se foi **renomeado** (ex.: `fatura.pdf.exe`).  
- **Nunca abrir anexos suspeitos** fora de um ambiente sandbox — primeiro analise em sandbox ou emito hash e consulte VirusTotal.
