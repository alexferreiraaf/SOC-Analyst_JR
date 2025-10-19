# 🧠 Comando PowerShell — Processos com maior uso de CPU

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 3 Name, CPU
🖥️ Resultado
Nome do Processo	CPU (segundos)
System	22377,1875
dwm	12055,546875
MsMpEng	7579,9375

📄 Descrição:
O comando acima lista os 3 processos que mais consumiram CPU, ordenando pelo uso acumulado.
Isso é útil para identificar quais programas estão exigindo mais do processador no momento.