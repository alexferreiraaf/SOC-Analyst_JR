import re

log = open("auth.log").read()

ips = re.findall(r"\b\d{1,3}(\.\d{1,3}){3}\b", log)

print(set(ips))