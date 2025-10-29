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

# Relatório — Análise Forense de E-mails Falsos (Simulação)

## Resumo executivo
<<resumo curto>>

## Metodologia
1. Abrir e-mails `.eml` em view RAW.
2. Capturar prints: `print_email1.png`, `print_email2.png`.
3. Extrair cabeçalhos para `headers_email1.txt`, `headers_email2.txt`.
4. Buscar logs: `Select-String -Path "C:\logs\mail.log" -Pattern "login failed","unauthorized","unknown domain"`

## Evidências
- Print Email 1: `print_email1.png`
- Print Email 2: `print_email2.png`
- Headers email1: `headers_email1.txt`
- Headers email2: `headers_email2.txt`
- Resultado busca logs: `log_search_result.txt`

## Tabela de sinais de fraude
| E-mail | Sinal | Evidência |
| --- | --- | --- |
| phish_redefinicao_senha.eml | Domínio suspeito | `portal-seguranca.example` |
| phish_redefinicao_senha.eml | Urgência | "redefina sua senha dentro das próximas 24 horas" |
| fatura_april2025.eml | Anexo em base64 | `Fatura_Abril_2025.pdf` (analise em sandbox) |

## Análise de cabeçalhos
- Received: <<observações>>
- Return-Path: <<observações>>
- Reply-To: <<observações>>
- SPF/DKIM/DMARC: <<status>>

## Saída dos logs (trecho)



## Conclusão e recomendações
<<ações imediatas, next steps, mitigations>>

## Arquivos anexos entregues
- `phish_redefinicao_senha.eml`
- `fatura_april2025.eml`
- `print_email1.png`, `print_email2.png`
- `headers_email1.txt`, `headers_email2.txt`
- `log_search_result.txt`

