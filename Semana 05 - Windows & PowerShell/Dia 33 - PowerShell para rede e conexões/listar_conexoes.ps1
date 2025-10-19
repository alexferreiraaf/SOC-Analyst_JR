# listar_conexoes.ps1
# Lista conexões HTTPS (porta 443) e identifica IPs conhecidos

Write-Host "Listando conexões na porta 443 (HTTPS)..."

# 1. Listar todas as conexões usando a porta 443
Get-NetTCPConnection | Where-Object { $_.RemotePort -eq 443 } | `
Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State | `
Out-File listar_conexoes.md

# 2. Adicionar identificação de IPs conhecidos (Google, Microsoft, etc.)
Add-Content listar_conexoes.md "`n---"
Add-Content listar_conexoes.md "Verificação de IPs conhecidos:`n"

# Lista de IPs conhecidos (pode ser expandida)
$ips_legitimos = @(
    "8.8.8.8",     # Google DNS
    "8.8.4.4",     # Google DNS
    "20.42.73.1",  # Microsoft Azure (exemplo)
    "13.107.42.12" # Microsoft
)

# Obter apenas IPs únicos da lista de conexões
$conexoes = Get-NetTCPConnection | Where-Object { $_.RemotePort -eq 443 } | Select-Object -ExpandProperty RemoteAddress -Unique

foreach ($ip in $conexoes) {
    if ($ips_legitimos -contains $ip) {
        Add-Content listar_conexoes.md "$ip - IP legítimo (Google/Microsoft)"
    } else {
        Add-Content listar_conexoes.md "$ip - IP desconhecido ou não listado"
    }
}

Write-Host "Relatório salvo em listar_conexoes.md"
