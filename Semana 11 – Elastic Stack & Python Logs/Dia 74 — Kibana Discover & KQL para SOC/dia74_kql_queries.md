# Dia 74 — Consultas KQL (SOC)

## Login falho
event.action:"login_failed"

## IP suspeito
source.ip:"192.168.1.50"

## Brute force em conta admin
event.action:"login_failed" and user.name:"admin"

## Exclusão de ruído interno
event.action:"login_failed" and not source.ip:"192.168.0.*"

## Login fora do horário comercial
event.action:"login_failed" and not @timestamp:[now-8h TO now-18h]
