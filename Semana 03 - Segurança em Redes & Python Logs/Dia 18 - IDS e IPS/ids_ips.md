# ids_ips.md

# Dia 18 — IDS e IPS

---

## 1. Explicações teóricas

### IDS (Intrusion Detection System)
- **Função:** monitorar tráfego e gerar **alertas** quando identifica atividades suspeitas ou maliciosas.
- **Comportamento:** *passivo* — registra e alerta, não altera o tráfego.
- **Uso típico:** detecção de scans, reconhecimento e comportamentos anômalos para posterior investigação.

### IPS (Intrusion Prevention System)
- **Função:** detectar **e prevenir** intrusões — pode **bloquear** ou **quarentenar** tráfego automaticamente.
- **Comportamento:** *ativo* — descarta pacotes, envia reset (RST), aplica rate-limits, etc.
- **Uso típico:** proteção inline contra exploits conhecidos, mitigação de DoS simples, bloqueio automático de payloads maliciosos.

---

## 2. Modos de Detecção

### Baseado em Assinatura (Signature-based)
- Compara tráfego com um conjunto de assinaturas (padrões) conhecidos.
- **Prós:** preciso para ameaças conhecidas; baixos falsos positivos quando bem afinado.
- **Contras:** não identifica facilmente ataques *zero-day* (novos) sem assinatura.

### Baseado em Anomalia (Anomaly-based)
- Aprende o comportamento normal da rede e alerta quando detecta desvios.
- **Prós:** pode detectar ataques novos / desconhecidos.
- **Contras:** normalmente gera mais falsos positivos até que o modelo seja ajustado.

---

## 3. Modos de Prevenção (ações que um IPS pode executar)
- **Drop** — descartar pacotes maliciosos silenciosamente.  
- **Reject** — descartar e enviar resposta (ex.: TCP RST).  
- **Alert + Block** — gerar alerta e acrescentar bloqueio dinâmico (ex.: ACL temporária).  
- **Rate Limiting / Throttling** — reduzir a taxa de pacotes para mitigar DoS.  
- **Redirect / Quarantine** — redirecionar tráfego suspeito para um ambiente de análise ou isolar host.

---

## 4. Exemplos práticos de logs (formatos e interpretação)

### Exemplo Snort (alerta de ICMP ping)
[] [1:1000001:0] ICMP Ping detected []
[Priority: 3] {ICMP} 192.168.1.100 -> 192.168.1.1

**Interpretação:** assinatura de ping/ICMP identificada. Prioridade média; investigar origem.

### Exemplo Suricata (drop de SQL Injection)
10/03/2025-15:12:45.123456 [Drop] [1:2010935:2] SQL Injection attempt detected [**]
{TCP} 192.168.50.120:34567 -> 10.10.10.20:80

**Interpretação:** Suricata bloqueou requisição HTTP com padrão de SQLi; evento classificado como Drop.

### Exemplo (anomaly / DoS)
[] [1:1000003:0] ICMP Flood detected []
[Priority: 1] {ICMP} 192.168.1.40 -> 192.168.1.30
Count: 500 pkts/sec

**Interpretação:** tráfego ICMP fora do normal — possível DoS. Pode-se aplicar rate limiting.

> Observação: formatos variam entre ferramentas (Snort: `/var/log/snort/alert`; Suricata: `/var/log/suricata/fast.log` ou eve.json).

---

## 5. Diferença IDS / IPS (resumo objetivo)

- **IDS** = detecta + alerta (passivo).  
- **IPS** = detecta + previne (ativo) — bloqueia/descarta/quarentena.  
- **Onde colocar:** IDS normalmente em modo espelho (span/mirror) ou inline passivo; IPS precisa estar inline (no caminho do tráfego) para poder bloquear.

---

## 6. Três ataques detectáveis (com breve explicação)

1. **Port Scan (Nmap)**  
   - O IDS detecta varredura de portas (séries de SYN/ACK/FIN incomuns) e sinaliza o IP que varre.  
2. **SQL Injection (payload via HTTP)**  
   - Assinaturas que identificam strings/padrões típicos em URIs ou POST bodies são disparadas — IPS pode bloquear a requisição.  
3. **DoS / ICMP Flood**  
   - Anomalia de volume (muitos pacotes em curto período) dispara alertas; IPS pode aplicar rate limiting ou drop.

---

## 7. Como IDS/IPS complementam o firewall

- **Firewall:** controla portas, IPs e protocolos (filtro baseado em camada 3/4).  
- **IDS/IPS:** inspecionam o **conteúdo** do tráfego (camadas superiores) e detectam/podem bloquear ataques que passam por portas autorizadas (ex.: SQLi sobre HTTP/80).  
- **Fluxo prático:** firewall permite 80/443 → IPS analisa payload HTTP → IPS bloqueia payload malicioso → IDS gera logs/alertas para investigação.

---

## 8. Exercícios práticos realizados (sugestões e evidências a documentar)

> Execute sempre em ambiente controlado / laboratório.

1. **Detecção de Port Scan com Snort (IDS)**  
   - Configuração: Snort em modo console monitorando `eth0`.  
   - Ataque de teste: `nmap -sS <IP alvo>` (rodar em lab).  
   - Evidência: alerta Snort com mensagem de scan.

2. **Bloqueio de SQL Injection com Suricata (IPS)**  
   - Configuração: Suricata em modo inline / AF_PACKET com regras que detectam padrões `"' OR '1'='1"`.  
   - Teste: `curl "http://<web-lab>/login.php?user=admin' OR '1'='1"` (em lab).  
   - Evidência: Suricata registra `Drop` e cliente recebe 403/reset (ou equivalente).

3. **ICMP Flood detectado como anomalia**  
   - Configuração: regra de threshold/alerta para ICMP volumes altos.  
   - Teste: `ping -f -s 1000 <IP alvo>` (lab controlado).  
   - Evidência: alerta de DoS/ICMP flood com contadores.

4. **Exploit (EternalBlue) — bloqueio por IPS (simulado)**  
   - **Importante:** **não executar exploits reais** fora de ambiente controlado. Para testes, use simuladores ou gere tráfego com assinatura equivalente.  
   - Objetivo do exercício: confirmar que uma assinatura de exploit existente geraria `Drop`/`Reject` no IPS e log apropriado.

5. **Integração Firewall + IDS/IPS (simulada)**  
   - Configurar firewall para permitir HTTP.  
   - Gerar payload malicioso (SQLi) e observar: firewall não bloqueia (porta permitida), IDS alerta e IPS bloqueia; logs centralizados no SIEM.

---

## 9. Comandos úteis (exemplos para laboratório)

### Snort (rodar em console)
```bash
sudo snort -A console -i eth0 -c /etc/snort/snort.conf

Suricata (rodar em modo manual)
sudo suricata -c /etc/suricata/suricata.yaml -i eth0
# ou rodar como serviço
sudo systemctl start suricata
sudo tail -f /var/log/suricata/fast.log

Exemplos de verificação de logs
sudo tail -n 200 /var/log/snort/alert
sudo tail -f /var/log/suricata/eve.json

Reflexão — Como usaria firewall, IDS e IPS num SOC pequeno

Se eu montasse um SOC pequeno, organizaria as camadas assim:

Firewall (borda) — política default deny para serviços públicos, bloco de portas irrelevantes.

IPS inline — bloqueio automático para assinaturas críticas (exploit conhecidos, malwares que causam impacto imediato). IPS deve ser bem testado (tuning) para evitar interrupção de serviço por falsos positivos.

IDS em modo monitor — captura e registra tráfego para análise histórica, correlação e investigação (útil para detecção de anomalias e evidências).

Centralização de logs (SIEM) — enviar alertas/fluxos do firewall, IDS/IPS e hosts para um SIEM leve (ex.: ELK/Wazuh) para correlação e criação de alertas acionáveis.

Processo de resposta — playbooks simples: triagem, bloqueio temporário, coleta de evidências, escalonamento.

11. Segurança e ética

Testes de intrusão e geração de tráfego malicioso devem ser realizados apenas em laboratórios controlados ou com autorização explícita.

Nunca execute exploits em redes de produção ou sem permissão.

12. Referências rápidas e próximos passos

Ferramentas: Snort, Suricata, Zeek, ELK Stack, Wazuh.

Próximo passo sugerido: configurar Suricata + Filebeat → ELK/Kibana para dashboards de alertas; praticar tuning de regras para reduzir falsos positivos.
