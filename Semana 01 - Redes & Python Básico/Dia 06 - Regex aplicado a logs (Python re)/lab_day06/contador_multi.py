import csv

palavras = input("Digite palavras separadas por vírgula: ").split(",")
arquivo = input("Arquivo: ")

conteudo = open(arquivo, encoding="utf-8").read().lower()

resultados = []
for p in palavras:
    p = p.strip().lower()
    cont = conteudo.count(p)
    resultados.append((p, cont))

with open("counts.csv", "w", newline="", encoding="utf-8") as csvf:
    writer = csv.writer(csvf)
    writer.writerow(["palavra", "quantidade"])
    writer.writerows(resultados)

print("Counts salvos em counts.csv")
