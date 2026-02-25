# Dia 114 — Instalação do Wazuh (Lab SOC)

## Ambiente Utilizado

- VM Ubuntu 22.04
- 4 vCPU
- 8 GB RAM
- 50 GB Disco
- Acesso sudo habilitado

---

## 1. Atualização do Sistema

sudo apt update && sudo apt upgrade -y

Objetivo:
Garantir que o sistema esteja atualizado antes da instalação.

---

## 2. Instalação de Dependências

sudo apt install curl unzip apt-transport-https -y

Objetivo:
Evitar falhas relacionadas a pacotes ausentes.

---

## 3. Download do Script Oficial

curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh

chmod +x wazuh-install.sh

---

## 4. Instalação All-in-One

sudo ./wazuh-install.sh -a

Observações:
- Instala Manager, Indexer e Dashboard na mesma máquina.
- Processo leva alguns minutos.
- Credenciais do dashboard são exibidas ao final da instalação.
- Não interromper o processo.

---

## 5. Validação dos Serviços

sudo systemctl status wazuh-manager
sudo systemctl status wazuh-dashboard
sudo systemctl status wazuh-indexer

Todos os serviços apresentaram status:
active (running)

---

## 6. Conclusão

O Wazuh foi instalado com sucesso.
Serviços estão ativos.
Ambiente pronto para análise de alertas e futura conexão de agentes.