# log_parser.py
import re
import csv
from collections import Counter

# Patterns
ip_re = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d{1,2})\.){3}(?:25[0-5]|2[0-4]\d|1?\d{1,2})\b")
failed_re = re.compile(r"Failed\s+password\s+for\s+(?:invalid\s+user\s+)?(?P<user>\S+)\s+from\s+(?P<ip>(?:\d{1,3}\.){3}\d{1,3})", re.IGNORECASE)
ts_re = re.compile(r"\b\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\b")

ips = Counter()
users = Counter()
events = []

with open("auth_sample.log", "r", encoding="utf-8") as f:
    for line in f:
        m = failed_re.search(line)
        if m:
            user = m.group("user")
            ip = m.group("ip")
            ips[ip] += 1
            users[user] += 1
            ts = ts_re.search(line)
            time = ts.group(0) if ts else ""
            events.append({"time": time, "user": user, "ip": ip, "raw": line.strip()})

# Write CSV of events
with open("logins_falhos.csv", "w", newline="", encoding="utf-8") as csvf:
    writer = csv.DictWriter(csvf, fieldnames=["time","user","ip","raw"])
    writer.writeheader()
    writer.writerows(events)

# Summary
print("Top IPs:", ips.most_common(10))
print("Top Users:", users.most_common(10))

