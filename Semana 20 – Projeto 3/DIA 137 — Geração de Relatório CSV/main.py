import csv
import requests 
from api_key import API_KEY 
from utils import ( 
        extrair_ips, 
        validar_ip, 
        consultar_virustotal, 
        classificar_risco, 
        ) 
    ARQUIVO_LOG = "logs_exemplo.log" 
    ARQUIVO_SAIDA = "relatorio_final.csv" 

    def gerar_csv(resultado): 
        with open( 
                ARQUIVO_SAIDA, 
                mode="w", 
                newline="", 
                encoding="utf-8", 
             ) as arquivo: 

                writer = csv.writer(arquivo) 
                writer.writerow( 
                        [ 
                            "IP", 
                            "Detections", 
                            "Risk", 
                        ] 
                     ) 

                    for item in resultado: 
                        writer.writerow( 
                                [ 
                                    item["ip"], 
                                    item["detections"], 
                                    item["risk"], 
                                 ] 
                             ) 
    def main(): 
        print("=" * 50) 
        print("LOG THREAT INTELLIGENCE ANALYZER") 
        print("=" * 50) 

        ips = extrair_ips(ARQUIVO_LOG) 

        print(f"\nIPs encontrados: {len(ips)}") 

        resultados = [] 

        for ip in ips: 
            if not validar_ip(ip): 
                print(f"IP inválido ignorado: {ip}") 
                continue 
            print(f"\nConsultando {ip}...") 
            malicious, suspicious = consultar_virustotal( 
                    ip, 
                    API_KEY, 
            ) 

            detections = malicious + suspicious 
            risk = classificar_risco(detections) resultados.append( 
                    { 
                        "ip": ip, 
                        "detections": detections, 
                        "risk": risk, 
                     } 
             ) 

            print( 
                    f"Detecções: {detections} | Classificação: {risk}" 
             ) 
            gerar_csv(resultados) 

            print("\nRelatório CSV gerado com sucesso!") 
            print(f"Arquivo: {ARQUIVO_SAIDA}") 

            if __name__ == "__main__": 
                main()
