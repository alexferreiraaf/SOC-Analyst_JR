# O que o SOC faz em cada fase do NIST 800-61 durante um Brute Force

## Preparação
O SOC mantém scripts, regras e playbooks prontos para detectar falhas de login, além de políticas de bloqueio e hardening do SSH.

## Identificação
Analisa logs e alertas para confirmar múltiplas tentativas de login falhas do mesmo IP, validando se é um ataque real.

## Contenção
Bloqueia imediatamente o IP atacante no firewall ou via ferramenta automática para impedir novas tentativas.

## Erradicação
Corrige a causa raiz, ajustando configurações de SSH, removendo acessos desnecessários e reforçando controles de autenticação.

## Recuperação
Garante que o serviço esteja estável, monitora o ambiente e confirma que o ataque não continua.

## Lições Aprendidas
Documenta o incidente e melhora regras, scripts e processos para evitar recorrência.
