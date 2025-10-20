# processos_filtrados.ps1
$processos = Get-Process | Where-Object {$_.CPU -gt 1.0}
if ($processos) {
    $processos | Select-Object Name, Id, CPU | Out-File processos_cpu_acima_1.md
    Write-Host "Foram encontrados $($processos.Count) processos com CPU > 1.0"
} else {
    Write-Host "Nenhum processo acima de 1.0 CPU encontrado."
}

