# Resumo — Dia 16 (Firewall)

## Definição
- **Packet filter** → filtra pacotes por portas, IPs e protocolos.
- **Stateful firewall** → analisa conexões ativas, decide com base no contexto.
- **Application layer firewall** → inspeciona tráfego em nível de aplicação (HTTP, SMTP etc.).

## Tipos
- **Firewall de rede** → protege toda a rede (ex.: roteador, appliance dedicado).
- **Firewall de host** → protege apenas a máquina em que está instalado.

## Exemplos
- **Linux**: iptables, UFW
- **Windows**: Windows Defender Firewall, Netsh
- **Open Source**: pfSense, OPNsense

## Casos de uso
- **Empresas**: bloquear portas inseguras, liberar VPN.
- **Residências**: restringir tráfego externo e proteger dispositivos IoT.
- **Servidores Web**: liberar apenas portas 80/443.
- **Cloud**: regras de segurança em VPC (AWS, Azure, GCP).

## Vantagens
- Controle de tráfego simples.
- Primeira barreira contra acessos não autorizados.
- Flexibilidade para liberar/bloquear serviços.

## Limitações
- Não protege contra ataques internos.
- Não analisa tráfego criptografado (sem inspeção SSL).
- Regras mal configuradas podem bloquear tráfego legítimo.

