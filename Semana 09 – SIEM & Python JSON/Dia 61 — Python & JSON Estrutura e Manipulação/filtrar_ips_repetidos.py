def ips_duplicados(eventos):
    contagem = {}

    for item in eventos:
        ip = (
            item.get("ip") or
            item.get("src_ip") or
            item.get("source_ip")
        )

        if not ip:
            continue

        contagem[ip] = contagem.get(ip, 0) + 1

    return contagem

