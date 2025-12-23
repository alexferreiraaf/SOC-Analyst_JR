defler_logs(caminho):
withopen(caminho, encoding="utf-8")as f:
for linhain f:
yield linha.strip()

