import csv
from urllib.parse import urlparse

ARQUIVO_ENTRADA = "../logs/extracted_urls.csv"
ARQUIVO_SAIDA = "../report/phishing_analysis.csv"


def classificar_url(dominio):
    dominio = dominio.lower()

    if "login" in dominio:
        return "HIGH"

    if "secure" in dominio:
        return "HIGH"

    if "intranet" in dominio:
        return "LOW"

    return "MEDIUM"


def analisar_urls():
    resultados = []

    with open(
        ARQUIVO_ENTRADA,
        "r",
        encoding="utf-8"
    ) as csvfile:

        leitor = csv.DictReader(csvfile)

        for linha in leitor:

            url = linha["url"]

            dominio = urlparse(url).netloc

            risco = classificar_url(dominio)

            resultados.append(
                {
                    "url": url,
                    "domain": dominio,
                    "risk": risco
                }
            )

    with open(
        ARQUIVO_SAIDA,
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        campos = ["url", "domain", "risk"]

        writer = csv.DictWriter(
            csvfile,
            fieldnames=campos
        )

        writer.writeheader()
        writer.writerows(resultados)

    print(
        f"Relatório gerado: {ARQUIVO_SAIDA}"
    )


if __name__ == "__main__":
    analisar_urls()