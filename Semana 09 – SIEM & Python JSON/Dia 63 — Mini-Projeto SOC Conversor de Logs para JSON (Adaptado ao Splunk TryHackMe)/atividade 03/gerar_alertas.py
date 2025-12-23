import json
from collections import Counter, defaultdict

# 1. Carregar logs normalizados
with open("logs_splunk_prontos.json", encoding="utf-8") as f:
    eventos = json.load(f)

alertas = []

# 2. Regra 1 — IP com muitas falhas
falhas_por_ip = Counter(
    e["src_ip"] for e in eventos if e["status"] == "failed"
)

for ip, total in falhas_por_ip.items():
    if total > 5:
        alertas.append({
            "tipo_alerta": "brute_force_ip",
            "src_ip": ip,
            "total_falhas": total,
            "criticidade": "alta"
        })

# 3. Regra 2 — Usuário muito atacado
falhas_por_usuario = Counter(
    e["user"] for e in eventos if e["status"] == "failed"
)

for user, total in falhas_por_usuario.items():
    if user and total >= 10:
        alertas.append({
            "tipo_alerta": "usuario_muito_atacado",
            "user": user,
            "total_falhas": total,
            "criticidade": "media"
        })

# 4. Regra 3 — IP tentando vários usuários
ips_usuarios = defaultdict(set)

for e in eventos:
    if e["status"] == "failed" and e["user"]:
        ips_usuarios[e["src_ip"]].add(e["user"])

for ip, usuarios in ips_usuarios.items():
    if len(usuarios) >= 3:
        alertas.append({
            "tipo_alerta": "spray_attack",
            "src_ip": ip,
            "usuarios_alvo": list(usuarios),
            "criticidade": "alta"
        })

# 5. Salvar alertas externos
with open("alertas.json", "w", encoding="utf-8") as f:
    json.dump(alertas, f, indent=4, ensure_ascii=False)

print(f"🚨 {len(alertas)} alertas gerados com sucesso")

