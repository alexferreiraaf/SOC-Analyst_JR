# Resumo — DIA 131: Enriquecimento Básico de IOCs

## Objetivo

Aprender a enriquecer indicadores de comprometimento (IOCs), principalmente endereços IP, adicionando contexto que auxilie na tomada de decisão durante uma investigação de segurança.

---

# O que é um IOC?

IOC (Indicator of Compromise) é qualquer evidência que possa indicar uma atividade potencialmente maliciosa.

Exemplos:

- Endereço IP
- Domínio
- URL
- Hash de arquivo
- User-Agent
- Endereço de e-mail
- Nome de processo

Um IOC isolado não confirma um ataque, mas serve como ponto de partida para investigação.

---

# O que significa enriquecer um IOC?

Enriquecer um IOC é adicionar informações externas ao indicador para aumentar o contexto da análise.

No caso de um IP, é possível obter:

- País de origem;
- ASN (Autonomous System Number);
- Organização responsável;
- Tipo de provedor;
- Histórico de abuso;
- Reputação;
- Indicação de VPN, Proxy ou Datacenter.

Quanto mais contexto, maior a qualidade da decisão do analista.

---

# País de Origem

Conhecer o país pode ajudar na investigação, mas não deve ser utilizado como única evidência.

Um IP localizado em outro país não significa automaticamente atividade maliciosa.

É apenas mais um elemento para compor a análise.

---

# ASN (Autonomous System Number)

O ASN identifica a organização responsável pelo bloco de endereços IP.

Pode representar:

- ISP residencial;
- Empresa privada;
- Universidade;
- Cloud Provider;
- Empresa de hospedagem.

Conhecer o ASN ajuda a entender o perfil do endereço utilizado.

---

# Datacenter x Residencial

## IP de Datacenter

Características:

- Hospedado em provedores cloud ou VPS;
- Muito utilizado para automação;
- Comum em scanners e ataques massivos.

Não significa obrigatoriamente atividade maliciosa.

---

## IP Residencial

Características:

- Pertence a provedores de internet domésticos;
- Geralmente utilizado por usuários finais.

Mesmo assim, pode ser utilizado por máquinas comprometidas.

---

# Reputação

A reputação informa se o IOC já apareceu em atividades suspeitas anteriormente.

Ela pode indicar:

- Participação em ataques;
- Spam;
- Brute force;
- Botnets;
- Malware.

Entretanto:

- Boa reputação não garante segurança.
- Má reputação não confirma um ataque.

Ela deve apenas reforçar ou enfraquecer hipóteses existentes.

---

# Cruzamento com Logs

O enriquecimento deve sempre ser combinado com evidências internas.

Alguns pontos importantes:

- Quantidade de tentativas;
- Horário do evento;
- Usuário afetado;
- Login bem-sucedido após falhas;
- Uso de privilégios elevados;
- Persistência do atacante.

É a combinação dessas informações que permite construir uma conclusão sólida.

---

# Exemplo do laboratório

IOC:

185.223.89.44

Informações obtidas:

- País: Rússia;
- ASN: Hosting Provider;
- Tipo: Datacenter;
- Histórico: associado a scanning SSH.

Eventos correlacionados:

- Falhas de login;
- Login bem-sucedido;
- Acesso ao usuário root;
- Criação de novos usuários.

Nesse cenário, o enriquecimento aumenta significativamente a confiança de que houve um comprometimento.

---

# Boas práticas

- Nunca confiar apenas na reputação de um IOC.
- Sempre validar o contexto do ambiente.
- Correlacionar múltiplas evidências.
- Utilizar enriquecimento como apoio à investigação.
- Basear decisões em fatos observáveis.

---

# Principais aprendizados do Dia 131

- Entendimento do conceito de IOC.
- Capacidade de enriquecer um IP com informações adicionais.
- Compreensão do papel do ASN.
- Diferença entre IP residencial e IP de datacenter.
- Uso da reputação como apoio à análise.
- Integração entre enriquecimento externo e investigação baseada em logs.

---

# Conclusão

O enriquecimento de IOCs adiciona contexto valioso à investigação, mas não substitui a análise técnica do analista.

A tomada de decisão deve considerar simultaneamente:

- Evidências dos logs;
- Contexto operacional;
- Informações externas;
- Histórico do ambiente.

Essa abordagem reduz falsos positivos e melhora significativamente a qualidade da resposta a incidentes.