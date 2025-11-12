senha = input("Digite sua senha: ").encode()
hash_senha = hashlib.sha256(senha).hexdigest()
print(f"Hash armazenado: {hash_senha}")

# Simulação de login
login = input("Digite novamente sua senha: ").encode()
if hashlib.sha256(login).hexdigest() == hash_senha:
    print("🔓 Senha correta!")
else:
    print("🚫 Senha incorreta!")


