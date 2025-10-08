# arquivos_teste.py
def exemplo_basico():
    # escrever
    with open("teste.txt", "w", encoding="utf-8") as f:
        f.write("Primeira linha\n")
        f.write("Segunda linha\n")

    # ler
    with open("teste.txt", "r", encoding="utf-8") as f:
        linhas = f.readlines()
        print("Conteúdo do arquivo:", linhas)

if __name__ == "__main__":
    exemplo_basico()

