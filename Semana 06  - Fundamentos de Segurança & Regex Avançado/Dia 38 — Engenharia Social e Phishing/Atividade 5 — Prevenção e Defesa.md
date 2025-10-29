# 🛡️ Atividade 5 — Prevenção e Defesa

## 🎯 Guia rápido de mitigação para equipe SOC

| **Categoria** | **Ação de Mitigação** | **Ferramenta / Exemplo** |
| --- | --- | --- |
| **Treinamento** | Simulações mensais de phishing e campanhas de conscientização | GoPhish |
| **Autenticação** | MFA obrigatório para todos os usuários e fornecedores | Microsoft Authenticator |
| **Segurança de e-mail** | Configuração e monitoramento de SPF, DKIM e DMARC | Admin do domínio / Postmaster Tools |
| **Monitoramento** | Coleta e correlação de eventos de segurança em tempo real | SIEM (ex: Splunk, ELK, QRadar) |
| **Resposta** | Alertar o SOC automaticamente via ticket ou webhook | Integração com SIEM / ServiceNow |
| **Gestão de acesso** | Revisões trimestrais de privilégios e remoção de acessos inativos | Active Directory / IAM |
| **Atualizações** | Aplicação de patches críticos semanalmente | WSUS / Ansible / Patch Manager |
| **Backups** | Cópias regulares e testes de restauração | Veeam / Acronis |
| **Análise de ameaças** | Inteligência de ameaças e indicadores IoC | MISP / VirusTotal / AlienVault OTX |

---

## 📘 Observações

- A **conscientização humana** continua sendo a principal linha de defesa contra phishing.  
- Ferramentas são eficazes **somente quando combinadas com processos claros e cultura de segurança**.  
- O SOC deve manter **planos de resposta e playbooks atualizados**, com testes periódicos.

