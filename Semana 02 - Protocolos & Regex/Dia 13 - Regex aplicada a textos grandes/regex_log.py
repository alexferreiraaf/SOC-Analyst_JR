# regex_logs.py
import re

# Lê o arquivo de log
with open("log_sample.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# Regex para e-mails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto)

# Regex para IPv4
ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", texto)

print("E-mails encontrados:", set(emails))
print("IPs encontrados:", set(ips))
