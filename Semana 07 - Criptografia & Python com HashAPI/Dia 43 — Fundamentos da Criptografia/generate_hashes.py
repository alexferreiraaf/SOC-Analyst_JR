#!/usr/bin/env python3
# generate_hashes.py
import hashlib
import csv
from pathlib import Path

FILES = ["file1.txt", "file2.txt", "file3.txt"]
OUT_CSV = "hashes_original.csv"

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

rows = []
for fname in FILES:
    p = Path(fname)
    if p.exists():
        rows.append({
            "file": fname,
            "sha256": sha256_of(p),
            "md5": md5_of(p),
            "path": str(p.resolve())
        })
    else:
        print(f"[!] Arquivo não encontrado: {fname}")

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["file","sha256","md5","path"])
    writer.writeheader()
    writer.writerows(rows)

print(f"[+] Hashes iniciais salvos em: {OUT_CSV}")

