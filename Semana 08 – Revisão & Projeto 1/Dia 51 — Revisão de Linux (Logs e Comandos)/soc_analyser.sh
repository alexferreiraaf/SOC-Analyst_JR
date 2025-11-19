#!/bin/bash

# ==========================================
# SOC ANALYSER TOOL - DIA 51
# Autor: Gemini & Você
# Descrição: Análise completa de logs SSH
# ==========================================

# --- Configurações ---
MEU_PAIS="BR"              # Seu código de país (ISO 3166-1 alpha-2)
LIMITE_FALHAS=10           # Limite para disparar alerta
ARQUIVO_CSV="relatorio_incidentes.csv"
ARQUIVO_GRAFICO="grafico_ataques.png"
TEMP_DATA="/tmp/dados_brutos_ssh.txt"

# --- Cores para Output ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 1. Verificação de Privilégios
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}[ERRO] Este script precisa ser executado como ROOT (sudo) para ler os logs.${NC}"
   exit 1
fi

# 2. Detecção Automática do Log
if [ -f "/var/log/auth.log" ]; then
    LOG_FILE="/var/log/auth.log"
elif [ -f "/var/log/secure" ]; then
    LOG_FILE="/var/log/secure" # CentOS/RHEL
else
    echo -e "${RED}[ERRO] Arquivo de log de autenticação não encontrado!${NC}"
    exit 1
fi

echo -e "${BLUE}=== INICIANDO ANÁLISE SOC ===${NC}"
echo -e "Arquivo de Log alvo: ${YELLOW}$LOG_FILE${NC}"

# 3. Verificação de Dependências
echo -ne "Checando dependências... "
if ! command -v gnuplot &> /dev/null; then
    echo -e "${YELLOW}Instalando gnuplot...${NC}"
    apt-get install gnuplot -y &> /dev/null || yum install gnuplot -y &> /dev/null
fi
if ! command -v jq &> /dev/null; then
    echo -e "${YELLOW}Instalando jq...${NC}"
    apt-get install jq -y &> /dev/null || yum install jq -y &> /dev/null
fi
echo -e "${GREEN}OK!${NC}"

# --- EXTRAÇÃO DE DADOS (Feita uma única vez para otimizar) ---
echo -e "${BLUE}[1/4] Processando arquivo de log...${NC}"
# Extrai IP, Mês, Dia, Hora
grep "Failed password" "$LOG_FILE" | awk '{
    for(i=1;i<=NF;i++) if($i=="from") ip=$(i+1);
    print ip, $1, $2, $3
}' > "$TEMP_DATA"

TOTAL_FALHAS=$(wc -l < "$TEMP_DATA")
echo -e "Total de falhas encontradas: ${RED}$TOTAL_FALHAS${NC}"

# --- TAREFA 1 & 2: CSV e ALERTAS ---
echo -e "${BLUE}[2/4] Gerando Relatório CSV e Verificando Alertas...${NC}"
echo "IP,Tentativas,Ultima_Ocorrencia" > "$ARQUIVO_CSV"

# Processa o arquivo temporário para contar ocorrências
sort "$TEMP_DATA" | uniq -c | while read count ip mes dia hora; do
    # Adiciona ao CSV
    echo "$ip,$count,$mes $dia $hora" >> "$ARQUIVO_CSV"
    
    # Verifica Limite (Alerta)
    if [ "$count" -gt "$LIMITE_FALHAS" ]; then
        echo -e "${RED}[ALERTA]${NC} IP $ip realizou $count tentativas (Limite: $LIMITE_FALHAS)"
        # Aqui você poderia descomentar o comando de email:
        # echo "Alerta: IP $ip excedeu limite" | mail -s "SOC ALERT" user@local
    fi
done

echo -e "${GREEN}Relatório salvo em: $ARQUIVO_CSV${NC}"

# --- TAREFA 3: GRÁFICO (GNUPLOT) ---
echo -e "${BLUE}[3/4] Gerando Gráfico de Ataques por Hora...${NC}"
DADOS_GRAFICO="/tmp/dados_plot.dat"

# Extrai apenas a hora (HH) e conta
awk '{print $4}' "$TEMP_DATA" | cut -d: -f1 | sort | uniq -c | awk '{print $2, $1}' > "$DADOS_GRAFICO"

if [ -s "$DADOS_GRAFICO" ]; then
gnuplot -persist <<-EOFMarker
    set terminal png size 800,600
    set output '$ARQUIVO_GRAFICO'
    set title "Atividade Maliciosa por Hora (SSH)"
    set xlabel "Hora do Dia (00-23)"
    set ylabel "Tentativas Bloqueadas"
    set style data histograms
    set style fill solid border -1
    set boxwidth 0.7
    set grid y
    plot "$DADOS_GRAFICO" using 2:xtic(1) title 'Tentativas' lc rgb "red"
EOFMarker
    echo -e "${GREEN}Gráfico gerado: $ARQUIVO_GRAFICO${NC}"
else
    echo -e "${YELLOW}Dados insuficientes para gerar gráfico.${NC}"
fi

# --- TAREFA 4: GEOLOCALIZAÇÃO ---
echo -e "${BLUE}[4/4] Analisando Origem Geográfica (Top 5 IPs)...${NC}"
echo "Nota: Limitado a 5 IPs para não bloquear a API pública."

# Pega os Top 5 IPs com mais falhas
awk '{print $1}' "$TEMP_DATA" | sort | uniq -c | sort -nr | head -n 5 | while read count ip; do
    # Consulta API
    pais=$(curl -s "ipinfo.io/$ip/country" | tr -d ' \n')
    
    if [[ -n "$pais" && "$pais" != "$MEU_PAIS" ]]; then
        echo -e "IP: $ip | Falhas: $count | Origem: ${RED}$pais (ESTRANGEIRO)${NC}"
    else
        echo -e "IP: $ip | Falhas: $count | Origem: ${GREEN}$pais${NC}"
    fi
    sleep 1 # Respeitar API rate limit
done

# Limpeza
rm "$TEMP_DATA" 2>/dev/null
rm "$DADOS_GRAFICO" 2>/dev/null

echo -e "${BLUE}=== ANÁLISE CONCLUÍDA ===${NC}"
