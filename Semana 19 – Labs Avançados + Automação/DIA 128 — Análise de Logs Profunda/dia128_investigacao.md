# Investigação – DIA 128

## Tipo de Evento

Brute Force SSH com possível comprometimento de credenciais.

---

## Evidências Encontradas

- **Total de tentativas de login falhas:** 45
- **IP de origem:** 185.44.23.11
- **Usuário alvo:** admin
- **Horário dos eventos:** 02:11
- **Login bem-sucedido após as falhas:** Sim
- **Persistência detectada:** Sim (execução de comandos com sudo e acesso ao arquivo `/etc/passwd`)

---

## Análise de Risco

**Classificação:** Alto

### Justificativa

O cenário apresenta diversas tentativas consecutivas de autenticação mal-sucedida seguidas por um login válido utilizando uma conta administrativa. Após o acesso, foram observadas ações privilegiadas, indicando potencial comprometimento do sistema.

Além disso:

- O IP de origem é externo.
- O horário da atividade é incomum.
- Houve uso de privilégios elevados após o login.

Esses fatores aumentam significativamente o risco do incidente.

---

## Checklist de Investigação

- [x] Quantidade de tentativas identificada
- [x] IP de origem analisado
- [x] Usuário envolvido identificado
- [x] Verificação de login bem-sucedido
- [x] Busca por persistência
- [x] Verificação de privilégios elevados
- [x] Avaliação do horário do evento
- [x] Classificação do risco

---

## Decisão Final

**Incidente confirmado.**

### Ações recomendadas

- Bloquear imediatamente o IP ofensivo no firewall.
- Resetar a senha do usuário comprometido.
- Revisar logs adicionais do servidor.
- Verificar outros ativos para identificar movimentação lateral.
- Escalar o caso para o nível superior (SOC N2 ou Blue Team).
- Manter monitoramento contínuo do ambiente.

---

## Conclusão

As evidências coletadas indicam uma forte possibilidade de comprometimento da conta administrativa após um ataque de força bruta bem-sucedido, justificando tratamento como incidente de segurança de alta prioridade.