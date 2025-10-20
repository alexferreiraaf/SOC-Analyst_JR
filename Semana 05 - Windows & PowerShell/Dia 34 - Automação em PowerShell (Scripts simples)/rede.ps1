# rede.ps1
# Testa conexão com a internet e salva resultado no log

if (Test-Connection 8.8.8.8 -Count 1 -Quiet) {
    "Internet OK - $(Get-Date)" | Out-File -FilePath rede.log -Append
} else {
    "Sem conexão - $(Get-Date)" | Out-File -FilePath rede.log -Append
}
