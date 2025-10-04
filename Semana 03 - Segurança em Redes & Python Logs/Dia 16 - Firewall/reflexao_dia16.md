# Reflexão — Dia 16 (Firewall)

Hoje aprendi como configurar e testar firewalls tanto no **Linux (UFW)** quanto no **Windows (Netsh)**.
Foi interessante ver como os comandos diferem, mas a lógica de regras é a mesma: **permitir o necessário e bloquear o inseguro**.

O UFW mostrou-se simples e direto, enquanto o Netsh é poderoso, mas menos intuitivo que a interface gráfica do Windows.

Um firewall sozinho, porém, não é suficiente. Ele não protege contra ataques internos, engenharia social ou malwares já presentes no sistema.
Por isso, deve ser usado em conjunto com **IDS/IPS, antivírus, monitoramento de logs e boas práticas de segurança**.

Essa prática reforçou a importância do firewall como **primeira linha de defesa**, mas também a necessidade de segurança em camadas.
