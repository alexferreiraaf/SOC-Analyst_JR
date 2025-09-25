# regex_fundamentos.py
import re

texto = "IP: 192.168.0.1 Email: teste@mail.com Data: 2025-09-10"

# Datas no formato YYYY-MM-DD
print("Datas:", re.findall(r"\d{4}-\d{2}-\d{2}", texto))

# IPv4 (não valida faixa 0–255, mas extrai padrões básicos)
print("IPs:", re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", texto))

# E-mails
print("E-mails:", re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto))
