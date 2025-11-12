import hashlib

# Função para gerar diferentes tipos de hash
def gerar_hashes(caminho_arquivo):
    try:
        with open(caminho_arquivo, "rb") as arquivo:
            conteudo = arquivo.read()

            # Gera os três tipos de hash
            hash_md5 = hashlib.md5(conteudo).hexdigest()
            hash_sha1 = hashlib.sha1(conteudo).hexdigest()
            hash_sha256 = hashlib.sha256(conteudo).hexdigest()

            # Exibe os resultados
            print(f"\n📂 Arquivo: {caminho_arquivo}")
            print(f"MD5:    {hash_md5}")
            print(f"SHA1:   {hash_sha1}")
            print(f"SHA256: {hash_sha256}")

    except FileNotFoundError:
        print("❌ Arquivo não encontrado. Verifique o nome e o caminho.")
    except Exception as e:
        print(f"⚠️ Erro inesperado: {e}")

# Entrada do usuário
arquivo = input("Digite o nome do arquivo (ex: teste.txt): ")
gerar_hashes(arquivo)

