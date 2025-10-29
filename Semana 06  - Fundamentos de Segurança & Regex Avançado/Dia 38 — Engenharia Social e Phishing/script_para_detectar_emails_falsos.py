import re

with open("mail.log", "r") as f:
    logs = f.read()

# Detectar URLs suspeitas
pattern = r"https?:\/\/(?!www\.).*\.xyz|\.ru|\.top|\.info"
suspeitos = re.findall(pattern, logs)

print("URLs suspeitas encontradas:")
for url in suspeitos:
    print("-", url)
