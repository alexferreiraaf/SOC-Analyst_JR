# inventario_sistema.ps1
# Script simples para gerar inventário do sistema

Write-Host "Gerando relatório de processos..."
Get-Process | Out-File processos.md

Write-Host "Gerando relatório de serviços..."
Get-Service | Out-File servicos.md

Write-Host "Gerando informações do sistema..."
Get-ComputerInfo | Out-File info_sistema.md

Write-Host "Relatórios gerados com sucesso!"
