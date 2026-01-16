# Prática 2 — Analisando um Documento (Elastic / Kibana)

## Evento analisado (baseado no arquivo fornecido)

**Contexto do evento real:**
- `datasource`: email  
- `direction`: internal  
- `attachment`: forceupdate.ps1  
- `sender`: yani.zubair@tryhatme.com  
- `subject`: Force update fix  
- `timestamp`: Jan 17, 2026 @ 02:47:10.304  

Este evento foi selecionado por apresentar **maior relevância de segurança** dentro do conjunto analisado.

---

## 1. Observação do Documento

### JSON completo
Cada linha do dataset representa um **documento JSON completo do Elastic**, apenas exportado para CSV.  
O documento contém metadados, campos normalizados e contexto suficiente para investigação SOC.

### Campos extraídos
Os campos já estão **parseados automaticamente** pelo Elastic, permitindo análise direta sem necessidade de regex inicial.

---

## 2. Identificação dos Campos Solicitados

### `@timestamp`
- Campo equivalente no arquivo: `timestamp`
- Valor observado: `Jan 17, 2026 @ 02:47:10.304`

**Interpretação SOC:**  
Indica o momento exato do evento, essencial para correlação temporal.

---

### `source.ip`
- **Não presente neste evento**

**Interpretação SOC:**  
Não se trata de tráfego de rede, firewall ou proxy. O evento é contextual (email).

---

### `user.name`
- Campo `user.name` não existe explicitamente
- Campo equivalente funcional: `sender`

Exemplo:
```
sender: yani.zubair@tryhatme.com
```

**Interpretação SOC:**  
Identidade do usuário no contexto de email corporativo.

---

### `event.action`
- Não existe como campo explícito
- A ação é inferida pelo contexto do evento

**Interpretação SOC:**  
Envio de email interno com anexo PowerShell.

---

## 3. Pensando como SOC

### Isso é login?
❌ Não  
Não há evento de autenticação, sucesso ou falha de login.

---

### É erro?
❌ Não é erro técnico  
⚠️ É um evento sensível de segurança.

O envio interno de um script `.ps1` pode indicar:
- Administração legítima  
- Malware  
- Movimento lateral  
- Engenharia social interna  

---

### É tráfego normal?
❌ Não  
Não envolve IP de origem, destino, DNS ou firewall.

---

## Conclusão SOC

O evento analisado representa **envio interno de email com script PowerShell anexado**, caracterizando uma **atividade sensível de alto risco**.  
Não é login, não é erro técnico e não é tráfego normal. Esse tipo de evento exige validação imediata pelo SOC para descartar comprometimento interno ou atividade maliciosa.

---
