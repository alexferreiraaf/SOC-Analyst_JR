import hashlib

texto = "Segredo123"
hash_md5 = hashlib.md5(texto.encode()).hexdigest()
hash_sha256 = hashlib.sha256(texto.encode()).hexdigest()

print("MD5:", hash_md5)
print("SHA256:", hash_sha256)
