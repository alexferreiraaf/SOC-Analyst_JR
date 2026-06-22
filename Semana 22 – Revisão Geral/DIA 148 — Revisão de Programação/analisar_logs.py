import re

ips = {}
arquivo = open("log.txt")

for linha in arquivo:
    encontrados = re.findall(r'\d+\.\d+\.\d+\.\d+', linha)

    for ip in encontrados:
        ips[ip] = ips.get(ip, 0) + 1

arquivo.close()

print("IPs encontrados:\n")

for ip, quantidade in ips.items():
    print(f"{ip} -> {quantidade} ocorrência(s)")

print("\nIPs com mais de uma ocorrência:\n")

for ip, quantidade in ips.items():
    if quantidade > 1:
        print(f"{ip} -> {quantidade}")