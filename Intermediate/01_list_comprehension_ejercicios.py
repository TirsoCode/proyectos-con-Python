"""
Ejercicios de List Comprehension en Python
Temas: range(), [expr for item in iterable], comprehension con condiciones
"""

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1: Cuadrados del 1 al 10
# Usa list comprehension para crear una lista con los cuadrados del 1 al 10
# Ejemplo: [1, 4, 9, 16, ..., 100]

cuadrados = None  # Tu código aquí: [x**2 for x in range(1, 11)]
print(cuadrados)


# Ejercicio 2: Números pares del 0 al 20
# Usa list comprehension con range() para generar los números pares del 0 al 20

pares = None  # Tu código aquí
print(pares)


# Ejercicio 3: Longitud de cada palabra
# Dada una lista de palabras, crea una lista con la longitud de cada palabra

palabras = ["python", "java", "javascript", "rust", "go"]
longitudes = None  # Tu código aquí: [len(p) for p in palabras]
print(longitudes)


# Ejercicio 4: Mayúsculas
# Convierte cada string de una lista a mayúsculas usando list comprehension

frutas = ["manzana", "banana", "cereza", "dátil"]
mayusculas = None  # Tu código aquí
print(mayusculas)


# Ejercicio 5: Tabla del 5
# Genera una lista con los resultados de la tabla del 5: [5, 10, 15, ..., 50]

tabla_5 = None  # Tu código aquí
print(tabla_5)


# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 6: Números pares con condición
# Crea una lista con los números pares del 1 al 30 usando list comprehension con if

pares_30 = None  # Tu código aquí: [x for x in range(1, 31) if x % 2 == 0]
print(pares_30)


# Ejercicio 7: Vocales de una frase
# Extrae todas las vocales de una frase usando list comprehension

frase = "Hola mundo desde Python"
vocales = None  # Tu código aquí: [c for c in frase if c.lower() in "aeiou"]
print(vocales)


# Ejercicio 8: Números divisibles por 3 y 5
# Encuentra los números del 1 al 100 que son divisibles por 3 y por 5

divisibles = None  # Tu código aquí
print(divisibles)


# Ejercicio 9: Celsius a Fahrenheit
# Convierte una lista de temperaturas en Celsius a Fahrenheit usando list comprehension
# Fórmula: F = C * 9/5 + 32

celsius = [0, 10, 20, 30, 40, 100]
fahrenheit = None  # Tu código aquí
print(fahrenheit)


# Ejercicio 10: Filtrar strings por longitud
# Dada una lista de palabras, conserva solo las que tienen más de 5 letras

palabras = ["sol", "ventana", "luz", "computadora", "mar", "teclado", "lapiz"]
largas = None  # Tu código aquí
print(largas)


# Ejercicio 11: Lista de tuplas (número, cuadrado)
# Genera una lista de tuplas (numero, cuadrado) para los números del 1 al 10

tuplas = None  # Tu código aquí: [(x, x**2) for x in range(1, 11)]
print(tuplas)


# Ejercicio 12: Extraer dígitos de un string
# Dado un string alfanumérico, extrae solo los dígitos numéricos como enteros

texto = "Python3.10 es mejor que 2.7"
digitos = None  # Tu código aquí
print(digitos)


# Ejercicio 13: Lista de listas (matriz identidad 3x3)
# Crea una matriz identidad de 3x3 usando list comprehension anidada
# Resultado: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

identidad = None  # Tu código aquí
print(identidad)


# Ejercicio 14: FizzBuzz con list comprehension
# Genera una lista del 1 al 30 donde:
# - "Fizz" si es múltiplo de 3
# - "Buzz" si es múltiplo de 5
# - "FizzBuzz" si es múltiplo de ambos
# - El número en caso contrario
# Pista: usa expresión ternaria dentro de la comprehension

fizzbuzz_lista = None  # Tu código aquí
print(fizzbuzz_lista)


# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 15: Aplanar lista de listas
# Convierte una lista de listas en una sola lista plana

lista_anidada = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
plana = None  # Tu código aquí: [x for sub in lista for x in sub]
print(plana)


# Ejercicio 16: Diccionario con dict comprehension + condicional
# Crea un diccionario donde las claves son números del 1 al 10 y los valores
# son "par" o "impar" según corresponda

par_impar = None  # Tu código aquí: {x: "par" if x % 2 == 0 else "impar" for x in range(1, 11)}
print(par_impar)


# Ejercicio 17: Transponer matriz
# Dada una matriz 3x3, transpónela usando list comprehension anidada

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpuesta = None  # Tu código aquí
print(transpuesta)


# Ejercicio 18: Factoriales con list comprehension
# Crea una lista con los factoriales de los números del 1 al 10
# Pista: puedes usar math.factorial() o implementarlo

import math
factoriales = None  # Tu código aquí
print(factoriales)


# Ejercicio 19: Palabras palíndromas
# Dada una lista de palabras, encuentra las que son palíndromas
# (se leen igual al derecho y al revés)

palabras = ["radar", "python", "reconocer", "sol", "somos", "casa", "anilina"]
palindromas = None  # Tu código aquí
print(palindromas)


# Ejercicio 20: Producto cartesiano
# Genera todas las combinaciones posibles de dos listas usando list comprehension anidada

colores = ["rojo", "verde", "azul"]
tallas = ["S", "M", "L"]
combinaciones = None  # Tu código aquí: [(color, talla) for color in colores for talla in tallas]
print(combinaciones)


# Ejercicio 21: Números primos con list comprehension
# Encuentra todos los números primos del 1 al 50 usando list comprehension
# Pista: un número es primo si no tiene divisores entre 2 y sqrt(n)

primos = None  # Tu código aquí (puedes combinar con all())
print(primos)


# Ejercicio 22: Triángulo de Pascal (fila n)
# Genera la fila n del triángulo de Pascal usando list comprehension
# Fila 4: [1, 4, 6, 4, 1]

from math import comb
n = 5  # Fila deseada (0-indexed)
fila_pascal = None  # Tu código aquí: [comb(n, k) for k in range(n+1)]
print(fila_pascal)


# Ejercicio 23: Agrupar por primera letra
# Dada una lista de palabras, crea un diccionario que agrupe palabras por su primera letra
# Usa dict comprehension con set

animales = ["gato", "perro", "gallina", "pato", "gorrión", "paloma", "ganso"]
agrupados = None  # Tu código aquí
print(agrupados)


# Ejercicio 24: Lista de números con formato
# Dada una lista de números, formatea cada uno como "Nº 001", "Nº 002", etc.
# Usa list comprehension con f-strings y formato de 3 dígitos

numeros = [1, 5, 12, 45, 123, 999]
formateados = None  # Tu código aquí
print(formateados)


# Ejercicio 25: Secuencia de Collatz
# Genera la secuencia de Collatz para un número dado usando list comprehension
# Regla: si es par -> n//2, si es impar -> 3n+1, hasta llegar a 1
# Pista: esto requiere un enfoque diferente, usa una función auxiliar

def collatz(n):
    secuencia = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        secuencia.append(n)
    return secuencia

n_inicial = 13
secuencia = None  # Tu código aquí (llama a la función)
print(f"Secuencia de Collatz para {n_inicial}: {secuencia}")
