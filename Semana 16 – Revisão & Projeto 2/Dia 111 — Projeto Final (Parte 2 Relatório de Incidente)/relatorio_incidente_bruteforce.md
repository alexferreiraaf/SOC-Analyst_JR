# 📄 Relatório de Incidente de Segurança  
## Incidente: Tentativa de Brute Force via SSH

---

## 1. Identificação do Incidente

- **ID do Incidente:** INC-2026-001  
- **Data da Detecção:** 18/02/2026  
- **Horário da Detecção:** 10:19 (UTC-3)  
- **Analista Responsável:** [Seu Nome]  
- **Sistema Afetado:** Servidor Linux – Serviço SSH (porta 22)  
- **Ambiente:** Laboratório / Ambiente de Teste  

---

## 2. Resumo Executivo

Foi identificado um volume anômalo de tentativas de login via SSH originadas de um único endereço IP externo, caracterizando comportamento compatível com tentativa de ataque de força bruta (brute force). O número de falhas excedeu o limite configurado no script de monitoramento, gerando alerta automático. Não houve evidência de autenticação bem-sucedida. O incidente foi classificado como tentativa de acesso não autorizado sem comprometimento do sistema.

---

## 3. Linha do Tempo do Incidente

| Horário | Evento |
|----------|--------|
| 10:12 | Primeira tentativa de login falha registrada |
| 10:15 | Aumento progressivo de falhas para o mesmo IP |
| 10:18 | Limiar configurado no script excedido |
| 10:19 | Alerta automático gerado |
| 10:22 | Coleta de evidências concluída |
| 10:30 | Análise manual confirmada |

---

## 4. Evidências Técnicas

### 4.1 Trechos do Log do Sistema

```bash
Feb 18 10:12:01 servidor sshd[1234]: Failed password for invalid user admin from 192.168.1.50 port 54321 ssh2
Feb 18 10:13:45 servidor sshd[1238]: Failed password for invalid user root from 192.168.1.50 port 54345 ssh2
Feb 18 10:14:12 servidor sshd[1240]: Failed password for invalid user test from 192.168.1.50 port 54367 ssh2
```

### 4.2 Saída do Script de Detecção
```bash
[ALERTA] Possível ataque de brute force detectado!
IP suspeito: 192.168.1.50
Total de tentativas: 12
```

### 4.3 Arquivos Gerados
Estrutura de evidências coletadas:
```bash
evidencias/
 ├── alertas.txt
 ├── ips_suspeitos.csv
 └── resumo.json
 ```
Descrição dos arquivos:

- `alertas.txt` → Registro textual dos alertas disparados
- `ips_suspeitos.csv` → Lista estruturada de IPs com contagem de tentativas
- `resumo.json` → Dados consolidados da análise (formato estruturado)

## 5. Análise e Classificação
### 5.1 Tipo de Incidente
Tentativa de Brute Force (MITRE ATT&CK T1110)

### 5.2 Foi um incidente real ou tentativa?
Foi caracterizada uma tentativa de acesso não autorizado, sem evidências de comprometimento.

### 5.3 Houve sucesso na invasão?
Não.
Não foram identificados registros de login bem-sucedido provenientes do IP analisado.

### 5.4 Severidade
Média

Justificativa:
- Tentativa externa de acesso
- Volume significativo de tentativas
- Sem comprometimento confirmado
- Detectado e contido rapidamente

### 5.5 Impacto

Não houve impacto operacional.
O incidente não resultou em acesso indevido ou indisponibilidade de serviço.

### 5.6 Risco Residual

Moderado, caso não sejam aplicadas medidas preventivas adicionais.
O IP pode tentar novamente ou fazer parte de botnet automatizada.

## 6. Ações Tomadas
- Análise dos logs do sistema
- Confirmação de ausência de login bem-sucedido
- Registro do incidente
- Organização das evidências
- Monitoramento reforçado do serviço SSH

## 7. Recomendações
- Implementar Fail2ban para bloqueio automático de IPs após múltiplas falhas.
- Configurar rate limiting para conexões SSH.
- Desabilitar login via senha e utilizar autenticação por chave pública.
- Alterar a porta padrão do SSH (opcional).
- Manter monitoramento contínuo dos logs.
- Revisar política de senhas e usuários habilitados.

### 8. Conclusão
O evento analisado caracteriza uma tentativa automatizada de brute force contra o serviço SSH do servidor monitorado. A detecção foi eficaz e não houve comprometimento do ambiente. Recomenda-se implementação de controles adicionais para redução de risco futuro.
