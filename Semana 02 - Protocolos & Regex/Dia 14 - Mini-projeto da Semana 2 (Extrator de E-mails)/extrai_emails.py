import re

# Lê o arquivo com os textos
with open("emails_dataset.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# Regex para capturar e-mails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto)

# Salva os resultados em um novo arquivo
with open("emails_encontrados.txt", "w", encoding="utf-8") as f:
    for e in sorted(set(emails)):   # remove duplicados e ordena
        f.write(e + "\n")

print("Total encontrados:", len(set(emails)))
