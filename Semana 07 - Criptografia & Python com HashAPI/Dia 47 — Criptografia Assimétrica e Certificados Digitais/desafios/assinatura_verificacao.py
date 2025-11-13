from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
import sys, os

def carregar_chaves():
    """Carrega a chave privada e pública do diretório atual."""
    with open("private.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)
    with open("public.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())
    return private_key, public_key

def assinar_arquivo(private_key, arquivo):
    """Gera assinatura digital do arquivo."""
    with open(arquivo, "rb") as f:
        dados = f.read()
    assinatura = private_key.sign(
        dados,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    with open("assinatura.bin", "wb") as f:
        f.write(assinatura)
    print(f"✅ Assinatura gerada: assinatura.bin")

def verificar_assinatura(public_key, arquivo):
    """Verifica a assinatura digital."""
    with open(arquivo, "rb") as f:
        dados = f.read()
    with open("assinatura.bin", "rb") as f:
        assinatura = f.read()
    try:
        public_key.verify(
            assinatura,
            dados,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("✅ Assinatura válida")
    except InvalidSignature:
        print("❌ Falha na verificação")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python assinatura_verificacao.py <arquivo>")
        sys.exit(1)

    arquivo = sys.argv[1]
    if not os.path.exists(arquivo):
        print(f"❌ Arquivo '{arquivo}' não encontrado.")
        sys.exit(1)

    private_key, public_key = carregar_chaves()
    assinar_arquivo(private_key, arquivo)
    verificar_assinatura(public_key, arquivo)

