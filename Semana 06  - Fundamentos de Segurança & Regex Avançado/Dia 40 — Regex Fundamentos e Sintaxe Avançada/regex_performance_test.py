#!/usr/bin/env python3
# regex_performance_test.py
# Objetivo: comparar performance entre diferentes abordagens de regex em logs grandes

import re
import time

LOG_FILE = "auth_sample_large.log"  # gere um arquivo grande para o teste

# Regex para detectar falhas de login com IP
regex_str = r"Failed\s+login.*Source\s+Network\s+Address:\s+(\d{1,3}(?:\.\d{1,3}){3})"

def metodo_1_search_por_linha():
    """Recria regex a cada linha — menos eficiente"""
    with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            re.search(regex_str, line)

def metodo_2_regex_compilado():
    """Compila regex uma vez — mais eficiente"""
    pattern = re.compile(regex_str)
    with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            pattern.search(line)

def metodo_3_findall_bloco():
    """Lê todo arquivo e aplica findall de uma vez"""
    with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
        data = f.read()
    re.findall(regex_str, data)

def medir_tempo(func):
    inicio = time.perf_counter()
    func()
    fim = time.perf_counter()
    print(f"{func.__name__}: {fim - inicio:.3f} segundos")

if __name__ == "__main__":
    print("🏁 Iniciando teste de performance de Regex...\n")
    medir_tempo(metodo_1_search_por_linha)
    medir_tempo(metodo_2_regex_compilado)
    medir_tempo(metodo_3_findall_bloco)
