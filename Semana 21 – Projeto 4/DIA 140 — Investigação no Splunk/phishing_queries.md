# Consultas Splunk - Investigação de Phishing

## Todos os e-mails

index=email_logs

---

## Possíveis phishing

index=email_logs subject="verify" OR subject="account"

---

## URLs suspeitas

index=email_logs url="login"

---

## Estatística por URL

index=email_logs
| stats count by url

---

## Extração de URLs

index=email_logs
| rex field=_raw "(?<url>https?://[^\s]+)"

---

## Exportação

Campos exportados:

* timestamp
* sender
* recipient
* url
