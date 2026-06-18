# `README.md`

````markdown
# Log Threat Intelligence Analyzer

## Descrição

Projeto desenvolvido para automatizar a análise de logs e enriquecer IPs utilizando a API do VirusTotal.

O script realiza a leitura de um arquivo de log, extrai automaticamente os endereços IP, consulta a reputação de cada um no VirusTotal e gera um relatório em formato CSV com a classificação de risco.

---

## Funcionalidades

- Extração automática de IPs de arquivos de log
- Remoção de IPs duplicados
- Validação de IPv4
- Integração com a API do VirusTotal
- Cálculo de detecções (`malicious + suspicious`)
- Classificação de risco:
  - BAIXO
  - MÉDIO
  - ALTO
- Geração automática de relatório CSV

---

## Estrutura do projeto

```

semana20_projeto/

├── main.py
├── utils.py
├── api_key.py
├── requirements.txt
├── logs_exemplo.log
├── relatorio_final.csv
├── README.md
└── .gitignore

```

---

## Instalação

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Configuração

No arquivo `api_key.py`:

```python
API_KEY = "SUA_API_KEY"
```

---

## Execução

```bash
python main.py
```

---

## Exemplo de saída

```

Consultando 185.223.89.44...

Detecções: 7 | Classificação: ALTO

```

Será gerado automaticamente:

```

relatorio_final.csv

```

---

## Tecnologias utilizadas

- Python 3
- requests
- csv
- ipaddress
- re
- VirusTotal API v3

---

## Objetivo

Projeto criado como parte dos estudos para atuação como Analista SOC Júnior, demonstrando integração com APIs externas, parsing de logs, enriquecimento de IOCs e geração automatizada de relatórios.
````
