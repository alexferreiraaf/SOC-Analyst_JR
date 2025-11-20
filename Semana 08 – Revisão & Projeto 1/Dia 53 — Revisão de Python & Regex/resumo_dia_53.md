# 📘 Resumo do Dia 53 --- Automação de Logs com Python & Regex

**📅 Data:** 20 de Novembro de 2025\
**🎯 Foco:** Análise de Logs, Expressões Regulares e Scripting para SOC\
**🔍 Objetivo:** Automatizar a extração de Indicadores de
Comprometimento (IoCs) e gerar inteligência a partir de arquivos de log
brutos (`auth.log`).

------------------------------------------------------------------------

## 1. 🔤 Fundamentos de Regex (Expressões Regulares)

Regex é a habilidade de definir padrões de busca em texto. Para um
analista de SOC, é a principal ferramenta para **entender e extrair
inteligência** de logs.

### Principais Funções do Módulo `re`

  -------------------------------------------------------------------------------------
  Função                        Descrição                 Uso no SOC
  ----------------------------- ------------------------- -----------------------------
  `re.findall(padrao, texto)`   Retorna todas as          Extrair todos os IPs que
                                ocorrências em uma lista. falharam login.

  `re.search(padrao, texto)`    Retorna apenas a primeira Verificar se um log contém
                                correspondência.          erro.

  `re.compile(padrao)`          Compila o padrão na       Otimiza performance ao
                                memória.                  analisar logs grandes.
  -------------------------------------------------------------------------------------

### ⭐ O Padrão de Ouro para SSH

Para capturar IPs em falhas de autenticação no Linux:

    r"Failed password.*from (\d{1,3}(?:\.\d{1,3}){3})"

**Quebra do padrão:**

-   **Failed password:** evento gatilho\
-   **.**\*: qualquer caractere entre o evento e o IP\
-   **from:** âncora antes do IP\
-   **(`\d{1,3}`{=tex}(?:.`\d{1,3}`{=tex}){3}):** estrutura completa de
    IPv4

------------------------------------------------------------------------

## 2. ⚙️ Fluxo de Análise Automatizada

Durante o laboratório, desenvolvemos um **pipeline lógico de análise**:

1.  **Leitura:** abertura eficiente do arquivo de log com `open()`.

2.  **Extração:** uso de Regex para capturar IP, usuário e data.

3.  **Estatística:** uso de `collections.Counter` para gerar métricas.

4.  **Filtragem:** aplicação de thresholds (ex: mais de 5 tentativas).

    ``` python
    if total > 5:
        print("Alerta")
    ```

5.  **Exportação:** resultados enviados para CSV, JSON ou Markdown.

------------------------------------------------------------------------

## 3. 🧰 Ferramentas Avançadas Integradas

A análise foi enriquecida com bibliotecas externas:

### 📊 Visualização

Uso de *Matplotlib* para gerar gráficos de barras com o volume de
ataques.

### 🌍 Geolocalização

Uso de *Requests* + API (`ip-api.com`) para identificar países de
origem.

### ⏱️ Monitoramento em Tempo Real

Leitura contínua dos logs (similar a `tail -f`) para alertas imediatos.

------------------------------------------------------------------------

## 4. 🧠 Mini Case SOC --- Reflexão Crítica

### 🔎 Cenário

Você detecta um ataque de **força bruta** e identifica os **Top 3
IPs**.\
Um deles é interno: `192.168.x.x`.

### ❓ Pergunta

**O que fazer quando o IP atacante é interno?**

### ✅ Procedimento do Analista

**1. Isolamento imediato**\
Colocar a máquina em **quarentena** (remover da rede).

**2. Investigação**\
- Infeção por malware/botnet?\
- Credenciais comprometidas?\
- Funcionário mal-intencionado (Insider Threat)?\
- Script mal configurado com senha incorreta?

**3. Varredura**\
Analisar os logs da máquina de origem para descobrir o vetor de
comprometimento.

------------------------------------------------------------------------

## 5. 🏁 Conclusão

Combinar **Python + Regex** permite:

-   Processar **gigabytes de logs em segundos**\
-   Extrair **IoCs automaticamente**\
-   Criar inteligência acionável\
-   Responder incidentes de forma **rápida e assertiva**
