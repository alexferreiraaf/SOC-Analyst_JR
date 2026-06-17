# classificador_avancado.sh

```bash
#!/bin/bash

# ==============================
# Classificador Inteligente
# DIA 132
# ==============================

# Dados simulados
ip="185.223.89.44"
usuario="root"
level=12
hora=2
tentativas=5

score=0
motivos=""

# ------------------------------
# Verificar IP externo
# ------------------------------

if [[ ! "$ip" =~ ^10\. ]] && \
   [[ ! "$ip" =~ ^192\.168\. ]] && \
   [[ ! "$ip" =~ ^172\.(1[6-9]|2[0-9]|3[0-1])\. ]]; then

    score=$((score+2))
    motivos+="\n- IP externo"

fi

# ------------------------------
# Usuário root
# ------------------------------

if [ "$usuario" = "root" ]; then

    score=$((score+2))
    motivos+="\n- Usuário root"

fi

# ------------------------------
# Horário incomum
# ------------------------------

if [ "$hora" -lt 8 ] || [ "$hora" -gt 18 ]; then

    score=$((score+1))
    motivos+="\n- Horário incomum"

fi

# ------------------------------
# Severidade
# ------------------------------

if [ "$level" -ge 10 ]; then

    score=$((score+3))
    motivos+="\n- Level crítico"

fi

# ------------------------------
# Múltiplas tentativas
# ------------------------------

if [ "$tentativas" -ge 3 ]; then

    score=$((score+2))
    motivos+="\n- Múltiplas tentativas"

fi

# ------------------------------
# Classificação Final
# ------------------------------

if [ "$score" -le 3 ]; then

    classificacao="BAIXO"

elif [ "$score" -le 6 ]; then

    classificacao="MÉDIO"

else

    classificacao="ALTO"

fi

echo "==============================="
echo " CLASSIFICADOR INTELIGENTE"
echo "==============================="
echo
echo "IP: $ip"
echo "Usuário: $usuario"
echo "Level: $level"
echo "Hora: ${hora}:00"
echo "Tentativas: $tentativas"
echo
echo "Score Total: $score"
echo "Risco Final: $classificacao"
echo
echo "Motivos:"
echo -e "$motivos"
```
