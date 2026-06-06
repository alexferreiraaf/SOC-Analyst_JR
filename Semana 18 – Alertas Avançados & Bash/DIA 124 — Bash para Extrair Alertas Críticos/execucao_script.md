# Execução do Script

## Permissão de execução

```bash
chmod +x extrair_criticos.sh
```

## Execução

```bash
./extrair_criticos.sh
```

## Exemplo de saída

```

=====================================
Extraindo alertas críticos do Wazuh
=====================================

Total de alertas críticos encontrados: 27

Arquivo gerado:
criticos_2026-06-06_14-30.json

Top 5 IPs ofensores:

18 185.220.100.10
11 45.227.10.55
7 203.0.113.25
5 192.168.1.15
4 10.0.0.20

Processo concluído.

```

## Benefícios para o SOC

- Redução do tempo de triagem;
- Priorização automática dos eventos mais relevantes;
- Identificação rápida de IPs reincidentes;
- Base para futuras automações e integrações com Python ou SOAR.