# testar_conectividade.ps1
# Script para testar conectividade com hosts e salvar resultados em .md

Write-Host "Iniciando testes de conectividade..."

# Define o arquivo de saída
$arquivo = "testar_conectividade.md"

# Cabeçalho do arquivo Markdown
"## 🌐 Teste de Conectividade" | Out-File $arquivo
"_" | Out-File $arquivo -Append
" " | Out-File $arquivo -Append
"**Data e Hora:** $(Get-Date)" | Out-File $arquivo -Append
" " | Out-File $arquivo -Append

# Teste 1 - Microsoft
Write-Host "Testando www.microsoft.com..."
"### Teste: www.microsoft.com" | Out-File $arquivo -Append
Test-Connection -ComputerName www.microsoft.com -Count 3 | Out-String | Out-File $arquivo -Append
" " | Out-File $arquivo -Append

# Teste 2 - GitHub
Write-Host "Testando www.github.com..."
"### Teste: www.github.com" | Out-File $arquivo -Append
Test-Connection -ComputerName www.github.com -Count 3 | Out-String | Out-File $arquivo -Append
" " | Out-File $arquivo -Append

# Teste 3 - Google DNS
Write-Host "Testando 8.8.8.8..."
"### Teste: 8.8.8.8 (Google DNS)" | Out-File $arquivo -Append
Test-Connection -ComputerName 8.8.8.8 -Count 4 | Out-String | Out-File $arquivo -Append
" " | Out-File $arquivo -Append

Write-Host "✅ Testes concluídos. Resultados salvos em $arquivo"
