from collections import Counter
import re

ips = re.findall(r"\b\d{1,3}(\.\d{1,3}){3}\b", open("auth.log").read())

contador = Counter(ips)

for ip, count in contador.items():
    if count > 10:
        print(f"Possível brute force: {ip} ({count} tentativas)")