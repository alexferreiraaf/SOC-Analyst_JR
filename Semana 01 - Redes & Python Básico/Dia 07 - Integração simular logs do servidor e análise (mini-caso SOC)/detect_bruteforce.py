# detect_bruteforce.py
from collections import Counter, defaultdict
import re

# Regex para capturar IP e timestamp
ip_re = re.compile(r"SRC=(\d{1,3}(?:\.\d{1,3}){3})")
time_re = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")

limite = 3  # Exemplo: mais de 3 falhas = suspeito

counts = Counter()
lines_by_ip = defaultdict(list)

with open("ssh_auth.log", "r", encoding="utf-8") as f:
    for line in f:
        ipm = ip_re.search(line)
        if ipm:
            ip = ipm.group(1)
            counts[ip] += 1
            lines_by_ip[ip].append(line.strip())

suspects = [ip for ip, c in counts.items() if c >= limite]

print("Resumo de contagens por IP:")
for ip, c in counts.most_common():
    print(ip, c)

if suspects:
    print("\nIPs suspeitos (mais de {} tentativas):".format(limite))
    for s in suspects:
        print("\n===>", s)
        for l in lines_by_ip[s]:
            print("   ", l)
else:
    print("\nNenhum IP acima do limite.")
