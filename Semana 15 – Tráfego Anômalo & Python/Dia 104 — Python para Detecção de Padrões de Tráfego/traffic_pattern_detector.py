from collections import Counter, defaultdict

ips = []
ports_by_ip = defaultdict(set)

with open("network.log", "r") as file:
    for line in file:
        parts = line.split()

        # 🔒 Garantir que a linha tem todos os campos
        if len(parts) < 6:
            continue

        src_ip = parts[2]
        dest_port = parts[4]

        ips.append(src_ip)
        ports_by_ip[src_ip].add(dest_port)

# ===============================
# Volume
# ===============================
contador = Counter(ips)

LIMITE_CONEXOES = 10
LIMITE_PORTAS = 5

print("=== Análise ===")

for ip in contador:
    total = contador[ip]
    portas = len(ports_by_ip[ip])

    print(f"{ip} -> {total} conexões | {portas} portas")

    if total > LIMITE_CONEXOES:
        print(f"[ALERTA - VOLUME] {ip}")

    if portas > LIMITE_PORTAS:
        print(f"[ALERTA - SCAN] {ip}")

