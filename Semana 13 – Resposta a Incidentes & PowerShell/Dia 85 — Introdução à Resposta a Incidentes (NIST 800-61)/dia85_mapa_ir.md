# 🛡️ Mapa Mental — Resposta a Incidentes (NIST 800-61)
## Cenário: Brute Force em SSH

Brute Force SSH
├── 🟢 Preparação
│   ├── Scripts de detecção prontos
│   ├── Política de bloqueio definida
│   ├── Hardening SSH aplicado
│   └── Playbook SOC documentado
│
├── 🟡 Identificação
│   ├── Análise de logs (/var/log/auth.log)
│   ├── Alertas de falhas repetidas de login
│   ├── Confirmação de IP externo
│   └── Validação de usuário privilegiado
│
├── 🟠 Contenção
│   ├── Bloqueio temporário do IP atacante
│   ├── Aplicação de regra no firewall
│   ├── Fail2ban ativado
│   └── Redução imediata do risco
│
├── 🔴 Erradicação
│   ├── Ajuste de políticas SSH
│   ├── Desabilitar login por senha
│   ├── Remover acessos desnecessários
│   └── Correção da causa raiz
│
├── 🔵 Recuperação
│   ├── Validação dos serviços
│   ├── Monitoramento reforçado
│   ├── Confirmação de estabilidade
│   └── Operação normal restabelecida
│
└── 🟣 Lições Aprendidas
    ├── Atualização do relatório final
    ├── Ajuste do threshold de detecção
    ├── Melhoria do script SOC
    └── Atualização do playbook
