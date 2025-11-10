from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import hashlib

# --- 1️⃣ Gerar par de chaves RSA ---
def gerar_chaves():
    chave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    chave_publica = chave_privada.public_key()

    # Salvar em arquivos PEM
    with open("chave_privada.pem", "wb") as f:
        f.write(chave_privada.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open("chave_publica.pem", "wb") as f:
        f.write(chave_publica.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("✅ Par de chaves RSA gerado com sucesso!")
    return chave_privada, chave_publica


# --- 2️⃣ Criptografar com a chave pública ---
def criptografar_mensagem(mensagem, chave_publica):
    ciphertext = chave_publica.encrypt(
        mensagem.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    with open("mensagem_criptografada.bin", "wb") as f:
        f.write(ciphertext)
    print("🔐 Mensagem criptografada e salva em 'mensagem_criptografada.bin'")
    return ciphertext


# --- 3️⃣ Descriptografar com a chave privada ---
def descriptografar_mensagem(chave_privada, ciphertext):
    plaintext = chave_privada.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()


# --- 4️⃣ Validar integridade com SHA256 ---
def validar_integridade(original, descriptografado):
    hash_original = hashlib.sha256(original.encode()).hexdigest()
    hash_descriptografado = hashlib.sha256(descriptografado.encode()).hexdigest()

    print("\n🧾 Hash Original:       ", hash_original)
    print("🧾 Hash Descriptografado:", hash_descriptografado)

    if hash_original == hash_descriptografado:
        print("✅ Integridade confirmada: os dados não foram alterados!")
    else:
        print("⚠️ Integridade comprometida: os dados foram modificados!")


# --- Execução Principal ---
if __name__ == "__main__":
    chave_privada, chave_publica = gerar_chaves()

    mensagem = input("\nDigite a mensagem a ser criptografada: ")
    cifrada = criptografar_mensagem(mensagem, chave_publica)

    descriptografada = descriptografar_mensagem(chave_privada, cifrada)

    print("\n🔓 Mensagem descriptografada:", descriptografada)
    validar_integridade(mensagem, descriptografada)

