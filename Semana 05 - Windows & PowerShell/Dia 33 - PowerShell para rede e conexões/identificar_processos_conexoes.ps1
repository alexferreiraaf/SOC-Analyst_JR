# identificar_processos_conexoes.ps1
# Lista conexões TCP externas e identifica os processos responsáveis

# Arquivo de saída
$saida = "processos_conexoes.md"

# Cabeçalho do relatório
@"
# Relatório de Processos com Conexões Externas

Gerado em: $(Get-Date -Format 'dd/MM/yyyy HH:mm:ss')

## Processos com conexões externas
"@ | Out-File -FilePath $saida -Encoding utf8

# Obter todas as conexões externas (RemoteAddress diferente de 127.0.0.1 ou ::1)
$conexoes = Get-NetTCPConnection | Where-Object {
    $_.RemoteAddress -and $_.RemoteAddress -notmatch "^(127\.0\.0\.1|::1|0\.0\.0\.0)$"
}

# Agrupar por processo
foreach ($conexao in $conexoes) {
    try {
        $processo = Get-Process -Id $conexao.OwningProcess -ErrorAction Stop
        $nomeProc = $processo.ProcessName
        $caminhoProc = $processo.Path
    } catch {
        $nomeProc = "Desconhecido"
        $caminhoProc = "N/A"
    }

    $linha = @"
### Processo: $nomeProc  
**PID:** $($conexao.OwningProcess)  
**Caminho:** $caminhoProc  
**Conexão:** $($conexao.LocalAddress):$($conexao.LocalPort) → $($conexao.RemoteAddress):$($conexao.RemotePort)  
**Estado:** $($conexao.State)

---
"@

    # Grava no relatório
    Add-Content -Path $saida -Value $linha
}

# Mensagem final
@"
## Resumo

Total de conexões externas: $($conexoes.Count)
Relatório salvo em: $saida
"@ | Add-Content -Path $saida

Write-Host "✅ Relatório salvo em $saida" -ForegroundColor Green
