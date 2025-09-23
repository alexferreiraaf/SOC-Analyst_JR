# contador_palavras.py

# Solicita arquivo e palavra
arquivo = input("Digite o nome do arquivo (ex: texto.txt): ")
palavra = input("Digite a palavra a contar: ")

# Lê o arquivo
with open(arquivo, "r", encoding="utf-8") as f:
    conteudo = f.read()

# Conta ocorrências
qtd = conteudo.lower().count(palavra.lower())

print(f"A palavra '{palavra}' aparece {qtd} vezes no arquivo.")
