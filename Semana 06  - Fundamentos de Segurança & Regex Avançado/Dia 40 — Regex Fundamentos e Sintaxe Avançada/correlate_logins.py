#!/usr/bin/env python3
# correlate_logins.py
# Compatível com Python 3.6+
# Objetivo: detectar quando um usuário falha no login e tem sucesso em até 5 minutos (mesmo user+ip)

import re
import pandas as pd
from datetime import datetime, timedelta

LOGFILE = "auth_sample.log"
OUTPUT_CSV = "correlacao_falha_sucesso.csv"
ASSUME_YEAR = 2025  # ajuste se necessário

# --- Patterns ---
# Exemplos de linhas esperadas:
# Oct  8 12:11:22 server sshd[1288]: Failed password for root from 192.168.0.45 port 55522 ssh2
# Oct  8 12:11:35 server sshd[1288]: Accepted password for user1 from 10.0.0.25 port 55801 ssh2
# Também suporta: "Failed password for invalid user admin from 203.0.113.10 ..."
fail_pattern = re.compile(
    r'^(?P<ts>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}).*Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
)
success_pattern = re.compile(
    r'^(?P<ts>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}).*Accepted password for (?P<user>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
)

# --- Ler arquivo e extrair eventos ---
events = []
with open(LOGFILE, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        line = line.rstrip("\n")
        m = fail_pattern.search(line)
        if m:
            events.append({
                "raw_ts": m.group("ts"),
                "user": m.group("user"),
                "ip": m.group("ip"),
                "status": "fail",
                "line": line
            })
            continue
        m2 = success_pattern.search(line)
        if m2:
            events.append({
                "raw_ts": m2.group("ts"),
                "user": m2.group("user"),
                "ip": m2.group("ip"),
                "status": "success",
                "line": line
            })

if not events:
    print("Nenhum evento fail/success encontrado em", LOGFILE)
    raise SystemExit(0)

# --- Converter para DataFrame e timestamps ---
df = pd.DataFrame(events)

# Tenta converter 'raw_ts' (ex: "Oct  8 12:11:22") para datetime com ano ASSUME_YEAR
def parse_ts(s):
    # Pad day if single digit (some syslogs use single space)
    try:
        dt = datetime.strptime(f"{s} {ASSUME_YEAR}", "%b %d %H:%M:%S %Y")
    except ValueError:
        # tentar ajustar espaços
        s2 = re.sub(r'\s+', ' ', s).strip()
        dt = datetime.strptime(f"{s2} {ASSUME_YEAR}", "%b %d %H:%M:%S %Y")
    return dt

df["timestamp"] = df["raw_ts"].apply(parse_ts)

# Ordenar por time para garantir sequência
df = df.sort_values("timestamp").reset_index(drop=True)

# --- Correlacionar: para cada 'fail' procurar 'success' do mesmo user+ip em até 5 min depois ---
suspects = []
grouped = df.groupby(["user", "ip"])
for (user, ip), group in grouped:
    # group already sorted by timestamp globally, but re-sort per group
    g = group.sort_values("timestamp").reset_index(drop=True)
    for i, row in g.iterrows():
        if row["status"] != "fail":
            continue
        fail_time = row["timestamp"]
        # procurar a primeira success que ocorra após o fail_time e dentro de 5 minutos
        window_end = fail_time + timedelta(minutes=5)
        later_successes = g[(g["status"] == "success") & (g["timestamp"] > fail_time) & (g["timestamp"] <= window_end)]
        if not later_successes.empty:
            first_success = later_successes.iloc[0]
            suspects.append({
                "user": user,
                "ip": ip,
                "fail_time": fail_time,
                "success_time": first_success["timestamp"],
                "fail_line": row.get("line", ""),
                "success_line": first_success.get("line", "")
            })

# --- Resultado ---
if not suspects:
    print("Nenhum caso de fail -> success em até 5 minutos encontrado.")
else:
    suspects_df = pd.DataFrame(suspects)
    # formatar datetime em string para CSV
    suspects_df["fail_time"] = suspects_df["fail_time"].dt.strftime("%Y-%m-%d %H:%M:%S")
    suspects_df["success_time"] = suspects_df["success_time"].dt.strftime("%Y-%m-%d %H:%M:%S")
    suspects_df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print("Casos detectados salvos em:", OUTPUT_CSV)
    print(suspects_df[["user", "ip", "fail_time", "success_time"]].to_string(index=False))
