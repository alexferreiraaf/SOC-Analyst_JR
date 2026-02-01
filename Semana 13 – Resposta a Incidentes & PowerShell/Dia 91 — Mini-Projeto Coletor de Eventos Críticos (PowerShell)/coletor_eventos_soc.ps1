# =========================================
# COLETOR SOC — EVENTOS CRÍTICOS WINDOWS
# Autor: Alex Ferreira
# Uso: Executar como Administrador
# =========================================

$BasePath = ".\coleta_eventos"
New-Item -ItemType Directory -Path $BasePath -Force | Out-Null

Write-Host "Iniciando coleta de eventos críticos..." -ForegroundColor Cyan

function Coletar-Eventos {
    param (
        [int[]]$EventID,
        [string]$Arquivo
    )

    Get-WinEvent -FilterHashtable @{
        LogName = 'Security'
        Id      = $EventID
    } -MaxEvents 200 |
    Select TimeCreated, Id, Message |
    Out-File "$BasePath\$Arquivo" -Encoding UTF8
}

# Coletas individuais
Coletar-Eventos -EventID 4625 -Arquivo "eventos_4625_falhas.txt"
Coletar-Eventos -EventID 4624 -Arquivo "eventos_4624_sucesso.txt"
Coletar-Eventos -EventID 4688 -Arquivo "eventos_4688_processos.txt"
Coletar-Eventos -EventID 4672 -Arquivo "eventos_4672_privilegios.txt"
Coletar-Eventos -EventID 4720 -Arquivo "eventos_4720_usuarios.txt"

# Timeline consolidada
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id      = 4625,4624,4688,4672,4720
} -MaxEvents 500 |
Sort-Object TimeCreated |
Select TimeCreated, Id, Message |
Out-File "$BasePath\timeline_eventos.txt" -Encoding UTF8

Write-Host "Coleta finalizada com sucesso." -ForegroundColor Green
