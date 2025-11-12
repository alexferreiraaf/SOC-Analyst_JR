from cryptography.fernet import Fernet

def carregar_chave():
    with open("chave.key", "rb") as f:
        return f.read()

def criptografar_arquivo(nome_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)
    with open(nome_arquivo, "rb") as file:
        dados = file.read()
    criptografado = fernet.encrypt(dados)
    with open(nome_arquivo + ".enc", "wb") as file:
        file.write(criptografado)
    print(f"✅ {nome_arquivo} criptografado com sucesso!")

def descriptografar_arquivo(nome_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)
    with open(nome_arquivo, "rb") as file:
        dados = file.read()
    descriptografado = fernet.decrypt(dados)
    with open(nome_arquivo.replace(".enc", ""), "wb") as file:
        file.write(descriptografado)
    print(f"🔓 {nome_arquivo} decifrado com sucesso!")

# Teste
criptografar_arquivo("mensagem.txt")
descriptografar_arquivo("mensagem.txt.enc")


