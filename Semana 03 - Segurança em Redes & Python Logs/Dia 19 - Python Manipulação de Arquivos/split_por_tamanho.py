# split_por_tamanho.py
def split_file(input_file, max_lines=10000, prefix="part_"):
    part = 0
    line_count = 0
    out = None
    with open(input_file, "r", encoding="utf-8") as fin:
        for line in fin:
            if line_count % max_lines == 0:
                if out:
                    out.close()
                part += 1
                out = open(f"{prefix}{part}.txt", "w", encoding="utf-8")
            out.write(line)
            line_count += 1
    if out:
        out.close()
    print(f"Arquivo dividido em {part} partes.")

if __name__ == "__main__":
    split_file("big_log.txt", max_lines=5000)

