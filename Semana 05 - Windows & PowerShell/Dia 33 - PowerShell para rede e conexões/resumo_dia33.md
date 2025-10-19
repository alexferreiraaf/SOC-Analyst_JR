# 🧠 Resumo — Dia 33: PowerShell para Rede e Conexões

Hoje o foco foi aprender como usar o **PowerShell** para analisar e monitorar conexões de rede — uma habilidade essencial em **Segurança da Informação** e no trabalho de um **analista SOC**.

---

## 🔍 O que foi ensinado

- **Fundamentos de Rede:** Revisão de protocolos como TCP e UDP, e o significado de portas e estados de conexão (Listen, Established, TimeWait, etc.).

- **Teste de Conectividade:** Uso do comando `Test-Connection` para verificar se um host está acessível, simulando o comportamento do “ping”.

- **Listagem de Conexões Ativas:** Como visualizar conexões TCP abertas com `Get-NetTCPConnection` e filtrar por estado, porta ou endereço IP.

- **Filtragem por Portas:** Identificação de conexões em portas específicas (como 80, 443, 3389, 445), usadas por serviços comuns da rede.

- **Análise de Adaptadores de Rede:** Verificação de interfaces de rede com `Get-NetAdapter`, status de conexão e velocidade de link.

- **Processos Associados às Conexões:** Como descobrir qual programa está por trás de uma conexão de rede, relacionando PID (Process ID) com o nome do processo via `Get-Process`.

- **Geração de Relatórios:** Salvando resultados em arquivos `.md` ou `.txt` para auditorias e documentação, com uso de `Out-File`.

- **Simulação SOC:** Exercício prático de análise de conexões suspeitas em portas incomuns, simulando a investigação de um possível incidente de segurança.

- **Estados de Conexão:** Interpretação dos principais estados TCP e o que cada um pode indicar em uma investigação.

- **Relatório Final:** Criação de um resumo com número total de conexões, portas mais usadas, processos externos e IPs desconhecidos.

---

## 🚀 Conclusão

O **Dia 33** consolidou o uso do **PowerShell como ferramenta de análise de rede e investigação de incidentes**.  
Agora, é possível:
- Mapear conexões em tempo real,  
- Identificar comunicações suspeitas,  
- Associar processos aos IPs conectados,  
- E gerar relatórios para auditoria e segurança.

Esse aprendizado é essencial para quem busca a primeira vaga em **Cybersegurança**, especialmente em áreas como **Monitoramento SOC** e **Análise de Tráfego**.
