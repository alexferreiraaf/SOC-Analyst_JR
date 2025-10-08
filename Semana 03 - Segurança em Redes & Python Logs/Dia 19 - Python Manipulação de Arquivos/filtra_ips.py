# filtra_ips.py
def filtrar_ips(entrada="ips.txt", saida="ips_saida.txt", prefixo="192.168."):
    encontrados = []
    with open(entrada, "r", encoding="utf-8") as fin, \
         open(saida, "w", encoding="utf-8") as fout:
        for linha in fin:
            ip = linha.strip()
            if ip.startswith(prefixo):
                fout.write(ip + "\n")
                encontrados.append(ip)
    return encontrados

if __name__ == "__main__":
    encontrados = filtrar_ips()
    print(f"IPs escritos em ips_saida.txt: {len(encontrados)}")
    for ip in encontrados:
        print(" -", ip)

