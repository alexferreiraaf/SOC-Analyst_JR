import hashlib

def gerar_hash(arquivo):
    h = hashlib.sha256()
    with open(arquivo, 'rb') as f:
        for bloco in iter(lambda: f.read(4096), b""):
            h.update(bloco)
    return h.hexdigest()

original = gerar_hash("segredo.txt")
copia = gerar_hash("segredo_decriptado.txt")

print("Hash Original:", original)
print("Hash Cópia:", copia)

if original == copia:
    print("✅ Os arquivos são idênticos!")
else:
    print("⚠️ Arquivos foram alterados!")


