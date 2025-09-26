# Semana 2 — Mini-projeto Regex (Extrator de E-mails)

## 📌 Objetivo
Criar um script em Python que lê um arquivo de texto grande, identifica todos os e-mails usando **Regex** e salva os resultados em outro arquivo.

## 📂 Arquivos
- `emails_dataset.txt` → dataset de teste com e-mails e linhas comuns.
- `extrai_emails.py` → script para extração.
- `emails_encontrados.txt` → resultado da execução.
- `README_week2.md` → resumo do aprendizado.

## 🧠 Aprendizados
- Regex para capturar e-mails válidos.
- Uso do `re.findall()` em Python.
- Manipulação de arquivos (`open`, leitura, escrita).
- Eliminação de duplicados com `set()` e ordenação com `sorted()`.

## 🚧 Dificuldades
- Garantir que apenas e-mails válidos fossem capturados.
- Lidar com duplicados no dataset.

## 🔜 Próximos passos
- Expandir para extrair **telefones** e **URLs**.
- Integrar o extrator em um script maior de análise de logs.
