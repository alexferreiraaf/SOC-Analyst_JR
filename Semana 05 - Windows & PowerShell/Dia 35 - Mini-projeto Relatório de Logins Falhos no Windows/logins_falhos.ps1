# logins_falhos.ps1
# Extrai eventos 4625 (logons falhos) e gera relatório CSV resumido

$maxEvents = 1000
$saida = "logins_falhos.csv"

$events = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents $maxEvents

$report = foreach ($e in $events) {
    $msg = $e.Message
    $ip = if ($msg -match 'Source Network Address:\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)') { $Matches[1] } else { "-" }
    $acct = if ($msg -match 'Account Name:\s+(\S+)') { $Matches[1] } else { "-" }
    $logonType = if ($msg -match 'Logon Type:\s+(\d+)') { $Matches[1] } else { "-" }

    [PSCustomObject]@{
        Time = $e.TimeCreated
        Account = $acct
        IP = $ip
        LogonType = $logonType
        Message = ($msg -replace "`r`n", " ")
    }
}

$report | Export-Csv -Path $saida -NoTypeInformation -Encoding utf8
Write-Host "Relatório gerado com sucesso: $saida (Total: $($report.Count) eventos)"

