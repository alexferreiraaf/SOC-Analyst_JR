$logs = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 10
$logs | ForEach-Object {
    if ($_.Message -match "Source Network Address") {
        Write-Host "Falha detectada: $($_.TimeCreated) - $($_.Message.Split('`n')[0])"
    }
}

