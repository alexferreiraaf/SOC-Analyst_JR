# conta_ocorrencias.py
from collections import Counter
import re

def contar_palavras(arquivo, palavras):
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read().lower()
    c = Counter()
    for p in palavras:
        c[p] = texto.count(p.lower())
    return c

if __name__ == "__main__":
    palavras = ["failed", "error", "login"]
    resultado = contar_palavras("sample_log.txt", palavras)
    print("Contagens:", resultado)
