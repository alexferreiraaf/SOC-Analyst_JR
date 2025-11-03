# 🧠 Dia 42 — Mini-projeto Final: Detector de Brute Force com Regex + CSV

**🎯 Objetivo:**
Construir uma ferramenta prática para detectar ataques de brute force em logs de autenticação (ex.: `/var/log/auth.log`) usando regex, agregação por IP e geração de relatórios em CSV.

---

## ✅ O que foi feito / aprendido

**Entendimento teórico do brute force e sinais típicos em logs:**

* Múltiplas falhas de login do mesmo IP em curto intervalo.
* Tentativas contra usuários inválidos (`invalid user`).
* Padrões de horário e origem (datacenters, países estranhos).

**Criação de um script base em Python que:**

* Usa `re.compile(...)` para detectar linhas com `Failed password`.
* Conta tentativas por IP com `collections.Counter`.
* Gera um CSV ordenado (`relatorio_bruteforce.csv`) com IPs e número de tentativas.
* Emite alertas no console para IPs com tentativas acima de um limiar (ex.: `>5`).
* Explicação detalhada linha-a-linha do script: regex, leitura de arquivo linha a linha, contador, escrita CSV e lógica de alerta.

---

## 🧩 Exercícios e extensões propostos (implementáveis)

1. **Adicionar Data/Hora**

   * Atualizar regex para capturar timestamp e salvar CSV com colunas: `Data/Hora | Usuário | IP`.

2. **Ranking dos IPs**

   * Exibir no final do script o **Top 5** de IPs com mais tentativas.

3. **Visualização (opcional)**

   * Gerar um gráfico de barras (`matplotlib`) para IPs com mais de 3 tentativas e salvar como `grafico_tentativas.png`.

4. **Geração de alerta em arquivo**

   * Criar `alertas.txt` listando IPs suspeitos (`ALERTA: <ip> com <count> tentativas`).

5. **Enriquecimento de IPs (desafio)**

   * Usar APIs como `ipinfo.io` ou `abuseipdb.com` para adicionar localização, ASN e informação se é datacenter; salvar em CSV (`enriched_ips_ipinfo.csv`).

---

## 🛡️ Mitigações práticas contra brute force

* **Fail2Ban** para bloqueio automático por padrão.
* **Rate limiting** via `iptables` / firewall.
* **Autenticação por chave SSH** (desabilitar autenticação por senha).
* **Segmentação e monitoramento contínuo** (SIEM, alertas automáticos).

**Exemplos rápidos:**

```bash
sudo apt install fail2ban
```

```bash
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP
```

---

## 📁 Saídas / Entregáveis esperados

* `detector_bruteforce.py` — script completo (com as melhorias se aplicadas).
* `relatorio_bruteforce.csv` — lista de IPs e tentativas (ordenada).
* `alertas.txt` — IPs que ultrapassaram o limiar.
* `grafico_tentativas.png` *(opcional)*.
* `README_semana6.md` — resumo e instruções de uso.

---

## 📝 Observações finais

* Teste sempre em ambiente de laboratório com logs anonimizados.
* Ao integrar enriquecimento por API, proteja a chave usando variável de ambiente (`IPINFO_TOKEN`).
* Ajuste thresholds (ex.: `>5`) conforme a realidade do ambiente para reduzir falsos positivos.
