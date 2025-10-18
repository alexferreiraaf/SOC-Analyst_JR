# 🛡️ Políticas de Senha — `politicas_senha.md`

## 1. Enforce password history → 24
**Descrição:** impede que o usuário reutilize senhas antigas. O sistema guarda o histórico das últimas 24 senhas usadas.  
**Por que é importante:** evita que o usuário altere a senha e volte imediatamente para a antiga, reforçando a rotação real de credenciais e reduzindo o risco de senhas comprometidas serem reutilizadas.

---

## 2. Maximum password age → 60 dias
**Descrição:** define o tempo máximo que uma senha pode ser usada antes de exigir alteração.  
**Por que é importante:** garante que senhas sejam trocadas periodicamente, limitando o tempo em que uma credencial comprometida poderia ser explorada.

---

## 3. Minimum password length → 8 caracteres
**Descrição:** define o tamanho mínimo que uma senha deve ter.  
**Por que é importante:** senhas curtas são mais vulneráveis a ataques de força bruta. Exigir no mínimo 8 caracteres aumenta consideravelmente a complexidade e o tempo necessário para quebrá-la.

---

## 4. Password must meet complexity requirements → Enabled
**Descrição:** obriga que senhas incluam letras maiúsculas, minúsculas, números e caracteres especiais.  
**Por que é importante:** aumenta a entropia da senha, tornando muito mais difícil sua quebra por ataques de dicionário ou força bruta.

---

## 💡 Resumo
Essas políticas combinadas formam uma **camada essencial de defesa** na gestão de credenciais do Active Directory.  
Implementá-las ajuda a reduzir ataques de **credential stuffing**, **brute force** e **reutilização de senhas**, fortalecendo a segurança do ambiente corporativo.
