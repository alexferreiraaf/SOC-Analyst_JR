# --- Configuração Inicial ---
$dir = "C:\Relatorios"
$out = "$dir\relatorio_logs_audit.txt"

# 1. Garante que a pasta existe (Evita erro de caminho)
if (!(Test-Path $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }

# Cabeçalho
"=== Relatório de Segurança Windows ===" | Out-File $out
"Gerado em: $(Get-Date)" | Out-File $out -Append
"" | Out-File $out -Append

# --- SEÇÃO 1: FALHAS DE LOGON (4625) ---
"🔹 Top 5 IPs com falhas de logon (4625):" | Out-File $out -Append
try {
    $ips = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 1000 -ErrorAction Stop |
    ForEach-Object {
        # Pega IP direto da propriedade [19] (Universal)
        $ip = $_.Properties[19].Value
        if ($ip -ne "-" -and $ip -ne "::1" -and $ip -ne $null) { $ip }
    } | Group-Object | Sort-Object Count -Descending | Select-Object -First 5
    
    if ($ips) {
        $ips | Format-Table -AutoSize | Out-String | Out-File $out -Append
    } else {
        "Nenhuma falha com IP detectada." | Out-File $out -Append
    }
} catch {
    "Nenhum evento de falha de logon encontrado." | Out-File $out -Append
}

"" | Out-File $out -Append

# --- SEÇÃO 2: LOGONS BEM-SUCEDIDOS (4624) ---
"🔹 Últimos 5 logons bem-sucedidos (4624):" | Out-File $out -Append
try {
    Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624} -MaxEvents 5 -ErrorAction Stop |
    Select-Object TimeCreated, 
        @{N='Usuario';E={$_.Properties[5].Value}},
        @{N='Tipo_Logon';E={$_.Properties[8].Value}},
        @{N='IP_Origem';E={$_.Properties[18].Value}} |
    Format-Table -AutoSize | Out-String | Out-File $out -Append
} catch {
    "Nenhum logon recente encontrado." | Out-File $out -Append
}

"" | Out-File $out -Append

# --- SEÇÃO 3: CRIAÇÃO/DELEÇÃO DE USUÁRIOS (4720, 4726) ---
"🔹 Eventos de modificação de usuários (4720/4726):" | Out-File $out -Append
try {
    Get-WinEvent -FilterHashtable @{LogName='Security'; Id=@(4720,4726)} -MaxEvents 10 -ErrorAction Stop |
    Select-Object TimeCreated, 
        Id,
        @{N='Acao';E={if($_.Id -eq 4720){"CRIOU"}else{"DELETOU"}}},
        @{N='Conta_Afetada';E={$_.Properties[0].Value}},
        @{N='Quem_Fez';E={$_.Properties[4].Value}} |
    Format-Table -AutoSize | Out-String | Out-File $out -Append
} catch {
    "Nenhuma criação ou exclusão de usuário detectada recentemente." | Out-File $out -Append
}

Write-Host "Relatório gerado com sucesso em: $out" -ForegroundColor Green