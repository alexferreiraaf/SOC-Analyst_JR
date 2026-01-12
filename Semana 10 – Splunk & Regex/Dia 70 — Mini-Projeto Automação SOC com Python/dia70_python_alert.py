import re
from collections import Counter

with open("auth.log", encoding="utf-8") as f:
    log = f.read()

ips = re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", log)
contador = Counter(ips)

print("=== ALERTAS SOC ===")
for ip, count in contador.items():
    if count > 10:
        print(f"[ALERTA] Possível brute force detectado")
        print(f"IP: {ip}")
        print(f"Tentativas: {count}")
        print("Ação recomendada: Bloqueio temporário e investigação")
        print("-" * 40)
