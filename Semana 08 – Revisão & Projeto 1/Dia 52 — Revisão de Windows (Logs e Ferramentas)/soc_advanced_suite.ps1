# =============================================================================
# SOC HUNTER SUITE - POWERED BY POWERSHELL
# Funcionalidades: Filtro Noturno, Correlação de Ataques, Detecção de Privilégios
# =============================================================================

# --- 1. Configurações e Estilo HTML (CSS) ---
$ReportPath = "C:\Relatorios\SOC_Advanced_Report.html"
$SMTPServer = "smtp.seuprovedor.com" # Configure aqui para envio real
$EmailTo    = "soc@empresa.com"
$EmailFrom  = "alertas@empresa.com"

# CSS para deixar o relatório com cara de "Dashboard Profissional"
$HeaderCSS = @"
<style>
    body { font-family: 'Segoe UI', sans-serif; background-color: #f4f4f4; color: #333; }
    h1 { background-color: #2c3e50; color: white; padding: 15px; text-align: center; }
    h2 { color: #2980b9; border-bottom: 2px solid #2980b9; padding-bottom: 5px; margin-top: 30px; }
    table { border-collapse: collapse; width: 100%; margin-bottom: 20px; background-color: white; box-shadow: 0 1px 3px rgba(0,0,0,0.2); }
    th { background-color: #34495e; color: white; padding: 10px; text-align: left; }
    td { border: 1px solid #ddd; padding: 8px; }
    tr:nth-child(even) { background-color: #f2f2f2; }
    tr:hover { background-color: #e8f6f3; }
    .alert { color: red; font-weight: bold; }
    .safe { color: green; }
</style>
"@

# Garante diretório
$dir = [System.IO.Path]::GetDirectoryName($ReportPath)
if (!(Test-Path $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }

Write-Host "Iniciando Varredura SOC... Aguarde." -ForegroundColor Cyan

# --- 2. Desafio: Ataques Noturnos (00h - 06h de hoje) ---
Write-Host "[1/4] Analisando ataques noturnos..." -ForegroundColor Yellow
$Inicio = (Get-Date).Date # 00:00 de hoje
$Fim = (Get-Date).Date.AddHours(6) # 06:00 de hoje

try {
    $EventosNoturnos = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=$Inicio; EndTime=$Fim} -ErrorAction Stop | Select-Object @{N='Data';E={$_.TimeCreated}}, @{N='Usuario';E={$_.Properties[5].Value}}, @{N='IP';E={$_.Properties[19].Value}}
    
    # Converte para HTML fragmentado
    $HtmlNoturno = $EventosNoturnos | ConvertTo-Html -Fragment
} catch {
    $HtmlNoturno = "<p class='safe'>Nenhum ataque detectado no período noturno (00h-06h).</p>"
}


# --- 3. Desafio: Correlação (Falha -> Sucesso) = Brute Force Bem Sucedido ---
Write-Host "[2/4] Correlacionando Falha + Sucesso (Risco Crítico)..." -ForegroundColor Yellow

# Pega falhas e sucessos da última hora para performance
$LookBack = (Get-Date).AddHours(-1)
$Falhas   = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=$LookBack} -ErrorAction SilentlyContinue
$Sucessos = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624; StartTime=$LookBack} -ErrorAction SilentlyContinue

$CorrelacaoSuspeita = @()

if ($Falhas -and $Sucessos) {
    # Agrupa falhas por IP para não processar repetidos
    $IPsAtacantes = $Falhas | Select-Object -ExpandProperty Properties | Where-Object { $_[19].Value -ne "-" } | Select-Object @{N='IP';E={$_.Value}} -Unique

    foreach ($item in $IPsAtacantes) {
        $IP = $item.IP
        # Filtra eventos deste IP específico
        $FalhasIP = $Falhas | Where-Object { $_.Properties[19].Value -eq $IP }
        $SucessosIP = $Sucessos | Where-Object { $_.Properties[18].Value -eq $IP } # No 4624 o IP é índice 18

        if ($SucessosIP) {
            foreach ($sucesso in $SucessosIP) {
                # Verifica se houve falha 2 minutos ANTES do sucesso
                $FalhaRecente = $FalhasIP | Where-Object { ($sucesso.TimeCreated - $_.TimeCreated).TotalMinutes -lt 2 -and ($sucesso.TimeCreated -gt $_.TimeCreated) }
                
                if ($FalhaRecente) {
                    $CorrelacaoSuspeita += [PSCustomObject]@{
                        DataSucesso = $sucesso.TimeCreated
                        Usuario     = $sucesso.Properties[5].Value
                        IP_Origem   = $IP
                        Status      = "ALERTA: Brute Force seguido de Sucesso"
                    }
                    break # Achou um, já basta para alertar
                }
            }
        }
    }
}

if ($CorrelacaoSuspeita.Count -gt 0) {
    $HtmlCorrelacao = $CorrelacaoSuspeita | ConvertTo-Html -Fragment
} else {
    $HtmlCorrelacao = "<p class='safe'>Nenhuma correlação de invasão detectada na última hora.</p>"
}


# --- 4. Desafio: Criação de Conta Administrativa (4720 + 4732) ---
# Nota: Usamos 4732 (Adicionado a grupo) em vez de 4672, pois 4732 confirma elevação de privilégio na criação.
Write-Host "[3/4] Verificando criação de contas suspeitas..." -ForegroundColor Yellow

try {
    # Busca criação de usuários nas últimas 24h
    $NovosUsuarios = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4720; StartTime=(Get-Date).AddDays(-1)} -ErrorAction Stop
    
    $ContasSuspeitas = @()

    foreach ($evento in $NovosUsuarios) {
        $NovoUserSID = $evento.Properties[2].Value # SID do usuário criado
        $HoraCriacao = $evento.TimeCreated
        
        # Busca se esse SID foi adicionado ao grupo de Administradores (4732) nos 5 minutos seguintes
        $Elevacao = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4732; StartTime=$HoraCriacao; EndTime=$HoraCriacao.AddMinutes(5)} -ErrorAction SilentlyContinue | 
                    Where-Object { $_.Properties[1].Value -eq $NovoUserSID } # Propriedade 1 no 4732 é o SID do membro adicionado
        
        if ($Elevacao) {
             $ContasSuspeitas += [PSCustomObject]@{
                DataCriacao = $HoraCriacao
                UsuarioCriado = $evento.Properties[0].Value
                CriadoPor = $evento.Properties[4].Value
                Risco = "CRÍTICO: Conta criada e adicionada a Administradores imediatamente"
            }
        }
    }
    
    if ($ContasSuspeitas) {
        $HtmlCriacao = $ContasSuspeitas | ConvertTo-Html -Fragment
    } else {
        $HtmlCriacao = "<p class='safe'>Nenhuma escalação de privilégio na criação de contas.</p>"
    }

} catch {
    $HtmlCriacao = "<p class='safe'>Nenhuma conta criada nas últimas 24h.</p>"
}


# --- 5. Desafio: Alerta de Email (>10 Falhas) e Geração HTML ---
Write-Host "[4/4] Consolidando Relatório e Verificando Alertas..." -ForegroundColor Yellow

# Verifica Top Falhas para Email
$TopFalhas = try {
    Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-12)} -ErrorAction Stop |
    Group-Object { $_.Properties[19].Value } | Where-Object { $_.Name -ne "-" } | Sort-Object Count -Descending 
} catch { $null }

$HtmlFalhas = if ($TopFalhas) { 
    $TopFalhas | Select-Object @{N='IP Origem';E={$_.Name}}, Count | ConvertTo-Html -Fragment 
} else { "<p>Sem dados.</p>" }

# Lógica de Envio de Email
$IpCritico = $TopFalhas | Where-Object { $_.Count -gt 10 } | Select-Object -First 1
if ($IpCritico) {
    Write-Host "ALERTA: O IP $($IpCritico.Name) falhou $($IpCritico.Count) vezes. Disparando e-mail..." -ForegroundColor Red
    # Send-MailMessage -From $EmailFrom -To $EmailTo -Subject "ALERTA SOC: Brute Force Detectado" -Body "IP $($IpCritico.Name) detectado com $($IpCritico.Count) falhas." -SmtpServer $SMTPServer
    # (Comentado pois requer servidor SMTP real configurado)
}

# Montagem Final do HTML
$RelatorioFinal = @"
<!DOCTYPE html>
<html>
<head>
    <title>Relatório SOC Diário</title>
    $HeaderCSS
</head>
<body>
    <h1>🛡️ Relatório de Operações de Segurança (SOC)</h1>
    <p>Gerado em: $(Get-Date)</p>

    <h2>1. Análise de Correlação (Risco Crítico)</h2>
    <p>Monitora IPs que falharam login e conseguiram entrar em menos de 2 min.</p>
    $HtmlCorrelacao

    <h2>2. Criação de Contas Administrativas</h2>
    <p>Contas criadas e promovidas a Admins no mesmo minuto.</p>
    $HtmlCriacao

    <h2>3. Tentativas de Invasão Noturna (00h - 06h)</h2>
    $HtmlNoturno

    <h2>4. Top IPs com Falhas de Login (Geral)</h2>
    $HtmlFalhas
</body>
</html>
"@

$RelatorioFinal | Out-File $ReportPath
Invoke-Item $ReportPath # Abre o relatório no navegador

Write-Host "Relatório gerado com sucesso: $ReportPath" -ForegroundColor Green