# listar_servicos.ps1
param (
    [string]$Status = "Running"
)

Write-Host "Listando serviços com status: $Status"
Get-Service | Where-Object {$_.Status -eq $Status} |
Select-Object Name, Status | Out-File "servicos_$Status.md"

Write-Host "Arquivo servicos_$Status.md gerado."

