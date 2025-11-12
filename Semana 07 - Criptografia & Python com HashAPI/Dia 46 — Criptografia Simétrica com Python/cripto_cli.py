#!/usr/bin/env python3
"""
cripto_cli.py — Sistema de criptografia simétrica com Fernet (AES + HMAC)

Funções:
1. Gera uma chave e salva em chave.key
2. Criptografa arquivos
3. Decifra arquivos

Requisitos:
    pip install cryptography
"""

from cryptography.fernet import Fernet
from pathlib import Path


# =========================
# 🔹 Funções principais
# =========================

def gerar_chave():
    """Gera uma nova chave e salva em chave.key"""
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as arquivo:
        arquivo.write(chave)
    print("✅ Chave gerada e salva em 'chave.key'\n")


def carregar_chave():
    """Carrega a chave existente"""
    path = Path("chave.key")
    if not path.exists():
        print("❌ Arquivo 'chave.key' não encontrado! Gere uma nova chave primeiro.\n")
        return None
    return path.read_bytes()


def criptografar_arquivo(nome_arquivo):
    """Criptografa o arquivo especificado"""
    chave = carregar_chave()
    if not chave:
        return
    fernet = Fernet(chave)

    try:
        with open(nome_arquivo, "rb") as f:
            dados = f.read()
        criptografado = fernet.encrypt(dados)

        nome_saida = nome_arquivo + ".enc"
        with open(nome_saida, "wb") as f:
            f.write(criptografado)

        print(f"🔒 Arquivo '{nome_arquivo}' criptografado como '{nome_saida}'\n")
    except FileNotFoundError:
        print("❌ Arquivo não encontrado!\n")
    except Exception as e:
        print(f"⚠️ Erro ao criptografar: {e}\n")


def descriptografar_arquivo(nome_arquivo):
    """Decifra o arquivo especificado"""
    chave = carregar_chave()
    if not chave:
        return
    fernet = Fernet(chave)

    try:
        with open(nome_arquivo, "rb") as f:
            dados = f.read()
        descriptografado = fernet.decrypt(dados)

        nome_saida = nome_arquivo.replace(".enc", "")
        with open(nome_saida, "wb") as f:
            f.write(descriptografado)

        print(f"🔓 Arquivo '{nome_arquivo}' decifrado como '{nome_saida}'\n")
    except FileNotFoundError:
        print("❌ Arquivo não encontrado!\n")
    except Exception as e:
        print(f"⚠️ Erro ao decifrar: {e}\n")


# =========================
# 🔹 Interface CLI
# =========================

def menu():
    print("""
=== 🔐 Menu Criptografia ===
1. Gerar nova chave
2. Criptografar arquivo
3. Decifrar arquivo
0. Sair
""")

    while True:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerar_chave()

        elif opcao == "2":
            nome = input("Digite o nome do arquivo a criptografar: ").strip()
            criptografar_arquivo(nome)

        elif opcao == "3":
            nome = input("Digite o nome do arquivo a decifrar (.enc): ").strip()
            descriptografar_arquivo(nome)

        elif opcao == "0":
            print("👋 Encerrando o programa...")
            break

        else:
            print("❌ Opção inválida!\n")

        print("=" * 40)
        menu()  # Mostra o menu novamente após cada ação


if __name__ == "__main__":
    menu()

