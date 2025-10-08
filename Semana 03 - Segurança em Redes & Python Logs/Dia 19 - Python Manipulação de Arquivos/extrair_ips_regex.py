# extrair_ips_regex.py
import re

IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

def extrair(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()
    ips = set(IP_RE.findall(texto))
    return sorted(ips)

if __name__ == "__main__":
    resultado = extrair("ips_mistos.txt")
    print("IPs encontrados:", resultado)

