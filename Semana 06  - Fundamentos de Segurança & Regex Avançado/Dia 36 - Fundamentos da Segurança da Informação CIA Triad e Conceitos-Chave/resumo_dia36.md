# 🧭 **Resumo — Dia 36: Fundamentos da Segurança da Informação (CIA Triad)**

## 🎯 **Objetivo do Dia**
Entender os **três pilares da Segurança da Informação** — **Confidencialidade, Integridade e Disponibilidade (Tríade CIA)** — e como aplicá-los em práticas reais de defesa cibernética e no dia a dia de um **SOC (Security Operations Center)**.

---

## 🔐 **1. A Tríade CIA**

| Pilar | Significado | Como é garantido | Exemplo |
| --- | --- | --- | --- |
| **Confidencialidade** | Protege as informações contra acesso não autorizado. | Criptografia, autenticação multifator, controle de acesso. | Dados criptografados com AES ou acesso restrito via VPN. |
| **Integridade** | Garante que os dados não foram alterados. | Hashes (SHA256), logs assinados digitalmente, versionamento. | Comparar hashes para detectar corrupção de arquivos. |
| **Disponibilidade** | Garante que o sistema esteja acessível quando necessário. | Backups, redundância, mitigação DDoS. | Servidor com failover ou monitoramento via Zabbix. |

---

## 🧩 **2. Conceitos-Chave Complementares**

- **Autenticidade:** confirma se a origem da informação é legítima.  
- **Accountability (Responsabilidade):** todas as ações devem ser rastreáveis.  
- **Não-repúdio:** impede que alguém negue ter realizado uma ação (ex: e-mail assinado digitalmente).  

---

## ⚔️ **3. Ameaças, Vulnerabilidades e Riscos**

- **Ameaça:** algo que pode explorar uma falha (ex: hacker, malware).  
- **Vulnerabilidade:** fraqueza no sistema (ex: software desatualizado).  
- **Risco:** combinação entre ameaça, vulnerabilidade e impacto.  

📊 **Fórmula:**  
`Risco = Ameaça × Vulnerabilidade × Impacto`

---

## 🧠 **4. Aplicações Práticas em SOC**

| Pilar | Ação no SOC | Exemplo |
| --- | --- | --- |
| **Confidencialidade** | Monitorar logins e tentativas de acesso. | Evento 4625 do Windows. |
| **Integridade** | Detectar alteração em arquivos sensíveis. | Alerta de modificação de logs. |
| **Disponibilidade** | Monitorar uptime e resposta de servidores. | Ping e monitoramento no Zabbix. |

---

## 🧪 **5. Exercícios Práticos Realizados**

- **Hash de Integridade:** usar `sha256sum` para detectar alterações em arquivos.  
- **Criptografia de Dados:** proteger arquivos com `gpg -c`.  
- **Teste de Disponibilidade:** pingar e traçar rotas (`ping` e `tracert`).  
- **Mapa Mental:** estruturar os pilares e suas relações com ferramentas SOC.  

---

## 🧩 **6. Conclusão**

A **Tríade CIA** é o **alicerce da Segurança da Informação**.  
Toda política, ferramenta ou procedimento de segurança deve proteger pelo menos um desses pilares.  
Compreendê-los é essencial para atuar em **análise de incidentes, resposta e defesa SOC** de forma eficaz.

---

## 📘 **Dica Extra**

Quer revisar de forma interativa?  
👉 Acesse o material completo com vídeos, podcasts e cards de estudo no **NotebookLM:**  
🔗 [https://notebooklm.google.com/notebook/c243e2c3-ee32-4236-916b-23110bac56ae]
