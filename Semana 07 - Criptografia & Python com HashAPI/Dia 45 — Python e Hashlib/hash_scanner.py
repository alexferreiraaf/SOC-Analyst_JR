#!/usr/bin/env python3
"""
hash_scanner.py
- Lista arquivos em um diretório
- Calcula SHA256 para cada arquivo
- Salva resultados em hashes_diretorio.csv
- Mostra os 5 primeiros caracteres do hash (fingerprint) no console

Usage:
    python3 hash_scanner.py --dir PATH_TO_DIR [--recursive] [--out FILE]
"""
import hashlib
import csv
from pathlib import Path
from datetime import datetime
import argparse
import sys

BUFFER_SIZE = 65536  # 64KB


def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(BUFFER_SIZE), b""):
            h.update(chunk)
    return h.hexdigest()


def scan_directory(dir_path: Path, recursive: bool = False):
    if recursive:
        files = [p for p in dir_path.rglob("*") if p.is_file()]
    else:
        files = [p for p in dir_path.iterdir() if p.is_file()]
    return sorted(files)


def main():
    parser = argparse.ArgumentParser(description="Scaneia um diretório e gera SHA256 para cada arquivo")
    parser.add_argument("--dir", "-d", default=".", help="Diretório a ser escaneado (padrão: .)")
    parser.add_argument("--recursive", "-r", action="store_true", help="Varre recursivamente subpastas")
    parser.add_argument("--out", "-o", default="hashes_diretorio.csv", help="Arquivo CSV de saída")
    args = parser.parse_args()

    dir_path = Path(args.dir).expanduser().resolve()
    if not dir_path.exists() or not dir_path.is_dir():
        print(f"❌ Diretório inválido: {dir_path}", file=sys.stderr)
        sys.exit(1)

    files = scan_directory(dir_path, recursive=args.recursive)
    if not files:
        print("⚠️ Nenhum arquivo encontrado no diretório.")
        return

    out_file = Path(args.out)

    with out_file.open("w", newline="", encoding="utf-8") as csvf:
        writer = csv.writer(csvf)
        writer.writerow(["arquivo", "sha256", "tamanho_bytes", "modificado_iso"])

        for p in files:
            try:
                sha = sha256_of_file(p)
                size = p.stat().st_size
                mtime = datetime.fromtimestamp(p.stat().st_mtime).isoformat(sep=" ")
                # write to CSV
                writer.writerow([str(p.relative_to(dir_path)), sha, size, mtime])
                # print fingerprint (first 5 chars)
                print(f"{p.relative_to(dir_path)}  |  {sha[:5]}  |  {size} bytes")
            except PermissionError:
                print(f"⚠️ Permissão negada: {p}", file=sys.stderr)
            except Exception as e:
                print(f"⚠️ Erro processando {p}: {e}", file=sys.stderr)

    print(f"\n✅ Scan concluído. Resultados salvos em: {out_file.resolve()}")
    print(f"Total de arquivos processados: {len(files)}")


if __name__ == "__main__":
    main()

