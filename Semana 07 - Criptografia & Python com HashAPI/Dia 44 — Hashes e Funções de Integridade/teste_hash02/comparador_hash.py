import hashlib

def hash_arquivo(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(4096), b""):
            h.update(bloco)
    return h.hexdigest()

orig = hash_arquivo("arquivo_original.txt")
novo = hash_arquivo("arquivo_modificado.txt")

if orig == novo:
    print("✅ Arquivos idênticos!")
else:
    print("⚠️ Arquivos diferentes!")


