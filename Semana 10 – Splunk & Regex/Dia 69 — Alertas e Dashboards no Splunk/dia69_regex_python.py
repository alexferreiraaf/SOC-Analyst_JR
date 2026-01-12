import re
from collections import Counter

with open("auth.log", "r", encoding="utf-8") as f:
    log = f.read()

ips = re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", log)
contador = Counter(ips)

print("IPs suspeitos:")
for ip, count in contador.items():
    if count > 10:
        print(f"Possível brute force: {ip} ({count} tentativas)")
