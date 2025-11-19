# Relatório Técnico: Análise de Logs e Automação no Linux (Dia 51)

**Data:** 19 de Novembro de 2025
**Responsável:** Alex Ferreira
**Contexto:** Revisão de estrutura de logs, comandos de filtragem e criação de scripts para detecção de incidentes (SOC).

---

## 1. Resumo Teórico: A Estrutura de Auditoria do Linux

Para um Analista de SOC, o sistema de arquivos `/var/log` é a "caixa preta" do servidor. Durante a revisão, focamos nos arquivos críticos para a segurança da informação:

| Arquivo de Log | Descrição Técnica | Relevância para o SOC |
| :--- | :--- | :--- |
| **`/var/log/auth.log`** | Registra eventos de autenticação (SSH, sudo, su). | **Crítica:** Fonte primária para detecção de ataques de força bruta e escalonamento de privilégios. |
| **`/var/log/syslog`** | Mensagens gerais do sistema e serviços (daemon). | **Alta:** Permite correlacionar falhas de serviço com eventos de segurança. |
| **`/var/log/nginx/access.log`** | Registros de acesso ao servidor web (quando aplicável). | **Alta:** Vital para investigar ataques na camada de aplicação (L7) como SQLi e XSS. |

**Ferramentas Essenciais Utilizadas:**
* **`grep`**: Filtragem primária (busca por strings como "Failed" ou "Accepted").
* **`awk`**: Extração cirúrgica de colunas de dados (isolamento de IPs e usuários).
* **`uniq -c`**: Análise estatística para detecção de anomalias de volume.
* **`journalctl`**: Interface moderna para leitura de logs do *systemd*.

---

## 2. Laboratório Prático: Execução e Análise

Nesta etapa, simulamos a rotina de investigação de incidentes utilizando a interface de linha de comando (CLI).

### 🧪 2.1 Identificação de Falhas de Login (SSH)
Executamos filtros para capturar tentativas de acesso com credenciais inválidas.

* **Comando Executado:**
    ```bash
    sudo grep "Failed password" /var/log/auth.log | tail -n 20
    ```
* **Análise Técnica:**
    O comando permite visualizar o *timestamp*, o usuário alvo (frequentemente `root` ou `admin`) e o IP de origem. A repetição de falhas em curtos intervalos de tempo é o principal indicador de comprometimento ou varredura ativa.

### 🧪 2.2 Estatística de Ataque (Top Talkers)
Isolamos os endereços IP para entender a magnitude do ataque volumétrico.

* **Comando Executado:**
    ```bash
    sudo grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr
    ```
* **Análise Técnica:**
    A ordenação decrescente revela os IPs mais agressivos. Em um cenário real, endereços com centenas de tentativas devem ser imediatamente cruzados com bases de Threat Intelligence (como VirusTotal) e bloqueados no Firewall.

### 🧪 2.3 Auditoria de Sucesso (Comprometimento?)
Verificamos se, em meio ao ruído dos ataques, houve algum acesso legítimo ou invasão bem-sucedida.

* **Comando Executado:**
    ```bash
    sudo grep "Accepted password" /var/log/auth.log | tail -n 10
    ```
* **Análise Técnica:**
    Logins bem-sucedidos vindos de IPs desconhecidos ou em horários atípicos (fora do expediente) representam um alerta vermelho de possível conta comprometida.

---

## 3. Automação e Scripting SOC

Para mitigar a fadiga de alertas e agilizar a resposta, foi desenvolvido o script `soc_analyser.sh`. A ferramenta automatiza a coleta de métricas e gera inteligência acionável.

**Funcionalidades Implementadas:**
1.  **Coleta Automática:** Detecção dinâmica do arquivo de log (`auth.log` ou `secure`).
2.  **Relatório CSV:** Geração de arquivo estruturado para auditoria externa.
3.  **Visualização:** Criação de gráfico de ataques por hora (via Gnuplot).
4.  **Enriquecimento:** Geolocalização de IPs atacantes.

**Exemplo de Saída do Relatório:**
```text
=== INICIANDO ANÁLISE SOC ===
Arquivo de Log alvo: /var/log/auth.log
[1/4] Processando arquivo de log...
Total de falhas encontradas: 452
[2/4] Gerando Relatório CSV e Verificando Alertas...
[ALERTA] IP 192.168.50.5 realizou 120 tentativas (Limite: 10)
[3/4] Gerando Gráfico de Ataques por Hora...
Gráfico gerado: grafico_ataques.png
[4/4] Analisando Origem Geográfica...
IP: 192.168.50.5 | Origem: CN (ESTRANGEIRO)

## 4. Conclusões do Dia 51

A revisão técnica confirmou a importância do domínio da CLI para a operação de defesa cibernética.

1. **Eficiência da CLI:** A combinação de `grep` + `awk` demonstrou ser superior em velocidade para diagnósticos imediatos quando comparada à extração e upload de logs para ferramentas gráficas externas.
2. **Padrões de Ataque:** Foi constatado que serviços expostos à internet (porta 22) sofrem tentativas de força bruta constantes e automatizadas. A monitoria passiva não é suficiente; é necessária a aplicação de bloqueios ativos (Fail2Ban ou regras de Firewall).
3. **Automação:** A criação do script `soc_analyser.sh` provou que é possível criar ferramentas de monitoramento robustas (com alertas e gráficos) utilizando apenas recursos nativos do sistema operacional, garantindo visibilidade mesmo em servidores com recursos limitados.