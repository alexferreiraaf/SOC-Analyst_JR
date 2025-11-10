import hashlib
import csv
import os

# --- Função para gerar hashes ---
def gerar_hashes(arquivo):
    try:
        with open(arquivo, 'rb') as f:
            conteudo = f.read()
            hash_md5 = hashlib.md5(conteudo).hexdigest()
            hash_sha256 = hashlib.sha256(conteudo).hexdigest()
        return hash_md5, hash_sha256
    except FileNotFoundError:
        print(f"⚠️ Arquivo '{arquivo}' não encontrado!")
        return None, None


# --- Função para salvar no CSV ---
def salvar_hashes_csv(arquivo, hash_md5, hash_sha256):
    existe = os.path.exists('hashes.csv')
    with open('hashes.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not existe:
            writer.writerow(["Arquivo", "MD5", "SHA256"])
        writer.writerow([arquivo, hash_md5, hash_sha256])


# --- Função para comparar dois arquivos ---
def comparar_arquivos(arquivo1, arquivo2):
    h1_md5, h1_sha = gerar_hashes(arquivo1)
    h2_md5, h2_sha = gerar_hashes(arquivo2)

    if not h1_sha or not h2_sha:
        return

    print(f"\n🔍 Comparando arquivos:\n- {arquivo1}\n- {arquivo2}")
    if h1_sha == h2_sha:
        print("✅ Os arquivos são idênticos (hashes iguais)")
    else:
        print("⚠️ Os arquivos são diferentes (hashes diferentes)")


# --- Programa principal ---
if __name__ == "__main__":
    arquivo = input("Digite o nome do arquivo para gerar hash: ")
    md5, sha256 = gerar_hashes(arquivo)

    if md5 and sha256:
        salvar_hashes_csv(arquivo, md5, sha256)
        print(f"\n✅ Hashes gerados e salvos em 'hashes.csv'")
        print(f"MD5: {md5}")
        print(f"SHA256: {sha256}")

    # --- Opção de comparação ---
    opcao = input("\nDeseja comparar dois arquivos? (s/n): ").lower()
    if opcao == 's':
        a1 = input("Arquivo 1: ")
        a2 = input("Arquivo 2: ")
        comparar_arquivos(a1, a2)

