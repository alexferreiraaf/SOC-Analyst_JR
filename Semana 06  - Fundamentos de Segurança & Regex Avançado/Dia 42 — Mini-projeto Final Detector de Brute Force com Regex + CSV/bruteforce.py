import re, csv, collections

pattern = re.compile(r"Failed password for (\w+) from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)")
ips = collections.Counter()

with open("auth_sample.log") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            user, ip = match.groups()
            ips[ip] += 1

with open("relatorio_bruteforce.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["IP", "Tentativas"])
    for ip, count in ips.most_common():
        writer.writerow([ip, count])

print("Relatório salvo em relatorio_bruteforce.csv")

# Alerta se IP suspeito
for ip, count in ips.items():
    if count > 5:
        print(f"⚠️ ALERTA: IP {ip} com {count} tentativas de login!")

