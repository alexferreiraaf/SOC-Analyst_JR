# relatorio_sistema.ps1
$data = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$arquivo = "relatorio_$data.md"

"Relat�rio do sistema gerado em $data" | Out-File $arquivo
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 | Out-File -Append $arquivo
Get-Service | Where-Object {$_.Status -eq "Running"} | Select-Object -First 10 | Out-File -Append $arquivo

Write-Host "Relat�rio salvo em $arquivo"

