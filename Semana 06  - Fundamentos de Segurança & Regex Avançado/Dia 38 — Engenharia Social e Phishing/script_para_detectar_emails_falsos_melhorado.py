import re

with open("mail.log", "r") as f:
    logs = f.read()

# Regex aprimorado: captura domínios com letras trocadas ou repetidas
pattern = r"https?:\/\/(?:[a-zA-Z0-9\-]*?(?:m1crosoft|micros0ft|g00gle|paypall|faceb00k)[a-zA-Z0-9\-]*\.[a-z]{2,})"
suspeitos = re.findall(pattern, logs)

print("🚨 Domínios suspeitos (typosquatting) encontrados:")
for url in suspeitos:
    print("-", url)
