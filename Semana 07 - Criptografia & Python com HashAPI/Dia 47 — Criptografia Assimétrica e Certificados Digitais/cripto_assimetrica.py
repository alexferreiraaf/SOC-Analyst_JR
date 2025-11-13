from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Gerar chaves
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Serializar para salvar
pem_priv = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

pem_pub = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Salvar chaves
with open("private_py.pem", "wb") as f: f.write(pem_priv)
with open("public_py.pem", "wb") as f: f.write(pem_pub)

# Cifrar e decifrar
mensagem = b"Teste SOC com RSA"
cifrada = public_key.encrypt(
    mensagem,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

decifrada = private_key.decrypt(
    cifrada,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

print("Mensagem original:", mensagem)
print("Mensagem decifrada:", decifrada)


