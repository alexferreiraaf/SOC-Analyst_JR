from collectionsimport Counter

ips = [e["ip"]for ein eventos]
usuarios = [e["usuario"]for ein eventos]

alertas = {
"ips_suspeitos": [ipfor ip, cin Counter(ips).items()if c >5],
"usuarios_mais_atacados": Counter(usuarios).most_common(3)
}


