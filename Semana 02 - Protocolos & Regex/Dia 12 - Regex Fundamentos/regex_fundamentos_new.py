import re
with open("sample.txt", "r", encoding="utf-8") as f:
    texto = f.read()

print("Datas:", re.findall(r"\d{4}-\d{2}-\d{2}", texto))
print("IPs:", re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", texto))
print("E-mails:", re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto))
