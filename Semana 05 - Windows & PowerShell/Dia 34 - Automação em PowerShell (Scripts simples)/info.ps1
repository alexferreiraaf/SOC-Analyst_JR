# info.ps1
# Script básico para exibir e salvar informações do sistema

$pc = $env:COMPUTERNAME
$user = $env:USERNAME
$data = Get-Date

Write-Host "Nome do computador: $pc"
Write-Host "Usuario atual: $user"
Write-Host "Data e hora: $data"

"Computador: $pc" | Out-File info.md
"Usuario: $user" | Out-File info.md -Append
"Data e hora: $data" | Out-File info.md -Append
