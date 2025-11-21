# Dia 56 — Documentação & Publicação no GitHub (SOC Analyst)

## 🎯 Objetivo do Dia
Aprender a documentar projetos de segurança cibernética de forma profissional e publicá-los, criando um portfólio técnico atraente para recrutadores.

---

## 📘 1. A Importância da Documentação
"Código sem documentação é mistério."
Para um Analista SOC, documentar é essencial para:
1.  **Registrar Incidentes:** Explicar o que aconteceu.
2.  **Criar Playbooks:** Ensinar como resolver problemas.
3.  **Portfólio:** Mostrar aos recrutadores que você sabe comunicar ideias técnicas.

---

## 📝 2. Estrutura de Diretórios Recomendada
Antes de subir para o GitHub, organize a pasta do projeto assim:

```text
projeto-soc-logs/
│
├── analisador_logs.py      # O script principal (Python)
├── auth_sample.log         # Log de exemplo para testes
├── relatorio.csv           # Exemplo de saída (gerado pelo script)
├── alertas.txt             # Exemplo de alertas (gerado pelo script)
├── requirements.txt        # Dependências (ex: requests, rich)
├── LICENSE                 # Licença de uso (MIT)
├── README.md               # A documentação principal
└── assets/                 # Pasta para imagens/prints
    ├── print_terminal.png
    └── print_csv.png
```

# 🛡️ SOC Log Analyzer
## 📖 Descrição
Este é um projeto de automação de segurança desenvolvido para analisar logs de autenticação (Linux/Windows). O script identifica padrões de ataques de força bruta, gera relatórios CSV e emite alertas automáticos.
---
## 🚀 Funcionalidades
Leitura de Logs: Suporte a arquivos .log e texto puro.

- **Detecção de Ameaças:** Identifica falhas de login repetitivas via Regex.

- **Relatórios:** Gera um arquivo relatorio.csv com estatísticas.

- **Alertas:** Cria um arquivo alertas.txt para IPs com comportamento suspeito.

###🛠️ Tecnologias Utilizadas
Python 3

Expressões Regulares (Regex)

Manipulação de Arquivos e I/O

##⚙️ Como Executar
Clone o repositório:

git clone [https://github.com/SEU-USUARIO/soc-log-analyzer.git](https://github.com/SEU-USUARIO/soc-log-analyzer.git)
cd soc-log-analyzer

Execute o script:
python3 analisador_logs.py auth_sample.log
Verifique os resultados:

Abra o arquivo relatorio.csv gerado.

Verifique se houve alertas em alertas.txt.

📊 Exemplo de Saída (Terminal)
Plaintext

[INFO] Iniciando análise de logs...
[ALERTA] IP 192.168.1.50 detectado com 15 falhas de login!
[SUCESSO] Relatório gerado: relatorio.csv
⚖️ Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.

💻 4. Guia Rápido de Git (Comandos)
Passo 1: Inicializar e Configurar
Bash

# Inicia o repositório na pasta
git init

# Evita subir arquivos desnecessários
echo "__pycache__/" > .gitignore
echo "*.tmp" >> .gitignore
Passo 2: Salvar as alterações (Commit)
Bash

# Adiciona todos os arquivos
git add .

# Cria o ponto de salvamento (snapshot)
git commit -m "Primeira versão: Analisador de Logs SOC"
Passo 3: Enviar para o GitHub (Push)
Bash

# Renomeia a branch principal para 'main' (boa prática)
git branch -M main

# Conecta com o repositório remoto (pegue o link no site do GitHub)
git remote add origin [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)

# Envia os arquivos
git push -u origin main
✅ Checklist de Entrega
[ ] Script analisador_logs.py funcionando e sem erros.

[ ] Arquivo README.md escrito e formatado.

[ ] Pasta assets/ com prints provando que funciona.

[ ] Licença LICENSE (MIT) adicionada.

[ ] Código subido no GitHub (Repositório Público).

[ ] Link do projeto postado no LinkedIn.