"""
Ejercicios de Algoritmos Clásicos
Temas: FizzBuzz, anagramas, Fibonacci, números primos, invertir strings, etc.
"""

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1: Invertir un string
# Escribe una función que reciba un string y devuelva el string invertido
# Ejemplo: "python" -> "nohtyp"

def invertir_string(texto):
    pass  # Tu código aquí (puedes usar slicing [::-1])

print(invertir_string("python"))  # "nohtyp"


# Ejercicio 2: Contar vocales
# Escribe una función que cuente cuántas vocales (a, e, i, o, u) tiene un string

def contar_vocales(texto):
    pass  # Tu código aquí

print(contar_vocales("Hola mundo"))  # 4


# Ejercicio 3: Número par o impar
# Pide un número al usuario y determina si es par o impar

def es_par(numero):
    pass  # Tu código aquí (True si es par, False si es impar)

print(es_par(7))  # False
print(es_par(10)) # True


# Ejercicio 4: Factorial de un número
# Calcula el factorial de un número entero positivo (n!) de forma iterativa
# Ejemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    pass  # Tu código aquí

print(factorial(5))  # 120


# Ejercicio 5: Suma de dígitos
# Suma todos los dígitos de un número entero positivo
# Ejemplo: 1234 -> 1 + 2 + 3 + 4 = 10

def suma_digitos(numero):
    pass  # Tu código aquí

print(suma_digitos(1234))  # 10


# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 6: FizzBuzz
# Imprime los números del 1 al 100. Para múltiplos de 3 imprime "Fizz",
# para múltiplos de 5 imprime "Buzz", para múltiplos de ambos imprime "FizzBuzz"

def fizzbuzz():
    pass  # Tu código aquí (usa un bucle del 1 al 100)

fizzbuzz()


# Ejercicio 7: ¿Es palíndromo?
# Determina si una palabra o frase es palíndroma (se lee igual al derecho y al revés)
# Ignora espacios, mayúsculas y signos de puntuación

def es_palindromo(texto):
    pass  # Tu código aquí

print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("python"))             # False


# Ejercicio 8: Fibonacci
# Genera los primeros n números de la secuencia de Fibonacci
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(n):
    pass  # Tu código aquí (devuelve una lista con los n primeros)

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Ejercicio 9: ¿Es primo?
# Determina si un número es primo (divisible solo por 1 y por sí mismo)

def es_primo(numero):
    pass  # Tu código aquí (True si es primo, False si no)

print(es_primo(7))   # True
print(es_primo(10))  # False


# Ejercicio 10: Anagramas
# Determina si dos palabras son anagramas (tienen las mismas letras en diferente orden)
# Ejemplo: "listen" y "silent"

def son_anagramas(palabra1, palabra2):
    pass  # Tu código aquí

print(son_anagramas("listen", "silent"))   # True
print(son_anagramas("python", "java"))     # False


# Ejercicio 11: Números perfectos
# Un número perfecto es aquel que es igual a la suma de sus divisores propios
# (excluyendo él mismo). Ejemplo: 6 = 1 + 2 + 3

def es_numero_perfecto(n):
    pass  # Tu código aquí

print(es_numero_perfecto(6))   # True
print(es_numero_perfecto(28))  # True
print(es_numero_perfecto(10))  # False


# Ejercicio 12: Contar palabras en una frase
# Cuenta cuántas veces aparece cada palabra en una frase
# Devuelve un diccionario con {palabra: frecuencia}

def contar_palabras(frase):
    pass  # Tu código aquí

frase = "el gato y el perro juegan con el gato"
print(contar_palabras(frase))
# {"el": 3, "gato": 2, "y": 1, "perro": 1, "juegan": 1, "con": 1}


# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 13: Torre de Hanoi
# Implementa el algoritmo recursivo de la Torre de Hanoi
# Mueve n discos del poste origen al poste destino usando un poste auxiliar

def torre_hanoi(n, origen, destino, auxiliar):
    pass  # Tu código aquí

torre_hanoi(3, "A", "C", "B")
# Salida esperada:
# Mover disco 1 de A a C
# Mover disco 2 de A a B
# Mover disco 1 de C a B
# Mover disco 3 de A a C
# Mover disco 1 de B a A
# Mover disco 2 de B a C
# Mover disco 1 de A a C


# Ejercicio 14: Ordenamiento burbuja (Bubble Sort)
# Implementa el algoritmo de ordenamiento burbuja para ordenar una lista
# de números de menor a mayor

def bubble_sort(lista):
    pass  # Tu código aquí

numeros = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numeros))  # [11, 12, 22, 25, 34, 64, 90]


# Ejercicio 15: Búsqueda binaria
# Implementa búsqueda binaria para encontrar un elemento en una lista ordenada
# Devuelve el índice del elemento o -1 si no existe

def busqueda_binaria(lista, objetivo):
    pass  # Tu código aquí

numeros = [1, 3, 5, 7, 9, 11, 13, 15]
print(busqueda_binaria(numeros, 7))   # 3
print(busqueda_binaria(numeros, 2))   # -1


# Ejercicio 16: Máximo común divisor (MCD)
# Implementa el algoritmo de Euclides para calcular el MCD de dos números

def mcd(a, b):
    pass  # Tu código aquí

print(mcd(48, 18))  # 6
print(mcd(56, 98))  # 14


# Ejercicio 17: Mínimo común múltiplo (MCM)
# Calcula el MCM de dos números usando la relación: MCM = a * b / MCD(a, b)

def mcm(a, b):
    pass  # Tu código aquí (puedes usar la función mcd del ejercicio anterior)

print(mcm(12, 18))  # 36


# Ejercicio 18: Comprobar si un número es feliz
# Un número feliz: suma de cuadrados de sus dígitos repetidamente hasta llegar a 1
# Si entra en un ciclo infinito (llega a 4), no es feliz
# Ejemplo: 19 -> 1²+9²=82 -> 64+4=68 -> 36+64=100 -> 1+0+0=1 (feliz)

def es_feliz(n):
    pass  # Tu código aquí

print(es_feliz(19))   # True
print(es_feliz(4))    # False


# Ejercicio 19: Comprimir string (Run-length encoding)
# Convierte "AABBBCCCC" en "A2B3C4"
# Si un carácter aparece una sola vez, se queda igual: "ABC" -> "ABC"

def comprimir_string(texto):
    pass  # Tu código aquí

print(comprimir_string("AABBBCCCC"))  # "A2B3C4"
print(comprimir_string("ABCD"))       # "ABCD"


# Ejercicio 20: Media, mediana y moda
# Calcula la media, mediana y moda de una lista de números

import statistics

def media_mediana_moda(lista):
    pass  # Tu código aquí (puedes usar statistics o implementarlo manual)

numeros = [1, 2, 2, 3, 4, 4, 4, 5]
print(media_mediana_moda(numeros))
# {"media": 3.125, "mediana": 3.5, "moda": 4}


# Ejercicio 21: Validar paréntesis balanceados
# Determina si una cadena de paréntesis, corchetes y llaves está balanceada
# Ejemplo: "{[()]}" -> True, "{[(])}" -> False

def parentesis_balanceados(cadena):
    pass  # Tu código aquí (usa una pila/lista)

print(parentesis_balanceados("{[()]}"))   # True
print(parentesis_balanceados("{[(])}"))   # False
print(parentesis_balanceados("()[]{}"))   # True


# Ejercicio 22: Números romanos a enteros
# Convierte un número romano a entero
# Símbolos: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
# Regla: si un símbolo menor precede a uno mayor, se resta

def romano_a_entero(romano):
    pass  # Tu código aquí

print(romano_a_entero("MCMXCIV"))  # 1994
print(romano_a_entero("LVIII"))    # 58


# Ejercicio 23: Generar contraseña aleatoria
# Genera una contraseña aleatoria con: mayúsculas, minúsculas, dígitos y símbolos
# La contraseña debe tener al menos un carácter de cada tipo

import random
import string

def generar_contraseña(longitud=12):
    pass  # Tu código aquí

print(generar_contraseña(16))


# Ejercicio 24: Subsecuencia común más larga (LCS)
# Encuentra la longitud de la subsecuencia común más larga entre dos strings
# Ejemplo: "ABCBDAB" y "BDCAB" -> "BCAB" (longitud 4)

def lcs_longitud(s1, s2):
    pass  # Tu código aquí (programación dinámica)

print(lcs_longitud("ABCBDAB", "BDCAB"))  # 4
