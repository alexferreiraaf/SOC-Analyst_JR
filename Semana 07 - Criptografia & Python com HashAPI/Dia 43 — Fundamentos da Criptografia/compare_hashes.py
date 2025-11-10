#!/usr/bin/env python3
# compare_hashes.py
import hashlib, csv
from pathlib import Path

ORIGINAL = "hashes_original.csv"
AFTER = "hashes_after.csv"
COMPARISON = "comparison_result.csv"

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def md5_of(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

# read original
orig = {}
with open(ORIGINAL, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    for row in r:
        orig[row["file"]] = row

# generate after hashes for same files listed in ORIGINAL
rows_after = []
for fname in orig.keys():
    p = Path(fname)
    if p.exists():
        rows_after.append({
            "file": fname,
            "sha256": sha256_of(p),
            "md5": md5_of(p),
            "path": str(p.resolve())
        })
    else:
        rows_after.append({
            "file": fname,
            "sha256": "",
            "md5": "",
            "path": ""
        })

# write after CSV
with open(AFTER, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["file","sha256","md5","path"])
    writer.writeheader()
    writer.writerows(rows_after)

# compare and produce result
comp_rows = []
for a in rows_after:
    name = a["file"]
    o = orig.get(name, {})
    sha_changed = (o.get("sha256","") != a.get("sha256",""))
    md5_changed = (o.get("md5","") != a.get("md5",""))
    changed = sha_changed or md5_changed
    comp_rows.append({
        "file": name,
        "sha256_original": o.get("sha256",""),
        "sha256_after": a.get("sha256",""),
        "md5_original": o.get("md5",""),
        "md5_after": a.get("md5",""),
        "path": a.get("path",""),
        "changed": "YES" if changed else "NO",
        "why": ("sha256" if sha_changed else ("md5" if md5_changed else "same"))
    })

with open(COMPARISON, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "file","sha256_original","sha256_after","md5_original","md5_after","path","changed","why"
    ])
    writer.writeheader()
    writer.writerows(comp_rows)

# console summary
print("[+] Comparação gerada em:", COMPARISON)
for r in comp_rows:
    status = "ALTERADO" if r["changed"] == "YES" else "OK"
    print(f" - {r['file']}: {status} (motivo: {r['why']})")

