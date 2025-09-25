# Lab DNS + DHCP

## Objetivo
Configurar um roteador com DHCP e um servidor DNS no Packet Tracer, e validar que os PCs recebem IP automático e resolvem nomes de domínio.

## Passos
1. Criado pool DHCP no roteador:
   - Network: 192.168.20.0/24
   - Gateway: 192.168.20.1
   - DNS: 192.168.20.10
2. Configurado servidor DNS com entrada `site2.com -> 192.168.20.10`.
3. Configurados PCs para IP dinâmico (DHCP).

## Testes
- `ipconfig /renew`: PCs receberam IP válido.
- `ping site2.com`: nome resolvido e resposta positiva.

## Conclusão
Lab funcionando: DHCP automatizou a configuração de rede e DNS traduziu o nome de domínio corretamente.
