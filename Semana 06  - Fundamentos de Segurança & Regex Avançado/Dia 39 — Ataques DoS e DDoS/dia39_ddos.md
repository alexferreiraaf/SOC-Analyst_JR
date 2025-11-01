# 💥 Dia 39 — Ataques DoS e DDoS

## 🎯 Objetivo do Dia
Compreender e identificar **ataques de negação de serviço (DoS/DDoS)**, detectar anomalias em logs e métricas, criar regras defensivas e montar um **playbook de resposta SOC**, utilizando apenas dados e simulações seguras.

---

## 🧠 Conceitos-Chave
- **DoS:** ataque de uma única origem.  
- **DDoS:** múltiplas origens (botnet distribuída).  
- **Vetores comuns:** SYN flood, UDP flood, ICMP flood, HTTP flood, slowloris, e amplification (NTP/DNS).  
- **Objetivo:** sobrecarregar banda, CPU, conexões ou recursos de aplicação.

---

## 🔍 Indicadores de Ataque (para o SOC)
- Pico súbito de tráfego ou conexões incompletas (SYN sem ACK).  
- Aumento de **HTTP 503 / timeout** em aplicações.  
- Conexões repetidas vindas de muitos IPs.  
- Alta taxa de **drops no firewall** ou alertas de IDS.  
- Métricas anormais em CPU, memória ou filas de rede.

---

## 🧩 Detecção (Consultas e Regras)

### 🟦 Splunk
Detectar picos de requisições HTTP:
```splunk
index=web_logs sourcetype=access_combined
| bin _time span=1m
| stats count as requests by _time, clientip
| eventstats avg(requests) as avg stdev(requests) as stdev by clientip
| where requests > avg + 3*stdev
| sort - requests
🟩 KQL (Sentinel)
Detectar aumento anormal de conexões TCP:

kql
Copiar código
CommonSecurityLog
| where DestinationPort == 80 or DestinationPort == 443
| summarize ConnCount = count() by SourceIP, bin(TimeGenerated, 5m)
| where ConnCount > 10 * avg(ConnCount)
🟥 Suricata / Snort
snort
Copiar código
alert tcp any any -> $HOME_NET any (msg:"Possible SYN flood";
flags:S; threshold:type threshold, track by_src, count 100, seconds 10; sid:1000001; rev:1;)
🧪 Análise Segura de PCAP
Filtros úteis no Wireshark:

tcp.flags.syn == 1 and tcp.flags.ack == 0 → SYN flood.

http.request → explosão de requisições HTTP.

udp or icmp → floods volumétricos.

Use apenas PCAPs públicos (CAIDA, MAWILab) em ambientes isolados.

🛡️ Mitigações e Defesa
Camadas de proteção:

Filtro no provedor (BGP blackhole, scrubbing).

CDN / WAF (Cloudflare, Akamai).

Rate limiting e limitação de conexões.

Firewalls e IPS com thresholds ajustados.

Autoescalonamento e redundância.

Blackhole controlado em casos críticos.

Ações rápidas:

Confirmar ataque → logs + métricas.

Aplicar rate limit e regras temporárias.

Bloquear regiões/IPs maliciosos.

Solicitar suporte ao ISP.

Escalar infraestrutura se necessário.

⚙️ Playbook SOC (Passo a Passo)
Detecção: alertas de tráfego e latência.

Triagem: verificar logs e métricas.

Enriquecimento: IPs, ASN, threat intel.

Containment: WAF, rate-limit, bloqueios temporários.

Erradicação: restabelecimento e estabilização do serviço.

Pós-incidente: relatório, métricas e ajustes de regras.

🧭 Exercícios Práticos
A) Analisar PCAP público (CAIDA, MAWILab).

B) Simular tráfego controlado (ex.: AWS Load Testing, k6).

C) Criar queries de detecção em SIEM.

D) Fazer simulação de resposta (table-top exercise).

📚 Recursos Úteis
CAIDA Datasets

MAWILab PCAPs

Cloudflare & Akamai blogs (casos reais)

Documentação WAF, SIEM, IDS (Splunk, ELK, Suricata, Zeek)

✅ Checklist do SOC
 Painéis e baselines de tráfego configurados.

 Alertas para picos de bytes/s ou pps ativos.

 Contatos de ISP/CDN prontos para mitigação.

 Playbook testado e atualizado.

 Comunicação externa planejada (status page, clientes).

