# Tabela de Severidade para Eventos de Autenticação SSH

| Evento | Severidade | Justificativa |
|----------|------------|---------------|
| Login realizado com sucesso | 0 | Evento esperado e informativo |
| 1 falha de login | 3 | Provável erro de digitação do usuário |
| 2 falhas consecutivas | 4 | Pequena atividade suspeita, porém comum |
| 5 falhas de login internas | 7 | Pode indicar erro do usuário ou script interno |
| 5 falhas de login externas | 10 | Possível tentativa de brute force |
| Login fora do horário comercial | 8 | Atividade incomum que requer validação |
| 5 falhas + login bem-sucedido | 15 | Forte indício de comprometimento |
| Múltiplos IPs atacando o mesmo usuário | 12 | Possível ataque distribuído |
| Ataque contínuo contra usuário root | 15 | Alto risco para o ambiente |