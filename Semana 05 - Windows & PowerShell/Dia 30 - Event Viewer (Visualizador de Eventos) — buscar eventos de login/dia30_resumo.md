# 🧠 Dia 30 — Event Viewer e Logs de Autenticação

## 📚 Teoria
- Event Viewer registra logs de sistema, aplicação e segurança.
- IDs 4624 (sucesso) e 4625 (falha) indicam logons.
- Campos importantes: Account Name, Source IP, Logon Type.

## ⚙️ Prática
- Filtro aplicado no log de segurança para IDs 4624 e 4625.
- Análise de eventos com IP de origem.
- Exportação de logs para `.evtx` e `.txt`.

## 💻 PowerShell
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624,4625} -MaxEvents 50 |
Select-Object TimeCreated, Id, Message |
Out-File eventos_login.txt

