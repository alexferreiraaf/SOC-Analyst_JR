# Dia 89 — Script SOC para Correlação de Eventos Críticos

$events = Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id = 4625,4624
} -MaxEvents 100 |
Sort-Object TimeCreated

$events | Select-Object `
    TimeCreated,
    Id,
    @{Name="User";Expression={$_.Properties[5].Value}},
    @{Name="IP";Expression={
        if ($_.Id -eq 4625) {$_.Properties[19].Value}
        elseif ($_.Id -eq 4624) {$_.Properties[18].Value}
    }} |
Format-Table -AutoSize
