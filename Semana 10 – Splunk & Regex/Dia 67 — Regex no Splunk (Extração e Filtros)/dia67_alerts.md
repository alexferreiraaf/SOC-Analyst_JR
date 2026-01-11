# Dia 67 — Alertas no Splunk (SOC)

## O que é um alerta SOC
Um alerta é uma condição automatizada que dispara quando um padrão suspeito é detectado nos logs.

## Objetivo dos alertas criados
- Detectar ataques de brute force em SSH
- Reduzir falsos positivos
- Priorizar eventos realmente suspeitos

## Tipos de alertas usados
- Scheduled Alerts (padrão SOC N1)
- Janela curta de tempo (5 minutos)

## Severidade aplicada
- Medium: falhas repetidas
- High: brute force confirmado
- Critical: acesso comprometido (não aplicado neste dia)

## Benefícios
- Resposta rápida
- Menos ruído
- Alertas acionáveis
