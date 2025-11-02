# parse_failed.ps1
$pattern = "Failed\s+password\s+for\s+(?:invalid\s+user\s+)?(?<user>\S+)\s+from\s+(?<ip>(?:\d{1,3}\.){3}\d{1,3})"
Get-Content .\auth_sample.log | ForEach-Object {
    if ($_ -match $pattern) {
        [PSCustomObject]@{
            Time = ($_ -match '\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}') ? $Matches[0] : ""
            User = $Matches['user']
            IP = $Matches['ip']
            Raw = $_
        }
    }
} | Export-Csv -Path logins_falhos_ps.csv -NoTypeInformation -Encoding utf8

