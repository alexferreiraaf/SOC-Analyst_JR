import hashlib, os, csv

def gerar_hash(arquivo, algoritmo="sha256"):
    h = hashlib.new(algoritmo)
    with open(arquivo, "rb") as f:
        for bloco in iter(lambda: f.read(4096), b""):
            h.update(bloco)
    return h.hexdigest()

with open("hashes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Arquivo", "Hash (SHA256)"])
    for arquivo in os.listdir("."):
        if os.path.isfile(arquivo):
            hash_valor = gerar_hash(arquivo)
            writer.writerow([arquivo, hash_valor])

print("✅ Arquivo 'hashes.csv' gerado com sucesso.")


