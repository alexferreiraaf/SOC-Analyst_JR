# soc_checker.py

def check_port(ip, porta):
    """Função que simula a checagem de uma porta em um IP"""
    print(f"Checando porta {porta} no IP {ip}...")


def main():
    # Criando lista para armazenar os IPs
    ips = []

    # Solicitando 3 IPs ao usuário
    for i in range(3):
        ip = input(f"Digite o IP {i+1}: ")
        ips.append(ip)

    # Percorrendo os IPs e verificando conexão
    for ip in ips:
        print(f"\nVerificando conexão com IP {ip}...")
        check_port(ip, 22)  # Porta 22 (SSH)


if __name__ == "__main__":
    main()
