# processos.ps1
# Lista os 10 processos que mais usam memória
# E verifica se o navegador Opera estão aberto

$top10 = Get-Process | Sort-Object WS -Descending | Select-Object -First 10
$top10

if (Get-Process | Where-Object { $_.Name -eq "opera" }) {
    Write-Host "Navegador aberto"
}
