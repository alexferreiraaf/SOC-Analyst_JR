from cryptography.fernet import Fernet

# Carregar chave existente
with open("chave.key", "rb") as arquivo:
    chave = arquivo.read()

fernet = Fernet(chave)

# Entrada do usuário
mensagem = input("Digite a mensagem para cifrar: ").encode()

# Cifrar
criptografada = fernet.encrypt(mensagem)
print("\n🔒 Mensagem criptografada:", criptografada)

# Decifrar
decifrada = fernet.decrypt(criptografada)
print("🔓 Mensagem decifrada:", decifrada.decode())


