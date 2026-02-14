from collections import Counter, defaultdict

LIMITE_CONEXOES = 15
LIMITE_PORTAS = 6

ips = []
ports_by_ip = defaultdict(set)

# Leitura segura do log
with open("network.log", "r") as file:
    for line in file:
        parts = line.split()

        # Proteção contra linhas inválidas
        if len(parts) < 6:
            continue

        src_ip = parts[2]
        dest_port = parts[4]

        ips.append(src_ip)
        ports_by_ip[src_ip].add(dest_port)

contador_ips = Counter(ips)

alertas = []

# Verificar volume de conexões
for ip, total in contador_ips.items():
    if total > LIMITE_CONEXOES:
        alertas.append(
            f"[ALERTA] IP {ip} realizou {total} conexões (possível DoS)"
        )

# Verificar múltiplas portas
for ip, ports in ports_by_ip.items():
    if len(ports) > LIMITE_PORTAS:
        alertas.append(
            f"[SCAN] IP {ip} acessou {len(ports)} portas diferentes"
        )

# Gerar relatório
with open("relatorio_conexoes_suspeitas.txt", "w") as report:
    report.write("RELATÓRIO SOC — CONEXÕES SUSPEITAS\n")
    report.write("=" * 40 + "\n\n")

    if alertas:
        for alerta in alertas:
            report.write(alerta + "\n")
    else:
        report.write("Nenhuma atividade suspeita detectada.\n")

print("Relatório gerado com sucesso.")

