import hashlib
from cryptography.fernet import Fernet
from pathlib import Path

# === 1️⃣ Solicita o nome do arquivo ===
arquivo = input("Digite o nome do arquivo: ")
path = Path(arquivo)

if not path.exists():
    print("❌ Arquivo não encontrado!")
    exit()

# === 2️⃣ Gera o hash SHA256 do conteúdo ===
conteudo = path.read_bytes()
hash_sha256 = hashlib.sha256(conteudo).hexdigest()

# === 3️⃣ Gera uma chave Fernet e criptografa o arquivo ===
chave = Fernet.generate_key()
fernet = Fernet(chave)
criptografado = fernet.encrypt(conteudo)

# Salva o arquivo criptografado
arquivo_saida = arquivo + ".enc"
with open(arquivo_saida, "wb") as f:
    f.write(criptografado)

# === 4️⃣ Exibe os resultados ===
print("\n🔐 Resultado Final:")
print(f"SHA256 original: {hash_sha256}")
print(f"Arquivo criptografado: {arquivo_saida}")
print(f"Chave gerada (guarde com segurança!): {chave.decode()}")

