# 1. Garante que a pasta existe
$caminho = "C:\Relatorios"
if (!(Test-Path $caminho)) { New-Item -ItemType Directory -Path $caminho | Out-Null }

# 2. Coleta os logs com limite para não travar
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 500 -ErrorAction SilentlyContinue |
ForEach-Object {
    # Cria um objeto personalizado (Custom Object) para limpar os dados
    [PSCustomObject]@{
        DataHora  = $_.TimeCreated
        Usuario   = $_.Properties[5].Value  # Nome da conta tentada
        Dominio   = $_.Properties[6].Value  # Domínio
        IP_Origem = $_.Properties[19].Value # IP do atacante
        Motivo    = $_.Properties[8].Value  # Tipo de falha (ex: senha errada, conta bloqueada)
    }
} | 
# 3. Exporta com codificação correta para abrir no Excel BR
Export-Csv -Path "$caminho\falhas_logon_limpo.csv" -NoTypeInformation -Encoding UTF8

Write-Host "Relatório gerado com sucesso em $caminho\falhas_logon_limpo.csv" -ForegroundColor Green