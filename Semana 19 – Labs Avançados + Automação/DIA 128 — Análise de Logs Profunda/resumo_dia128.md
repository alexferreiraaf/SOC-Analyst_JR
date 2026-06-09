# Resumo — Dia 128: Análise de Logs Profunda

## Objetivo

Aprender a investigar eventos de segurança utilizando diferentes fontes de logs e transformar dados em evidências para tomada de decisão.

## Principais conceitos

- Leitura de logs de autenticação (`/var/log/auth.log`).
- Identificação de tentativas de login falhas e bem-sucedidas.
- Análise de IPs, usuários e horários dos eventos.
- Verificação de possíveis ações pós-comprometimento, como uso de `sudo`.
- Correlação entre múltiplas evidências para confirmar ou descartar um incidente.

## Fluxo básico de investigação

1. Identificar o alerta inicial.
2. Extrair evidências dos logs.
3. Confirmar se houve sucesso após as tentativas.
4. Procurar sinais de persistência ou escalonamento de privilégios.
5. Classificar o risco.
6. Decidir entre encerrar, monitorar ou escalar o caso.

## Aprendizado principal

No SOC, o objetivo não é apenas identificar um alerta, mas entender toda a história do ataque por meio das evidências disponíveis e tomar uma decisão fundamentada.