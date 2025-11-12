import hashlib
import json
from cryptography.fernet import Fernet
from pathlib import Path

ARQUIVO_CHAVE = "chave.key"
ARQUIVO_SENHA = "senha.hash"
ARQUIVO_MENSAGENS = "mensagens.json"


# 🔑 Função para gerar chave
def gerar_chave():
    chave = Fernet.generate_key()
    with open(ARQUIVO_CHAVE, "wb") as f:
        f.write(chave)
    print("✅ Chave gerada e salva em chave.key")
    return chave


# 🔐 Função para carregar chave existente
def carregar_chave():
    if not Path(ARQUIVO_CHAVE).exists():
        print("⚠️ Nenhuma chave encontrada. Gerando nova...")
        return gerar_chave()
    with open(ARQUIVO_CHAVE, "rb") as f:
        return f.read()


# 🧠 Função para criar senha mestra (com hash)
def criar_senha():
    senha = input("Crie uma senha mestra: ").encode()
    hash_senha = hashlib.sha256(senha).hexdigest()
    with open(ARQUIVO_SENHA, "w") as f:
        f.write(hash_senha)
    print("✅ Senha mestra criada com sucesso!")


# 🔎 Função para verificar senha mestra
def verificar_senha():
    if not Path(ARQUIVO_SENHA).exists():
        print("⚠️ Nenhuma senha mestra encontrada. Vamos criar uma!")
        criar_senha()

    senha = input("Digite a senha mestra: ").encode()
    hash_dig = hashlib.sha256(senha).hexdigest()

    with open(ARQUIVO_SENHA, "r") as f:
        hash_salvo = f.read()

    if hash_dig == hash_salvo:
        print("🔓 Acesso concedido!\n")
        return True
    else:
        print("❌ Senha incorreta!")
        return False


# 💬 Adicionar mensagem ao cofre
def adicionar_mensagem():
    chave = carregar_chave()
    fernet = Fernet(chave)

    mensagem = input("Digite a mensagem secreta: ").encode()
    criptografada = fernet.encrypt(mensagem)

    if Path(ARQUIVO_MENSAGENS).exists():
        with open(ARQUIVO_MENSAGENS, "r") as f:
            mensagens = json.load(f)
    else:
        mensagens = []

    mensagens.append(criptografada.decode())

    with open(ARQUIVO_MENSAGENS, "w") as f:
        json.dump(mensagens, f, indent=4)

    print("✅ Mensagem armazenada com sucesso!\n")


# 📖 Ler mensagens do cofre
def ler_mensagens():
    chave = carregar_chave()
    fernet = Fernet(chave)

    if not Path(ARQUIVO_MENSAGENS).exists():
        print("📭 Nenhuma mensagem salva ainda.")
        return

    with open(ARQUIVO_MENSAGENS, "r") as f:
        mensagens = json.load(f)

    print("\n=== 💌 Mensagens no Cofre ===")
    for i, msg_enc in enumerate(mensagens, 1):
        try:
            msg = fernet.decrypt(msg_enc.encode()).decode()
            print(f"{i}. {msg}")
        except:
            print(f"{i}. ❌ Erro ao decifrar (chave incorreta?)")
    print("=============================\n")


# 🧩 Menu principal
def menu():
    print("""
=== 🔐 Cofre de Mensagens ===
1. Adicionar mensagem
2. Ler mensagens
3. Sair
""")

    while True:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_mensagem()
        elif opcao == "2":
            ler_mensagens()
        elif opcao == "3":
            print("👋 Saindo do cofre...")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


# 🚀 Execução principal
if __name__ == "__main__":
    print("=== Acesso ao Cofre de Mensagens ===")
    if verificar_senha():
        menu()

