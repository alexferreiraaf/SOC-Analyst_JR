# 🧠 Resumo — Dia 34: Monitoramento e Automação com PowerShell

## 📋 Conteúdo Estudado

Hoje aprendemos a criar **scripts PowerShell** para coletar informações do sistema, testar conectividade e automatizar relatórios diários.

### 🧩 Nível 1 — Fundamentos
- Obtenção de informações básicas:
  - Nome do computador (`$env:COMPUTERNAME`)
  - Usuário atual (`$env:USERNAME`)
  - Data e hora (`Get-Date`)
- Salvando informações em um arquivo de texto (`info.txt`).

### ⚙️ Nível 2 — Manipulação
- Listar os **10 processos que mais usam memória**.
- Identificar se o processo “opera” está aberto e exibir “Navegador aberto”.

### 🌐 Nível 3 — Automação
- Testar conectividade com `8.8.8.8`.
- Registrar o status de conexão (“Internet OK” ou “Sem conexão”) em `rede.log`.

### 📊 Nível 4 — Relatório Diário
- Criar script para gerar relatório com:
  - Nome do PC e usuário
  - Top 5 processos por uso de CPU
  - 5 serviços parados
- O relatório é salvo como `relatorio_diario_<data>.txt`.

### ⏰ Desafio Extra
- Agendar o script para rodar **todos os dias às 8h** via Agendador de Tarefas do Windows.

## 💡 Habilidades Desenvolvidas
- Automação de tarefas com PowerShell
- Manipulação de processos e serviços
- Criação de logs e relatórios automáticos
- Uso do Agendador de Tarefas do Windows

---
📅 **Data de conclusão:** {datetime.now().strftime("%d/%m/%Y %H:%M")}
