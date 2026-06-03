### 🧠 Mini-Simulação Mental
## Cenário
Empresa funciona das 08:00 às 18:00.
Às 02:00 da manhã ocorre um login SSH bem-sucedido.
### 1. É automaticamente um incidente?
Não.
Inicialmente é apenas um alerta.
---
### 2. Pode ser manutenção?
Sim.
Pode existir:
- plantão
- suporte remoto
 - atualização emergencial
---
### 3. O que investigar?
- Usuário utilizado
- Endereço IP
- Histórico de acessos
- Chamados de manutenção
- Atividades executadas após o login
---
### 4. Escalaria imediatamente?
Depende do contexto.
Se não houver justificativa operacional conhecida, sim, o evento merece escalonamento para análise mais profunda.
---
### 5. Quais evidências coletar?
- Logs SSH
- Usuário autenticado
- IP de origem
- Comandos executados
- Horário exato
- Alertas relacionados