import os
import hashlib
import json
import csv
import urllib.request
import urllib.error

# ==============================
# CONFIGURAÇÕES
# ==============================
API_KEY = ""  # substitua pela sua chave pessoal do VirusTotal
PASTA_ANALISAR = "./arquivos_teste"  # caminho da pasta com os arquivos
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
    """Consulta o VirusTotal via API v3 sem requests."""
    url = f"https://www.virustotal.com/api/v3/files/{hash_arquivo}"
    req = urllib.request.Request(url, headers={"x-apikey": API_KEY})
    try:
        with urllib.request.urlopen(req, timeout=10) as resposta:
            dados = json.loads(resposta.read().decode())
            return dados
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"erro": "Hash não encontrado na base do VirusTotal"}
        else:
            return {"erro": f"HTTPError {e.code}"}
    except Exception as e:
        return {"erro": str(e)}


def analisar_arquivo(caminho_arquivo):
    """Analisa um único arquivo e retorna as informações consolidadas."""
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

    stats = resultado["data"]["attributes"]["last_analysis_stats"]
    maliciosos = stats.get("malicious", 0)
    limpos = stats.get("harmless", 0)

    return {
        "arquivo": nome,
        "hash": hash_arquivo,
        "status": "OK",
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

    resultados = []

    for arquivo in arquivos:
        caminho = os.path.join(PASTA_ANALISAR, arquivo)
        print(f"➡️  Analisando: {arquivo}")
        dados = analisar_arquivo(caminho)
        resultados.append(dados)

    # Salvar em JSON
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as fjson:
        json.dump(resultados, fjson, indent=4, ensure_ascii=False)

    # Salvar em CSV
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as fcsv:
        writer = csv.writer(fcsv)
        writer.writerow(["arquivo", "hash", "status", "malicious", "harmless"])
        for r in resultados:
            writer.writerow([r["arquivo"], r["hash"], r["status"], r["malicious"], r["harmless"]])

    print("\n✅ Análise concluída!")
    print(f"📄 Relatórios salvos em: {ARQUIVO_JSON} e {ARQUIVO_CSV}")


if __name__ == "__main__":
    main()

