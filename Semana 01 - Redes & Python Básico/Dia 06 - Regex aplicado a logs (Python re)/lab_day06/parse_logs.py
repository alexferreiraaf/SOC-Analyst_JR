import re

# Padrões
ip_re = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
email_re = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

# Leitura do log
with open("sample_log.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extração
ips = ip_re.findall(text)
emails = email_re.findall(text)

print("IPs encontrados:", set(ips))
print("Emails encontrados:", set(emails))
