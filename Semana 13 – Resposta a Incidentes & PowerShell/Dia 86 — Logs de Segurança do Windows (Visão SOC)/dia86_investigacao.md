## 📄 dia86_investigacao.md

### 🔍 Análise de Incidente — Exemplo Prático

**Cenário:**
Foram identificadas múltiplas falhas de logon (Event ID 4625) seguidas de um logon bem-sucedido (4624) para o mesmo usuário fora do horário comercial.

**Análise:**

* Possível ataque de força bruta
* Origem do IP deve ser analisada
* Verificar se houve criação de processos suspeitos (4688)
* Avaliar se privilégios elevados foram atribuídos (4672)

**Conclusão:**
Incidente classificado como **tentativa de acesso não autorizado**, exigindo reset de senha e monitoramento contínuo da conta.

---