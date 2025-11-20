# ==================================================
# FERRAMENTA DE INVESTIGAÇÃO DE INCIDENTE - CASO 01
# Objetivo: Correlacionar Brute Force -> Sucesso -> Admin
# ==================================================

# 1. Definição do Escopo Temporal (01:00 às 02:00 de Hoje)
# Para alterar a data, mude (Get-Date).Date para Get-Date "2025-11-19"
$DataAlvo = (Get-Date).Date 
$Inicio   = $DataAlvo.AddHours(1) # 01:00
$Fim      = $DataAlvo.AddHours(2) # 02:00

Write-Host "--- INICIANDO ANÁLISE FORENSE ---" -ForegroundColor Cyan
Write-Host "Janela de Tempo: $Inicio até $Fim" -ForegroundColor Gray

# 2. Coleta de Evidências
Write-Host "[1/3] Coletando logs de falha (4625)..." -ForegroundColor Yellow
$Falhas = try {
    Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=$Inicio; EndTime=$Fim} -ErrorAction Stop
} catch { $null }

Write-Host "[2/3] Coletando logs de sucesso (4624)..." -ForegroundColor Yellow
$Sucessos = try {
    Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624; StartTime=$Inicio; EndTime=$Fim} -ErrorAction Stop
} catch { $null }

# 3. Correlação (O motor da investigação)
if ($Falhas -and $Sucessos) {
    
    # Extrai IPs únicos que falharam
    $IPsSuspeitos = $Falhas | ForEach-Object { $_.Properties[19].Value } | Select-Object -Unique | Where-Object { $_ -ne "-" }

    foreach ($IP in $IPsSuspeitos) {
        # Verifica se esse IP também teve sucesso
        $LogonSucesso = $Sucessos | Where-Object { $_.Properties[18].Value -eq $IP } | Sort-Object TimeCreated -Descending | Select-Object -First 1

        if ($LogonSucesso) {
            # Temos um "Match"! (Falha + Sucesso do mesmo IP)
            
            # Pega a PRIMEIRA falha desse IP na janela de tempo
            $PrimeiraFalha = $Falhas | Where-Object { $_.Properties[19].Value -eq $IP } | Sort-Object TimeCreated | Select-Object -First 1
            
            # Cálculos
            $UsuarioComprometido = $LogonSucesso.Properties[5].Value
            $TempoDecorrido = New-TimeSpan -Start $PrimeiraFalha.TimeCreated -End $LogonSucesso.TimeCreated
            
            Write-Host "`n🚨 ALERTA CONFIRMADO: COMPROMETIMENTO DETECTADO!" -ForegroundColor Red
            Write-Host "--------------------------------------------------"
            Write-Host "IP do Atacante:      $IP"
            Write-Host "Usuário Afetado:     $UsuarioComprometido"
            Write-Host "Primeira Tentativa:  $($PrimeiraFalha.TimeCreated)"
            Write-Host "Sucesso obtido em:   $($LogonSucesso.TimeCreated)"
            Write-Host "Duração do Ataque:   $($TempoDecorrido.Minutes) minutos e $($TempoDecorrido.Seconds) segundos"

            # 4. Verificação de Privilégios (4672)
            # O evento 4672 acontece no mesmo segundo do 4624 para admins
            Write-Host "`n[3/3] Verificando privilégios administrativos..." -ForegroundColor Yellow
            
            $IsAdmin = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4672; StartTime=$LogonSucesso.TimeCreated.AddSeconds(-1); EndTime=$LogonSucesso.TimeCreated.AddSeconds(1)} -ErrorAction SilentlyContinue | 
                       Where-Object { $_.Properties[1].Value -eq $UsuarioComprometido } # Propriedade 1 é o nome do usuário no 4672

            if ($IsAdmin) {
                Write-Host "⚠️  NÍVEL CRÍTICO: O usuário obteve privilégios de Administrador (Evento 4672 encontrado)." -ForegroundColor Red -BackgroundColor White
            } else {
                Write-Host "ℹ️  Nível Médio: Usuário comum (Sem evento 4672 associado)." -ForegroundColor Green
            }
            Write-Host "--------------------------------------------------"
        }
    }
} else {
    Write-Host "Nenhuma correlação de ataque encontrada nesta janela de tempo." -ForegroundColor Green
}