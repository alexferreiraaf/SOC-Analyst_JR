# Lab SMTP e Simulação de E-mails

## Objetivo
Entender o funcionamento do SMTP e realizar uma simulação prática de envio de e-mails.

## Passos realizados
1. Testado acesso ao servidor SMTP real:
   - `telnet smtp.gmail.com 587`
   - Retornou banner ESMTP.
2. Criada topologia no Packet Tracer:
   - 1 servidor com serviço de e-mail ativado.
   - Contas: alice@lab.com e bob@lab.com.
   - PCs configurados para se comunicar com o servidor.
3. Alice enviou e-mail para Bob.
4. Bob conseguiu visualizar a mensagem recebida.

## Evidências
- Print do banner SMTP com telnet.
- Prints do envio e recebimento no Packet Tracer.

## Conclusão
Foi possível observar a porta e o banner do SMTP em uso real e simular o fluxo básico de envio/recebimento em laboratório.
