import hashlib

def gerar_hash(nome_arquivo):
    with open(nome_arquivo, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

arq1 = input("Arquivo 1: ")
arq2 = input("Arquivo 2: ")

hash1 = gerar_hash(arq1)
hash2 = gerar_hash(arq2)

if hash1 == hash2:
    print("✅ Os arquivos são idênticos (mesmo conteúdo).")
else:
    print("⚠️ Os arquivos são diferentes!")


