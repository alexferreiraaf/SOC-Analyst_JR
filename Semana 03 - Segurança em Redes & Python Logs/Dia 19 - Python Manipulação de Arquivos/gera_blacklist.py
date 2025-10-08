# gera_blacklist.py
from datetime import datetime

def gerar_csv(ips_file="ips_saida.txt", out="blacklist.csv"):
    hoje = datetime.utcnow().isoformat()
    with open(ips_file, "r", encoding="utf-8") as fin, \
         open(out, "w", encoding="utf-8") as fout:
        fout.write("ip,comentario,data\n")
        for linha in fin:
            ip = linha.strip()
            if not ip:
                continue
            fout.write(f"{ip},detected_by_lab,{hoje}\n")

if __name__ == "__main__":
    gerar_csv()
    print("blacklist.csv gerado.")

