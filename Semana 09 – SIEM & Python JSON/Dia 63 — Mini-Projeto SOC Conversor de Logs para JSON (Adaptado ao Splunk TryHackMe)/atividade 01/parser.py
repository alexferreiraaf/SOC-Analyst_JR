if __name__ == "__main__":
    logs_parseados = processar_logs("auth.log")
    salvar_json("logs_convertidos.json", logs_parseados)

    print(f"✔ {len(logs_parseados)} eventos extraídos")

