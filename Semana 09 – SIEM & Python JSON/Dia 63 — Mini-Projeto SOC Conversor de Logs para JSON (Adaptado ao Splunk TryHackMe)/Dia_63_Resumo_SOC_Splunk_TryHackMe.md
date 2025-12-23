
# Dia 63 — Mini-Projeto SOC: Conversor de Logs para JSON (Splunk TryHackMe)

## 🎯 Objetivo
- Converter logs brutos em JSON estruturado
- Gerar alertas SOC com Python
- Reingestar dados no Splunk THM
- Criar dashboards com logs próprios
- Simular pipeline ETL real de SOC

## 🔁 Fluxo SOC
LOG BRUTO → Python (ETL) → JSON → Alertas/Relatórios → Upload Splunk → Dashboards

## 🐍 Núcleo Python
- Leitura de logs linha a linha
- Parsing com regex (SSH failed)
- Normalização de campos (ip, usuario, evento, timestamp)
- Geração de JSON compatível com Splunk (_json)

## 🚨 Alertas Externos
- IPs com mais de 5 falhas
- Usuários mais atacados
- Saída: alertas.json

## 📊 Relatórios
- Total de eventos
- IPs suspeitos
- Usuário mais atacado
- Evento mais comum

## 📤 Splunk THM
- Upload manual de JSON
- Sourcetype: _json
- Index: main

## 🔎 Buscas SPL
- Falhas por IP
- Usuários mais atacados
- Validação do ETL

## 🏆 Entregáveis
- Código Python
- logs_convertidos.json
- alertas.json
- relatorio.json
- Dashboard SOC
