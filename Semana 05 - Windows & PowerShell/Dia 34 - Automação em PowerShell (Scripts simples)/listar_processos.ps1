# listar_processos.ps1
Get-Process | Select-Object Name, Id, CPU |
Sort-Object -Property CPU -Descending |
Out-File -FilePath processos_top.md -Encoding utf8

Write-Host "Arquivo processos_top.md gerado com sucesso!"

