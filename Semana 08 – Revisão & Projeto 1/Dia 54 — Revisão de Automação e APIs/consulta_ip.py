import requests

# 1. Definição do Alvo e URL
# Vamos usar o DNS do Google (8.8.8.8) como exemplo
alvo = "8.8.8.8"
url = f"https://ipinfo.io/{alvo}/json"

print(f"🔍 Consultando informações para: {alvo}...\n")

try:
    # 2. Fazendo a Requisição GET
    response = requests.get(url)

    # 3. Verificando se deu certo (Status 200 = OK)
    if response.status_code == 200:
        # Transforma a resposta JSON em um dicionário Python
        data = response.json()

        # 4. Exibindo os dados solicitados
        print("="*30)
        print(f"IP:           {data.get('ip')}")
        print(f"Cidade:       {data.get('city')}")
        print(f"Região:       {data.get('region')}")
        print(f"País:         {data.get('country')}")
        print(f"Organização:  {data.get('org')}")
        print("="*30)
        
    else:
        print(f"❌ Erro na consulta. Código HTTP: {response.status_code}")

except Exception as e:
    print(f"❌ Ocorreu um erro inesperado: {e}")