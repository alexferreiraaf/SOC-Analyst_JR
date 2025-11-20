# Busca criação (4720) e exclusão (4726)
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=@(4720, 4726)} -MaxEvents 50 -ErrorAction SilentlyContinue | 
Select-Object TimeCreated, 
    Id, 
    @{N='Acao';E={if($_.Id -eq 4720){"CRIOU"}else{"DELETOU"}}},
    @{N='Quem_Fez_Isso';E={$_.Properties[4].Value}},
    @{N='Conta_Alvo';E={$_.Properties[0].Value}} | 
Format-Table -AutoSize