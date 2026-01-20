import pandas as pd
import re

log_file = "access.log"

pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ '
    r'\[(?P<date>.*?)\] '
    r'"(?P<method>\S+) (?P<url>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)

records = []

with open(log_file) as f:
    for line in f:
        match = pattern.search(line)
        if match:
            records.append(match.groupdict())

logs = pd.DataFrame(records)

# Converter tipos
logs["status"] = logs["status"].astype(int)
logs["size"] = logs["size"].astype(int)

# Converter timestamp corretamente (com timezone)
logs["date"] = pd.to_datetime(
    logs["date"],
    format="%d/%b/%Y:%H:%M:%S %z"
)

print("\n📄 Primeiros eventos:")
print(logs.head())

# =========================
# Análises SOC
# =========================

print("\n🔹 Top IPs:")
print(logs["ip"].value_counts().head(10))

print("\n🚨 Possíveis brute force (401 / 403):")
failed = logs[logs["status"].isin([401, 403])]
print(failed["ip"].value_counts().head(10))

print("\n⏱️ Requisições por hora:")
logs["hour"] = logs["date"].dt.hour
print(logs.groupby("hour").size())

