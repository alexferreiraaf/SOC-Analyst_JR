# processos.ps1
# Lista os 10 processos que mais usam mem�ria
# E verifica se o navegador Opera est�o aberto

$top10 = Get-Process | Sort-Object WS -Descending | Select-Object -First 10
$top10

if (Get-Process | Where-Object { $_.Name -eq "opera" }) {
    Write-Host "Navegador aberto"
}
