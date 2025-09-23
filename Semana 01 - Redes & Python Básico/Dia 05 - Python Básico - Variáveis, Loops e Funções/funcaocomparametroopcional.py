def alerta(ip, porta=80):
    print(f"Alerta: tráfego suspeito do IP {ip} na porta {porta}")

alerta("192.168.1.10")
alerta("10.0.0.5", 22)
