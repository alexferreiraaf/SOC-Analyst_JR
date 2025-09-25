# Lab HTTP & HTTPS

## Objetivo
Entender as diferenças práticas entre HTTP e HTTPS e validar acessos via CLI e Packet Tracer.

## Passos realizados
1. Testado cabeçalhos de sites reais:
   - `curl -I http://example.com`
   - `curl -I https://example.com`
2. Baixada página com `curl -o pagina.html`.
3. Criada topologia no Packet Tracer:
   - Servidor com HTTP/HTTPS ativados.
   - PC acessando via navegador interno.

## Evidências
- Prints dos cabeçalhos recebidos.
- Arquivo pagina.html salvo.
- Teste funcional de acesso HTTP/HTTPS no Packet Tracer.

## Conclusão
HTTP transmite dados em claro, enquanto HTTPS adiciona criptografia e autenticação. Testes confirmaram o funcionamento de ambos em CLI e ambiente simulado.
