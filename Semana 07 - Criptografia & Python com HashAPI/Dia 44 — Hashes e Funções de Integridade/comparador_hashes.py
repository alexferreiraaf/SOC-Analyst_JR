import os
import hashlib
import csv

# Caminho da pasta a ser analisada
PASTA = "meus_arquivos"
ARQUIVO_CSV = "hashes01.csv"

def gerar_hash(caminho_arquivo):
    """Gera o hash SHA256 de um arquivo."""
    sha256 = hashlib.sha256()
    with open(caminho_arquivo, "rb") as f:
        for bloco in iter(lambda: f.read(4096), b""):
            sha256.update(bloco)
    return sha256.hexdigest()

def gerar_hashes():
    """Gera hashes de todos os arquivos e salva no CSV."""
    arquivos = []
    for nome_arquivo in os.listdir(PASTA):
        caminho = os.path.join(PASTA, nome_arquivo)
        if os.path.isfile(caminho):
            hash_arquivo = gerar_hash(caminho)
            arquivos.append((nome_arquivo, hash_arquivo))
    
    # Salva no CSV
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["arquivo", "hash"])
        escritor.writerows(arquivos)
    
    print("✅ Hashes gerados e salvos em", ARQUIVO_CSV)

def comparar_hashes():
    """Compara hashes atuais com o CSV salvo anteriormente."""
    if not os.path.exists(ARQUIVO_CSV):
        print("⚠️ Nenhum registro anterior encontrado. Gerando novo arquivo CSV...")
        gerar_hashes()
        return
    
    # Lê hashes antigos
    antigos = {}
    with open(ARQUIVO_CSV, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            antigos[linha["arquivo"]] = linha["hash"]

    # Gera hashes novos
    novos = {}
    for nome_arquivo in os.listdir(PASTA):
        caminho = os.path.join(PASTA, nome_arquivo)
        if os.path.isfile(caminho):
            novos[nome_arquivo] = gerar_hash(caminho)

    # Verifica diferenças
    alterados = [a for a in novos if a in antigos and novos[a] != antigos[a]]
    novos_arquivos = [a for a in novos if a not in antigos]
    removidos = [a for a in antigos if a not in novos]

    print("\n🔍 Resultado da comparação:")
    if alterados:
        print("🟡 Arquivos alterados:", ", ".join(alterados))
    if novos_arquivos:
        print("🟢 Novos arquivos:", ", ".join(novos_arquivos))
    if removidos:
        print("🔴 Arquivos removidos:", ", ".join(removidos))
    if not (alterados or novos_arquivos or removidos):
        print("✅ Nenhuma alteração detectada.")

    # Atualiza o CSV
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["arquivo", "hash"])
        for nome, hashv in novos.items():
            escritor.writerow([nome, hashv])

if __name__ == "__main__":
    comparar_hashes()

