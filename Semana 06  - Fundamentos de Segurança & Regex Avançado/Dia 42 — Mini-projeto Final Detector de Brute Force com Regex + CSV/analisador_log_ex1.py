import re, csv, collections

# Novo padrão: captura Data/Hora, Usuário e IP
pattern = re.compile(
    r"^(\w{3}\s+\d+\s[\d:]+).*Failed password for (\w+) from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"
)

# Contador de tentativas por IP
ips = collections.Counter()

# Abrir o log e capturar os dados
registros = []
with open("auth_sample.log") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            datetime_str, user, ip = match.groups()
            registros.append([datetime_str, user, ip])
            ips[ip] += 1

# Gerar novo CSV com Data/Hora, Usuário, IP
with open("relatorio_bruteforce_com_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Data/Hora", "Usuário", "IP"])
    writer.writerows(registros)

print("✅ Relatório salvo como relatorio_bruteforce_com_data.csv")

# Mostrar alertas se houver IPs suspeitos (>5 tentativas)
for ip, count in ips.items():
    if count > 5:
        print(f"⚠️ ALERTA: IP {ip} com {count} tentativas de login!")
