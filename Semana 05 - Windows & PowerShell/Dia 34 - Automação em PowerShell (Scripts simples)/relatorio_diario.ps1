# relatorio_diario.ps1
# Gera um relat�rio di�rio com informa��es do sistema

# Coletando dados b�sicos
$pc = $env:COMPUTERNAME
$usuario = $env:USERNAME
$data = Get-Date -Format "yyyy-MM-dd"
$arquivo = "relatorio_diario_$data.md"

# Cabe�alho
"Relat�rio Di�rio - $data" | Out-File $arquivo
"PC: $pc" | Out-File $arquivo -Append
"Usu�rio: $usuario" | Out-File $arquivo -Append
"" | Out-File $arquivo -Append

# Processos por CPU
"Top 5 Processos por CPU:" | Out-File $arquivo -Append
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5 Name, CPU | Out-File $arquivo -Append
"" | Out-File $arquivo -Append

# Servi�os parados
"5 Servi�os parados:" | Out-File $arquivo -Append
Get-Service | Where-Object {$_.Status -eq "Stopped"} | Select-Object -First 5 Name, Status | Out-File $arquivo -Append
"" | Out-File $arquivo -Append

Write-Host "Relat�rio gerado com sucesso: $arquivo"
