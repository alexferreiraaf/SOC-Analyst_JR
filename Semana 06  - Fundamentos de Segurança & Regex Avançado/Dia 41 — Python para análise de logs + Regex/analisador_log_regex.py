#!/usr/bin/env python3
"""
analisador_log_regex.py
- Extrai eventos "Failed password" de auth_sample.log
- Gera logins_falhos.csv com todos os eventos parseados
- Gera logins_suspeitos.csv com IPs que ultrapassam threshold
Usage:
    python analisador_log_regex.py --input auth_sample.log
"""

import re, csv, argparse
from collections import Counter, defaultdict
from datetime import datetime, timedelta

# -------- CONFIG --------
DEFAULT_INPUT = "auth_sample.log"
OUTPUT_EVENTS_CSV = "logins_falhos.csv"
OUTPUT_SUSPECTS_CSV = "logins_suspeitos.csv"

# thresholds
GLOBAL_THRESHOLD = 2           # Ip com > GLOBAL_THRESHOLD tentativas é suspeito
WINDOW_THRESHOLD = 3            # Tentativas dentro de WINDOW_MINUTES que tornam um IP suspeito
WINDOW_MINUTES = 2

# Regex patterns (ajuste conforme formato de log)
# Timestamp pattern (ISO-like: 2025-10-20 08:15:23) - adapt if your logs differ
ts_re = re.compile(r"(?P<ts>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})")

# Failed password pattern (covers "invalid user" and normal user)
failed_re = re.compile(
    r"Failed\s+password\s+for\s+(?:invalid\s+user\s+)?(?P<user>\S+)\s+from\s+(?P<ip>(?:\d{1,3}\.){3}\d{1,3})",
    re.IGNORECASE
)

def parse_line(line):
    """Tenta extrair timestamp, user, ip de uma linha de log. Retorna dict ou None."""
    m = failed_re.search(line)
    if not m:
        return None
    user = m.group("user")
    ip = m.group("ip")
    ts_m = ts_re.search(line)
    ts = ts_m.group("ts") if ts_m else ""
    # parse timestamp to datetime if possible
    dt = None
    if ts:
        try:
            dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
        except Exception:
            dt = None
    return {"time_str": ts, "time_dt": dt, "user": user, "ip": ip, "raw": line.strip()}

def main(input_file):
    events = []
    ip_counter = Counter()
    # per-ip list of datetimes for sliding window detection
    times_by_ip = defaultdict(list)

    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            p = parse_line(line)
            if p:
                events.append(p)
                ip_counter[p["ip"]] += 1
                if p["time_dt"]:
                    times_by_ip[p["ip"]].append(p["time_dt"])

    # write all parsed events
    with open(OUTPUT_EVENTS_CSV, "w", newline="", encoding="utf-8") as csvf:
        writer = csv.DictWriter(csvf, fieldnames=["time", "user", "ip", "raw"])
        writer.writeheader()
        for e in events:
            writer.writerow({"time": e["time_str"], "user": e["user"], "ip": e["ip"], "raw": e["raw"]})
    print(f"[+] {len(events)} eventos parseados. Salvo em: {OUTPUT_EVENTS_CSV}")

    # detect suspects by total count
    suspects = []
    for ip, cnt in ip_counter.most_common():
        first = ""
        last = ""
        times = sorted(times_by_ip.get(ip, []))
        if times:
            first = times[0].strftime("%Y-%m-%d %H:%M:%S")
            last = times[-1].strftime("%Y-%m-%d %H:%M:%S")
        suspect_reasons = []
        if cnt > GLOBAL_THRESHOLD:
            suspect_reasons.append(f"total>{GLOBAL_THRESHOLD}")
        # sliding window detection
        window_flag = False
        if times:
            # two-pointer technique
            i = 0
            for j in range(len(times)):
                while times[j] - times[i] > timedelta(minutes=WINDOW_MINUTES):
                    i += 1
                if (j - i + 1) >= WINDOW_THRESHOLD:
                    window_flag = True
                    break
        if window_flag:
            suspect_reasons.append(f"{WINDOW_THRESHOLD} in {WINDOW_MINUTES}min")
        if suspect_reasons:
            suspects.append({"ip": ip, "count": cnt, "first": first, "last": last, "reasons": ";".join(suspect_reasons)})

    # write suspects CSV
    with open(OUTPUT_SUSPECTS_CSV, "w", newline="", encoding="utf-8") as csvf:
        writer = csv.DictWriter(csvf, fieldnames=["ip", "count", "first", "last", "reasons"])
        writer.writeheader()
        for s in suspects:
            writer.writerow(s)

    print(f"[+] {len(suspects)} IPs suspeitos detectados. Salvo em: {OUTPUT_SUSPECTS_CSV}")

    # quick console summary
    print("\nTop 10 IPs por tentativas:")
    for ip, cnt in ip_counter.most_common(10):
        print(f"  {ip} -> {cnt}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analisa auth_sample.log e detecta logins falhos")
    parser.add_argument("--input", "-i", default=DEFAULT_INPUT, help="Arquivo de log de entrada")
    args = parser.parse_args()
    main(args.input)

