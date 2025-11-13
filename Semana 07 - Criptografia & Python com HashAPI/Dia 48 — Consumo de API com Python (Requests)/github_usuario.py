import requests
import json

# Solicita o nome do usuário
usuario = input("Digite o nome de usuário do GitHub: ").strip()

# Monta a URL da API
url = f"https://api.github.com/users/{usuario}"

print(f"\n🔍 Consultando dados do usuário: {usuario} ...")

# Faz a requisição GET
resposta = requests.get(url)

# Verifica se a resposta foi bem-sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    
    # Extrai os campos principais
    info = {
        "login": dados.get("login"),
        "public_repos": dados.get("public_repos"),
        "followers": dados.get("followers"),
        "created_at": dados.get("created_at")
    }

    # Exibe os resultados formatados
    print("\n✅ Dados do usuário:")
    print(f"👤 Login: {info['login']}")
    print(f"📦 Repositórios públicos: {info['public_repos']}")
    print(f"👥 Seguidores: {info['followers']}")
    print(f"🗓️ Conta criada em: {info['created_at']}")

    # Salva em arquivo JSON
    with open("github_usuario.json", "w") as f:
        json.dump(info, f, indent=4)

    print("\n💾 Dados salvos em 'github_usuario.json'")

else:
    print("\n❌ Usuário não encontrado ou erro na requisição!")
    print(f"Código HTTP: {resposta.status_code}")

