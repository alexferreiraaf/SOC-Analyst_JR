"""
enrich_ip_ipinfo.py
- Recebe um dicionário {ip: count} (por exemplo do seu parser)
- Consulta ipinfo.io para cada IP
- Salva enrichments em enriched_ips_ipinfo.csv
"""

import os
import time
import requests
import csv

# Exemplo de ips (substitua pelo seu Counter/Dict real)
ips = {
    "185.222.123.45": 10,
    "203.0.113.55": 3,
    "192.168.0.10": 1
}

# Se você tiver token do ipinfo (opcional)
IPINFO_TOKEN = os.getenv("IPINFO_TOKEN", "").strip()  # deixe vazio se não tiver

BASE_URL = "https://ipinfo.io"

def get_ipinfo(ip):
    """Consulta ipinfo.io e retorna dict com campos úteis."""
    headers = {}
    params = {}
    if IPINFO_TOKEN:
        # Com token: https://ipinfo.io/developers
        params["token"] = IPINFO_TOKEN
    url = f"{BASE_URL}/{ip}/json"
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        # campos de interesse: ip, hostname, city, region, country, org, loc, postal
        return {
            "ip": ip,
            "hostname": data.get("hostname", ""),
            "city": data.get("city", ""),
            "region": data.get("region", ""),
            "country": data.get("country", ""),
            "org": data.get("org", ""),
            "loc": data.get("loc", ""),  # lat,long
            "postal": data.get("postal", ""),
            "raw": data
        }
    except requests.HTTPError as e:
        return {"ip": ip, "error": f"HTTP {e.response.status_code}"}
    except Exception as e:
        return {"ip": ip, "error": str(e)}

def main():
    out_file = "enriched_ips_ipinfo.csv"
    with open(out_file, "w", newline="", encoding="utf-8") as csvf:
        writer = csv.writer(csvf)
        writer.writerow(["ip", "count", "hostname", "city", "region", "country", "org", "loc", "postal", "error"])

        for ip, count in ips.items():
            # Ignorar IPs privados se quiser
            if ip.startswith(("10.", "172.", "192.168.")):
                # opcional: ainda registrar com flag "private"
                writer.writerow([ip, count, "", "", "", "", "", "", "", "private-network"])
                continue

            info = get_ipinfo(ip)
            # respeitar rate-limits simples
            time.sleep(0.6)  # ajuste conforme limite (ex.: 1 req/s)
            writer.writerow([
                info.get("ip"),
                count,
                info.get("hostname", ""),
                info.get("city", ""),
                info.get("region", ""),
                info.get("country", ""),
                info.get("org", ""),
                info.get("loc", ""),
                info.get("postal", ""),
                info.get("error", "")
            ])

    print(f"Enriquecimento concluído. Salvo: {out_file}")

if __name__ == "__main__":
    main()
