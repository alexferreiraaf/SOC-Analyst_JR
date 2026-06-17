# Relatório Final — Semana 19

## 1️⃣ Resumo da Semana

Durante a Semana 19 foram desenvolvidas atividades voltadas para a criação de mecanismos de automação e análise de incidentes em um ambiente de Security Operations Center (SOC).

Ao longo dos estudos, foram implementados scripts para classificação automática de alertas, análise contextual baseada em fatores de risco, enriquecimento manual de IOCs e validação crítica das decisões tomadas pela automação.

O principal objetivo foi compreender que ferramentas automatizadas auxiliam no processo de triagem, mas não substituem a análise humana em cenários complexos.

---

## 2️⃣ O que aprendi nos Labs

### Identificação de Brute Force

Aprendi a reconhecer padrões típicos de ataques de força bruta por meio da correlação de múltiplas falhas de autenticação em um curto período de tempo.

Principais indicadores:

- Grande quantidade de falhas consecutivas;
- Mesma origem (IP);
- Intervalo reduzido entre as tentativas;
- Possível sucesso após diversas falhas.

---

### Classificação de Severidade

Entendi que a severidade de um alerta não depende apenas do valor do campo `level`, mas também do contexto do incidente.

Foram considerados fatores como:

- Origem do acesso (IP interno ou externo);
- Tipo de usuário envolvido;
- Horário da atividade;
- Quantidade de eventos relacionados;
- Consequências após o evento.

---

### Enriquecimento de IOC

Aprendi a adicionar contexto a indicadores de comprometimento, analisando informações como:

- País de origem;
- ASN (Autonomous System Number);
- Tipo de provedor (Datacenter ou Residencial);
- Histórico de abuso;
- Reputação pública do endereço IP.

Esse processo aumenta significativamente a qualidade da análise e reduz conclusões precipitadas.

---

### Modelo de Pontuação (Scoring)

Foi desenvolvido um classificador baseado em pontuação acumulativa.

Cada característica adiciona pontos ao score final:

| Critério | Pontos |
|-----------|---------|
| IP externo | +2 |
| Usuário root | +2 |
| Horário incomum | +1 |
| Level ≥ 10 | +3 |
| Múltiplas tentativas | +2 |

Com base no total obtido:

| Score | Classificação |
|---------|--------------|
| 0–3 | BAIXO |
| 4–6 | MÉDIO |
| ≥7 | ALTO |

Além da classificação, o sistema informa os motivos que contribuíram para o resultado, tornando a decisão transparente e auditável.

---

## 3️⃣ Dificuldades Encontradas

Durante o desenvolvimento dos laboratórios, algumas dificuldades ficaram evidentes.

### Definição dos Pesos

Determinar quanto cada fator deveria influenciar no score final mostrou-se uma tarefa subjetiva e dependente do contexto operacional.

---

### Falsos Positivos

Nem toda atividade aparentemente suspeita representa um incidente real.

Exemplos:

- Administradores realizando manutenção;
- Usuários digitando senha incorretamente;
- VPN corporativa utilizando IP externo.

---

### Falta de Contexto

A automação simples não consegue identificar:

- Plantões autorizados;
- Mudanças planejadas;
- Atividades administrativas legítimas;
- Exceções operacionais.

---

### Correlação Temporal

Detectar eventos isoladamente é relativamente simples.

Já correlacionar sequências como:

```
failed_login
failed_login
success_login
add_user
sudo
```

exige lógica adicional e conhecimento do ambiente.

---

## 4️⃣ Onde a Automação Funcionou Bem

Os scripts desenvolvidos apresentaram bons resultados principalmente em tarefas repetitivas.

Entre os principais benefícios:

- Priorização inicial dos alertas;
- Redução do volume de análise manual;
- Padronização dos critérios de classificação;
- Rapidez na identificação de eventos críticos;
- Explicação objetiva dos fatores que elevaram o risco.

Esse tipo de automação pode reduzir significativamente o tempo de resposta inicial de um SOC.

---

## 5️⃣ Onde o Humano Ainda é Essencial

Apesar da utilidade dos scripts, diversas decisões continuam dependendo da análise humana.

O analista deve avaliar:

- Contexto organizacional;
- Perfil do usuário envolvido;
- Histórico da máquina;
- Atividades previamente autorizadas;
- Relação entre diferentes eventos;
- Possíveis falsos positivos.

A automação fornece uma recomendação, mas a decisão final continua sendo responsabilidade do analista.

---

## 6️⃣ Melhorias Futuras

O projeto pode evoluir significativamente com a implementação de novos recursos.

### Histórico de IP

Manter um banco local contendo a frequência com que determinado IP aparece nos incidentes.

---

### Persistência do Score

Armazenar classificações anteriores em arquivos CSV ou banco de dados para análise histórica.

---

### Ajuste Dinâmico dos Pesos

Permitir calibrar automaticamente os pesos conforme o ambiente ou métricas de desempenho.

---

### Integração com APIs de Reputação

Consultar serviços externos para obter informações adicionais sobre:

- Reputação;
- ASN;
- Geolocalização;
- Histórico de abuso;
- Classificação de ameaças.

---

### Dashboard

Criar uma interface simples exibindo:

- Quantidade de alertas;
- Classificação de risco;
- Top IPs ofensores;
- Estatísticas gerais.

---

### Correlação Temporal

Adicionar lógica para detectar automaticamente sequências como:

```
failed_login
→ success_login
→ sudo
→ add_user
```

classificando-as como potencial comprometimento.

---

## 7️⃣ Autoavaliação Técnica

| Competência | Nota (1–5) | Comentário |
|-------------|------------|------------|
| Análise de Logs | ⭐⭐⭐⭐☆ (4/5) | Boa capacidade de interpretar eventos e identificar padrões suspeitos. |
| Automação | ⭐⭐⭐⭐☆ (4/5) | Desenvolvimento de scripts funcionais para triagem e classificação. |
| Raciocínio Crítico | ⭐⭐⭐⭐☆ (4/5) | Melhor compreensão sobre contexto e limitações das regras automatizadas. |
| Segurança Defensiva | ⭐⭐⭐☆☆ (3/5) | Base sólida construída, mas ainda há espaço para aprofundar técnicas de investigação e resposta a incidentes. |

---

# Conclusão

A Semana 19 representou uma evolução significativa na construção da mentalidade de um Analista SOC.

Durante os laboratórios foi possível compreender que:

- Logs isolados possuem pouco valor sem contexto;
- A automação acelera a triagem inicial;
- Modelos de pontuação ajudam na priorização;
- O enriquecimento de IOCs aumenta a confiança das análises;
- Nenhum script substitui completamente o julgamento humano.

Ao final desta etapa, foi possível sair de uma abordagem baseada apenas na execução de comandos para uma visão mais estratégica, focada em análise contextual, priorização inteligente e tomada de decisão fundamentada em evidências técnicas.

Essa evolução representa um passo importante na transição de um perfil operacional para uma atuação mais próxima da esperada de um Analista SOC N2.