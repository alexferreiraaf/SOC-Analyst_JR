import hashlib
import csv
from datetime import datetime
from pathlib import Path

arquivo = input("Digite o nome do arquivo: ")
path = Path(arquivo)

if not path.exists():
    print("❌ Arquivo não encontrado!")
else:
    conteudo = path.read_bytes()

    hashes = {
        "MD5": hashlib.md5(conteudo).hexdigest(),
        "SHA1": hashlib.sha1(conteudo).hexdigest(),
        "SHA256": hashlib.sha256(conteudo).hexdigest()
    }

    print(f"\n🔐 Hashes de {arquivo}:\n")
    for nome, valor in hashes.items():
        print(f"{nome}: {valor}")

    with open("hash_resultados.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([arquivo, datetime.now(), *hashes.values()])

    print("\n✅ Resultados salvos em hash_resultados.csv")


