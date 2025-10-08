# semana3_resumo.md

# Semana 3 — Resumo de Aprendizado

## 🧠 O que foi aprendido
- **IDS / IPS (Snort, Suricata, Zeek):**
  - Diferença entre detecção (IDS) e prevenção (IPS).
  - Modos de detecção: assinatura (signature-based) e anomalia (anomaly-based).
  - Modos de prevenção típicos de IPS: drop, reject, alert+block, rate limiting, redirect/quarantine.
  - Onde posicionar IDS/IPS na arquitetura (inline vs. mirror) e como complementam firewalls e SIEMs.

- **Casos práticos e indicadores:**
  - Exemplos de alertas (ICMP ping, SQLi, ICMP flood).
  - Como interpretar logs básicos de Snort/Suricata (formatos e campos importantes).

- **Python — Manipulação de Arquivos aplicada a SOC:**
  - Abrir/ler/escrever arquivos com `open()` e `with`.
  - Modos de arquivo: `r`, `w`, `a`, `r+`, `x` e modos binários `rb`/`wb`.
  - Técnicas práticas: filtrar IPs, extrair emails com regex, contar ocorrências, dividir arquivos grandes.
  - Scripts criados: exemplo de leitura/escrita, filtrador de IPs, extrator por regex, contador de IPs/e-mails, gerador de blacklist CSV.

- **Exercícios laboratoriais:**
  - Montagem de topologias NAT e VPN (site-to-site) no Packet Tracer (com comandos CLI).
  - Laboratórios práticos para geração e análise de logs, simulação de tráfego suspeito e validação de regras.

---

## ⚙️ O que foi mais difícil
- **Aplicar configurações de NAT / VPN no Packet Tracer**: detalhes de interfaces, DCE/DTE em serial, rotas de retorno e interações com NAT (NAT-T).
- **Afinar regras de IDS/IPS**: escolher assinaturas corretas, evitar falsos positivos sem perder cobertura.
- **Regex robusta**: escrever padrões que capturem e-mails e IPs sem muitos falsos positivos (e validar 0–255 quando necessário).
- **Manipulação segura de arquivos grandes**: aprender a iterar linha-a-linha e evitar usar `read()` em arquivos gigantes.

---

## 📚 O que precisa reforçar
- **Prática com regex**: criar e testar padrões para e-mails, IPs, timestamps e URLs; usar flags (`IGNORECASE`, `MULTILINE`, `DOTALL`) e validar octetos de IPv4 quando necessário.
- **Tuning de IDS/IPS**: implementar cenários de teste para reduzir falsos positivos e testar modos de prevenção (drop/reject/rate-limit).
- **Integração de logs no SIEM**: pipeline básico (Suricata → Filebeat → Logstash → Elasticsearch/Kibana) e dashboards de análise.
- **Roteamento e NAT avançado**: praticar com GNS3/IOS real se Packet Tracer limitar recursos (NAT, IPSec, NAT-T).
- **Automação**: transformar scripts Python em ferramentas reutilizáveis (argumentos CLI, logging, testes unitários, output CSV/JSON).

---

## ✅ Próximos passos sugeridos
1. Fazer 2–3 labs práticos de IDS/IPS em VM (Suricata + Snort) e capturar alertas reais com tráfego controlado (nmap, curl, payloads simulados).  
2. Melhorar regex do extrator de e-mails para reduzir falsos positivos; adicionar validação adicional para IPs.  
3. Integrar um script que consome logs do IDS e atualiza automaticamente uma blacklist (CSV → regras simuladas/iptables).  
4. Repetir labs de NAT/VPN usando GNS3 ou equipamento real para consolidar comandos Cisco IOS.  
5. Documentar cada laboratório com prints, comandos usados e aprendizado — transformar em material para portfolio.

---

## Notas finais
Semana produtiva: misturou teoria e prática com foco em aplicar conceitos diretamente ao fluxo de trabalho de um analista SOC. O progresso está em consolidar padrões (regex, tuning de regras) e ganhar confiança ao montar e testar topologias/infraestruturas reais ou emuladas.

