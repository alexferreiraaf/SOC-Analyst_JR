# Busca os últimos 1000 eventos de falha de login (ID 4625)
$logs = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 1000 -ErrorAction SilentlyContinue

if ($logs) {
    $logs | ForEach-Object {
        # Pega o IP direto da propriedade (funciona em PT-BR e EN-US)
        $ip = $_.Properties[19].Value
        if ($ip -ne "-" -and $ip -ne "::1" -and $ip -ne $null) { 
            $ip 
        }
    } | Group-Object | Sort-Object Count -Descending | Select-Object -First 5
} else {
    Write-Host "Nenhuma falha de login recente encontrada nos logs." -ForegroundColor Yellow
}