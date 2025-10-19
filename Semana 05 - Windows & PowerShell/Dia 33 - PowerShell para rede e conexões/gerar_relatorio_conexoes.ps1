# gerar_relatorio_conexoes.ps1
# Gera relatório completo de conexões e processos em formato Markdown

$saida = "relatorio_conexoes_final.md"

# Cabeçalho do relatório
@"
# 🧠 Relatório Final de Conexões de Rede

Gerado em: $(Get-Date -Format 'dd/MM/yyyy HH:mm:ss')

---
"@ | Out-File -FilePath $saida -Encoding utf8

# Coletar todas as conexões
$conexoes = Get-NetTCPConnection

# 1️⃣ Número total de conexões
$totalConexoes = $conexoes.Count

# 2️⃣ Quantas estão ativas (Established)
$conexoesAtivas = $conexoes | Where-Object {$_.State -eq "Established"}
$qtdAtivas = $conexoesAtivas.Count

# 3️⃣ Portas mais usadas
$portasMaisUsadas = $conexoes | Group-Object -Property LocalPort | Sort-Object Count -Descending | Select-Object -First 10

# 4️⃣ Processos com conexões externas
$conexoesExternas = $conexoes | Where-Object {
    $_.RemoteAddress -and $_.RemoteAddress -notmatch "^(127\.0\.0\.1|::1|0\.0\.0\.0)$"
}

$processosExternos = @()
foreach ($c in $conexoesExternas) {
    try {
        $proc = Get-Process -Id $c.OwningProcess -ErrorAction Stop
        $processosExternos += [PSCustomObject]@{
            Processo = $proc.ProcessName
            PID = $proc.Id
            Caminho = $proc.Path
            IP_Remoto = $c.RemoteAddress
            Porta_Remota = $c.RemotePort
            Estado = $c.State
        }
    } catch {
        $processosExternos += [PSCustomObject]@{
            Processo = "Desconhecido"
            PID = $c.OwningProcess
            Caminho = "N/A"
            IP_Remoto = $c.RemoteAddress
            Porta_Remota = $c.RemotePort
            Estado = $c.State
        }
    }
}

# 5️⃣ IPs desconhecidos (não pertencem a domínios comuns)
$ipsDesconhecidos = $processosExternos | Where-Object {
    $_.IP_Remoto -notmatch "^(8\.8\.8\.8|1\.1\.1\.1|13\.|20\.|40\.|52\.|104\.|172\.217\.|142\.250\.)"
}

# Escreve tudo no arquivo Markdown
@"
## 🔹 1. Número total de conexões
**$totalConexoes**

## 🔹 2. Conexões ativas (Established)
**$qtdAtivas**

## 🔹 3. Portas mais usadas
"@ | Add-Content -Path $saida

$portasMaisUsadas | ForEach-Object {
    Add-Content -Path $saida -Value "- Porta **$($_.Name)** → $($_.Count) conexões"
}

@"
## 🔹 4. Processos com conexões externas
"@ | Add-Content -Path $saida

$processosExternos | ForEach-Object {
@"
### Processo: $($_.Processo)
- **PID:** $($_.PID)
- **Caminho:** $($_.Caminho)
- **IP remoto:** $($_.IP_Remoto):$($_.Porta_Remota)
- **Estado:** $($_.Estado)

---
"@ | Add-Content -Path $saida
}

@"
## 🔹 5. IPs desconhecidos e possíveis riscos
"@ | Add-Content -Path $saida

if ($ipsDesconhecidos.Count -eq 0) {
    Add-Content -Path $saida -Value "Nenhum IP suspeito encontrado. ✅"
} else {
    foreach ($ip in $ipsDesconhecidos) {
        Add-Content -Path $saida -Value "- **$($ip.IP_Remoto)** (Processo: $($ip.Processo)) → ⚠️ Verificar origem desconhecida."
    }
}

@"

---
📁 **Relatório salvo em:** $saida
"@ | Add-Content -Path $saida

Write-Host "✅ Relatório final gerado com sucesso: $saida" -ForegroundColor Green
