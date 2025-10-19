# 📄 relatorio_lab32.ps1
# Script para gerar relatório de comandos administrativos no Windows

# Caminho do arquivo de saída
$arquivo = "C:\Users\Public\relatorio_lab32.md"

# Limpa o arquivo anterior, se existir
if (Test-Path $arquivo) {
    Remove-Item $arquivo
}

# 1️⃣ Listar 5 processos com maior uso de memória
Add-Content $arquivo "===== 1. Top 5 Processos por Uso de Memória ====="
Get-Process | Sort-Object WS -Descending | Select-Object -First 5 Name, WS |
    Out-String | Add-Content $arquivo
Add-Content $arquivo "`n"

# 2️⃣ Mostrar serviços com nome que contenha 'net'
Add-Content $arquivo "===== 2. Serviços que Contêm 'net' ====="
Get-Service | Where-Object { $_.Name -match "net" } |
    Out-String | Add-Content $arquivo
Add-Content $arquivo "`n"

# 3️⃣ Exibir o status do firewall
Add-Content $arquivo "===== 3. Status do Firewall ====="
Get-NetFirewallProfile |
    Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction |
    Out-String | Add-Content $arquivo
Add-Content $arquivo "`n"

# 4️⃣ Mostrar adaptadores de rede ativos
Add-Content $arquivo "===== 4. Adaptadores de Rede Ativos ====="
Get-NetAdapter | Where-Object { $_.Status -eq "Up" } |
    Select-Object Name, Status, MacAddress, LinkSpeed |
    Out-String | Add-Content $arquivo
Add-Content $arquivo "`n"

# 5️⃣ Mostrar endereços IP
Add-Content $arquivo "===== 5. Endereços IP ====="
Get-NetIPAddress |
    Select-Object InterfaceAlias, IPAddress |
    Out-String | Add-Content $arquivo
Add-Content $arquivo "`n"

# Finalização
Add-Content $arquivo "===== Relatório gerado em $(Get-Date) ====="

Write-Host "✅ Relatório criado com sucesso em: $arquivo"
