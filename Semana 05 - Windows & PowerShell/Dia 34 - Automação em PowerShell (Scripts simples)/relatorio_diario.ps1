# relatorio_diario.ps1
# Gera um relatório diário com informações do sistema

# Coletando dados básicos
$pc = $env:COMPUTERNAME
$usuario = $env:USERNAME
$data = Get-Date -Format "yyyy-MM-dd"
$arquivo = "relatorio_diario_$data.md"

# Cabeçalho
"Relatório Diário - $data" | Out-File $arquivo
"PC: $pc" | Out-File $arquivo -Append
"Usuário: $usuario" | Out-File $arquivo -Append
"" | Out-File $arquivo -Append

# Processos por CPU
"Top 5 Processos por CPU:" | Out-File $arquivo -Append
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5 Name, CPU | Out-File $arquivo -Append
"" | Out-File $arquivo -Append

# Serviços parados
"5 Serviços parados:" | Out-File $arquivo -Append
Get-Service | Where-Object {$_.Status -eq "Stopped"} | Select-Object -First 5 Name, Status | Out-File $arquivo -Append
"" | Out-File $arquivo -Append

Write-Host "Relatório gerado com sucesso: $arquivo"
