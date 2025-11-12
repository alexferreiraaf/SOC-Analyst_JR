import hashlib
from pathlib import Path

arquivo = Path("teste.txt")

if arquivo.exists():
    conteudo = arquivo.read_bytes()  # Lê o arquivo em bytes
    hash_md5 = hashlib.md5(conteudo).hexdigest()
    hash_sha1 = hashlib.sha1(conteudo).hexdigest()
    hash_sha256 = hashlib.sha256(conteudo).hexdigest()

    print(f"MD5: {hash_md5}")
    print(f"SHA1: {hash_sha1}")
    print(f"SHA256: {hash_sha256}")
else:
    print("❌ Arquivo não encontrado!")


