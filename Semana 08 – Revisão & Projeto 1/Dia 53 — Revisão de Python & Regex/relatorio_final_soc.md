# 🛡️ Relatório de Incidente: Análise de Tentativas SSH
**Data da Análise:** 20/11/2025 03:54

## 1. Resumo Executivo
Foram detectadas múltiplas tentativas de autenticação falha no servidor. A análise identificou os 3 principais vetores de ataque listados abaixo.

## 2. Top 3 Origens de Ataque
| Rank | Endereço IP | País de Origem | Tentativas | Status |
|---|---|---|---|---|
| #1 | **192.168.1.200** | Rede Interna (LAN) | 10 | 🔴 Crítico |
| #2 | **45.22.11.99** | N/A (Instale 'requests') | 3 | 🔴 Crítico |
| #3 | **200.10.5.1** | N/A (Instale 'requests') | 2 | 🔴 Crítico |

### Observação de Origem
ℹ️ **Ataque Distribuído:** Os ataques originaram-se de múltiplas regiões.

## 3. Evidências Técnicas e IoCs
### Alvo: 192.168.1.200 (Rede Interna (LAN))
- **Total de Falhas:** 10
- **Janela de Tempo:** Nov 20 08:18:15 até Nov 20 09:20:00
- **Usuários Alvo:** `admin, support, root`

### Alvo: 45.22.11.99 (N/A (Instale 'requests'))
- **Total de Falhas:** 3
- **Janela de Tempo:** Nov 20 08:30:45 até Nov 20 08:30:50
- **Usuários Alvo:** `root`

### Alvo: 200.10.5.1 (N/A (Instale 'requests'))
- **Total de Falhas:** 2
- **Janela de Tempo:** Nov 20 09:15:10 até Nov 20 09:15:12
- **Usuários Alvo:** `admin, root`

---
*Relatório gerado automaticamente pelo Python SOC Tool.*
