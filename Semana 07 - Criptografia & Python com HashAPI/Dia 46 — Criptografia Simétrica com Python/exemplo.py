from cryptography.fernet import Fernet

# 1️⃣ Gera uma chave
chave = Fernet.generate_key()
fernet = Fernet(chave)

# 2️⃣ Cifra a mensagem
mensagem = "Segredo do SOC".encode()
criptografada = fernet.encrypt(mensagem)

# 3️⃣ Decifra
decifrada = fernet.decrypt(criptografada)

print("Chave:", chave)
print("Criptografada:", criptografada)
print("Decifrada:", decifrada.decode())


