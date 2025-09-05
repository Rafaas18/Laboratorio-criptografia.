#!/usr/bin/env python3
import sys
import re

# Colores para resaltar en consola
GREEN = "\033[92m"
RESET = "\033[0m"

def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            nuevo_char = chr((ord(char) - ord('a') - desplazamiento) % 26 + ord('a'))
            resultado += nuevo_char
        else:
            resultado += char
    return resultado

def cargar_diccionario():
    # Diccionario básico de palabras comunes en español
    return set([
        "la", "el", "de", "que", "y", "en", "a", "los", "se", "del", "las", "por", "un", "para", "con",
        "no", "una", "su", "al", "lo", "como", "más", "pero", "sus", "le", "ya", "o", "este", "sí", "porque",
        "esta", "entre", "cuando", "muy", "sin", "sobre", "también", "me", "hasta", "hay", "donde", "quien",
        "desde", "todo", "nos", "durante", "todos", "uno", "les", "ni", "contra", "otros", "ese", "eso",
        "ante", "ellos", "e", "esto", "mí", "antes", "algunos", "qué", "unos", "yo", "otro", "otras", "otra",
        "él", "tanto", "esa", "estos", "mucho", "quienes", "nada", "muchos", "cual", "poco", "ella", "estar",
        "estas", "algunas", "algo", "nosotros", "mi", "mis", "tú", "te", "ti", "tu", "tus", "ellas", "nosotras",
        "vosotros", "vosotras", "os", "mío", "mía", "míos", "mías", "tuyo", "tuya", "tuyos", "tuyas"
    ])

if len(sys.argv) != 2:
    print("Uso: python3 readv2.py \"<texto interceptado>\"")
    sys.exit(1)

texto_cifrado = sys.argv[1]
diccionario = cargar_diccionario()
mejor_puntaje = -1
mejor_descifrado = ""
mejor_desplazamiento = 0
resultados = []

for desplazamiento in range(26):
    descifrado = descifrar_cesar(texto_cifrado, desplazamiento)
    palabras = re.findall(r'\b[a-z]+\b', descifrado)
    coincidencias = sum(1 for palabra in palabras if palabra in diccionario)
    resultados.append((desplazamiento, descifrado, coincidencias))
    if coincidencias > mejor_puntaje:
        mejor_puntaje = coincidencias
        mejor_descifrado = descifrado
        mejor_desplazamiento = desplazamiento

for desplazamiento, descifrado, coincidencias in resultados:
    if desplazamiento == mejor_desplazamiento and mejor_puntaje > 0:
        print(f"{GREEN}{desplazamiento}: {descifrado}{RESET}")
    else:
        print(f"{desplazamiento}: {descifrado}")