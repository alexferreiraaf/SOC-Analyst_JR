Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624} -MaxEvents 20 | Select-Object TimeCreated, 
    @{N='Usuario';E={$_.Properties[5].Value}},
    @{N='Dominio';E={$_.Properties[6].Value}},
    @{N='LogonType';E={$_.Properties[8].Value}},
    @{N='IP_Origem';E={$_.Properties[18].Value}} | 
Format-Table -AutoSize