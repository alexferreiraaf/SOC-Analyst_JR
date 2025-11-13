import os
import hashlib
import json
import csv
import urllib.request
import urllib.error
import time

# ==============================
# CONFIGURAÇÕES
# ==============================
API_KEY = ""  # substitua pela sua chave do VirusTotal
PASTA_ANALISAR = "./arquivos_teste"
ARQUIVO_JSON = "relatorio_multiplos.json"
ARQUIVO_CSV = "relatorio_multiplos.csv"

# ==============================
# FUNÇÕES AUXILIARES
# ==============================

def gerar_hash_sha256(caminho_arquivo):
    """Gera o hash SHA256 de um arquivo."""
    with open(caminho_arquivo, "rb") as f:
        conteudo = f.read()
    return hashlib.sha256(conteudo).hexdigest()


def consultar_virustotal(hash_arquivo):
    """Consulta o VirusTotal via API v3 (sem requests) e trata erros."""
    url = f"https://www.virustotal.com/api/v3/files/{hash_arquivo}"
    req = urllib.request.Request(url, headers={"x-apikey": API_KEY})
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resposta:
            if resposta.status == 429:
                print("⚠️  Limite de requisições atingido (HTTP 429). Aguardando 60 segundos...")
                time.sleep(60)
                return consultar_virustotal(hash_arquivo)

            dados_bytes = resposta.read()
            try:
                dados = json.loads(dados_bytes.decode())
                return dados
            except json.JSONDecodeError:
                return {"erro": "Erro ao decodificar JSON retornado"}
    
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"erro": "Hash não encontrado na base do VirusTotal"}
        elif e.code == 429:
            print("⚠️  Muitas requisições — aguardando 60 segundos...")
            time.sleep(60)
            return consultar_virustotal(hash_arquivo)
        else:
            return {"erro": f"HTTPError {e.code}"}

    except urllib.error.URLError as e:
        return {"erro": f"Erro de rede: {e.reason}"}
    except TimeoutError:
        return {"erro": "Tempo de requisição excedido"}
    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}


def analisar_arquivo(caminho_arquivo):
    """Analisa um único arquivo e retorna os dados formatados."""
    nome = os.path.basename(caminho_arquivo)
    hash_arquivo = gerar_hash_sha256(caminho_arquivo)
    resultado = consultar_virustotal(hash_arquivo)

    if "erro" in resultado:
        return {
            "arquivo": nome,
            "hash": hash_arquivo,
            "status": resultado["erro"],
            "malicious": None,
            "harmless": None
        }

    try:
        stats = resultado["data"]["attributes"]["last_analysis_stats"]
        maliciosos = stats.get("malicious", 0)
        limpos = stats.get("harmless", 0)
        status = "OK"
    except KeyError:
        maliciosos = limpos = 0
        status = "Formato inesperado de resposta"

    return {
        "arquivo": nome,
        "hash": hash_arquivo,
        "status": status,
        "malicious": maliciosos,
        "harmless": limpos
    }


# ==============================
# EXECUÇÃO PRINCIPAL
# ==============================
def main():
    print("🔍 Iniciando verificação de múltiplos arquivos...\n")

    arquivos = [f for f in os.listdir(PASTA_ANALISAR)
                if os.path.isfile(os.path.join(PASTA_ANALISAR, f))]

    if not arquivos:
        print("⚠️  Nenhum arquivo encontrado na pasta especificada.")
        return

    resultados = []

    for idx, arquivo in enumerate(arquivos, start=1):
        caminho = os.path.join(PASTA_ANALISAR, arquivo)
        print(f"[{idx}/{len(arquivos)}] Analisando: {arquivo}")
        dados = analisar_arquivo(caminho)
        resultados.append(dados)
        time.sleep(15)  # atraso leve entre requisições (boa prática)

    # Salvar JSON
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as fjson:
        json.dump(resultados, fjson, indent=4, ensure_ascii=False)

    # Salvar CSV
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as fcsv:
        writer = csv.writer(fcsv)
        writer.writerow(["arquivo", "hash", "status", "malicious", "harmless"])
        for r in resultados:
            writer.writerow([r["arquivo"], r["hash"], r["status"], r["malicious"], r["harmless"]])

    print("\n✅ Análise concluída com sucesso!")
    print(f"📄 Relatórios gerados: {ARQUIVO_JSON} e {ARQUIVO_CSV}")


if __name__ == "__main__":
    main()

