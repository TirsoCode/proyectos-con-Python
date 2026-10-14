"""
Ejercicios de Funciones de Orden Superior
Temas: funciones de orden superior, closures, map(), filter(), reduce()
"""

from functools import reduce

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1: Función que recibe otra función
# Escribe una función `aplicar_funcion` que tome una función y un valor,
# y aplique la función al valor

def aplicar_funcion(func, valor):
    pass  # Tu código aquí

print(aplicar_funcion(lambda x: x * 2, 5))  # 10
print(aplicar_funcion(lambda x: x ** 2, 4))  # 16


# Ejercicio 2: map() básico - convertir a mayúsculas
# Usa map() para convertir todas las palabras de una lista a mayúsculas

palabras = ["hola", "mundo", "python", "map"]
mayusculas = None  # Tu código aquí: list(map(str.upper, palabras))
print(mayusculas)  # ["HOLA", "MUNDO", "PYTHON", "MAP"]


# Ejercicio 3: map() con función definida
# Define una función `doble` y pásala a map() para duplicar cada número

def doble(n):
    return n * 2

numeros = [1, 2, 3, 4, 5]
duplicados = None  # Tu código aquí: list(map(doble, numeros))
print(duplicados)  # [2, 4, 6, 8, 10]


# Ejercicio 4: filter() básico - números positivos
# Usa filter() para obtener solo los números positivos de una lista

def es_positivo(n):
    return n > 0

numeros = [-3, -1, 0, 2, 5, -4, 7]
positivos = None  # Tu código aquí: list(filter(es_positivo, numeros))
print(positivos)  # [2, 5, 7]


# Ejercicio 5: reduce() básico - suma total
# Usa reduce() para sumar todos los elementos de una lista

numeros = [1, 2, 3, 4, 5]
suma_total = None  # Tu código aquí: reduce(lambda x, y: x + y, numeros)
print(suma_total)  # 15


# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 6: map() con múltiples iterables
# Usa map() con dos listas para sumar elemento a elemento
# map() puede recibir varias listas; la función debe aceptar tantos args como listas

numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]
sumas = None  # Tu código aquí: list(map(lambda x, y: x + y, numeros1, numeros2))
print(sumas)  # [5, 7, 9]


# Ejercicio 7: filter() para eliminar strings vacíos
# Usa filter() para eliminar strings vacíos de una lista

def no_vacio(s):
    return len(s) > 0  # o simplemente: return bool(s)

datos = ["hola", "", "mundo", "", "", "python", ""]
limpio = None  # Tu código aquí
print(limpio)  # ["hola", "mundo", "python"]


# Ejercicio 8: reduce() con valor inicial
# Usa reduce() con valor inicial 10 para sumar todos los números

numeros = [1, 2, 3, 4, 5]
suma_inicial = None  # Tu código aquí: reduce(lambda x, y: x + y, numeros, 10)
print(suma_inicial)  # 25


# Ejercicio 9: map() con strings - obtener iniciales
# Usa map() para obtener la primera letra de cada palabra en una lista

nombres = ["Ana", "Luis", "Marta", "Carlos"]
iniciales = None  # Tu código aquí: list(map(lambda x: x[0], nombres))
print(iniciales)  # ["A", "L", "M", "C"]


# Ejercicio 10: Closure - saludo personalizado
# Crea una función `crear_saludo` que tome un string `saludo` y devuelva
# una función que tome un `nombre` y devuelva el saludo completo

def crear_saludo(saludo):
    pass  # Tu código aquí (devuelve una función interna que use `saludo` y `nombre`)

saludo_formal = crear_saludo("Hola, buenos días")
saludo_informal = crear_saludo("¡Qué onda")
print(saludo_formal("Ana"))     # "Hola, buenos días Ana"
print(saludo_informal("Luis"))  # "¡Qué onda Luis"


# Ejercicio 11: Closure - acumulador
# Crea una función `crear_acumulador` que devuelva una función que vaya
# sumando los valores que se le pasen, manteniendo un total interno

def crear_acumulador():
    total = 0
    pass  # Tu código aquí (devuelve función interna que modifique `total`)

acumulador = crear_acumulador()
print(acumulador(5))   # 5
print(acumulador(3))   # 8
print(acumulador(10))  # 18


# Ejercicio 12: map() y filter() encadenados
# Primero filtra los números impares, luego eleva cada uno al cuadrado

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = None  # Tu código aquí
print(resultado)  # [1, 9, 25, 49, 81]


# Ejercicio 13: reduce() - encontrar el máximo
# Usa reduce() para encontrar el valor máximo de una lista

numeros = [23, 45, 12, 67, 34, 89, 5]
maximo = None  # Tu código aquí: reduce(lambda x, y: x if x > y else y, numeros)
print(maximo)  # 89


# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 14: Decorador simple
# Crea un decorador `mayusculas` que convierta el resultado de una función
# a mayúsculas automáticamente

def mayusculas(func):
    pass  # Tu código aquí

@mayusculas
def saludar(nombre):
    return f"hola {nombre}"

print(saludar("ana"))  # "HOLA ANA"


# Ejercicio 15: Decorador para medir tiempo
# Crea un decorador `medir_tiempo` que mida y muestre el tiempo de ejecución
# de una función

import time

def medir_tiempo(func):
    pass  # Tu código aquí

@medir_tiempo
def calcular_factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(calcular_factorial(10000))  # Debe mostrar el tiempo de ejecución


# Ejercicio 16: reduce() - producto de todos los números
# Usa reduce() para multiplicar todos los números de una lista

numeros = [1, 2, 3, 4, 5]
producto = None  # Tu código aquí
print(producto)  # 120


# Ejercicio 17: map() con múltiples funciones
# Aplica diferentes operaciones (doble, triple, cuádruple) a los números
# usando map() con una función que devuelva una tupla

def operaciones_multiples(n):
    return (n, n*2, n*3, n*4)  # (original, doble, triple, cuadruple)

numeros = [1, 2, 3]
resultados = None  # Tu código aquí: list(map(operaciones_multiples, numeros))
print(resultados)
# [(1, 2, 3, 4), (2, 4, 6, 8), (3, 6, 9, 12)]


# Ejercicio 18: filter() con función que evalúa múltiples condiciones
# Filtra números que sean primos y mayores que 10

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primo_y_mayor_que_10(n):
    pass  # Tu código aquí (combina es_primo y n > 10)

numeros = list(range(1, 51))
filtrados = None  # Tu código aquí
print(filtrados)  # [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


# Ejercicio 19: reduce() para aplanar lista de listas
# Usa reduce() para convertir una lista de listas en una sola lista plana

lista_anidada = [[1, 2, 3], [4, 5], [6, 7, 8]]
plana = None  # Tu código aquí: reduce(lambda x, y: x + y, lista_anidada)
print(plana)  # [1, 2, 3, 4, 5, 6, 7, 8]


# Ejercicio 20: Decorador con argumentos
# Crea un decorador `repetir` que acepte un argumento `n` y repita la
# ejecución de la función decorada n veces

def repetir(n):
    pass  # Tu código aquí

@repetir(3)
def decir_hola():
    print("¡Hola!")

decir_hola()  # Debe imprimir "¡Hola!" 3 veces


# Ejercicio 21: reduce() para construir un diccionario
# Usa reduce() para convertir una lista de tuplas (clave, valor) en un diccionario

pares = [("a", 1), ("b", 2), ("c", 3)]
diccionario = None  # Tu código aquí
print(diccionario)  # {"a": 1, "b": 2, "c": 3}


# Ejercicio 22: Composición de funciones
# Crea una función `componer` que tome dos funciones f y g, y devuelva
# una nueva función que sea f(g(x))

def componer(f, g):
    pass  # Tu código aquí

def cuadrado(x):
    return x ** 2

def mas_uno(x):
    return x + 1

f_g = componer(cuadrado, mas_uno)
g_f = componer(mas_uno, cuadrado)
print(f_g(3))  # (3+1)^2 = 16
print(g_f(3))  # (3^2)+1 = 10


# Ejercicio 23: Currying con funciones de orden superior
# Implementa una función `currificar` que convierta una función de 2 argumentos
# en una secuencia de funciones de 1 argumento

def currificar(func):
    pass  # Tu código aquí

def suma(a, b):
    return a + b

suma_currificada = currificar(suma)
print(suma_currificada(5)(3))  # 8


# Ejercicio 24: partial con functools
# Usa functools.partial para crear una función `doble` a partir de una función
# `multiplicar` con un argumento fijo

from functools import partial

def multiplicar(a, b):
    return a * b

doble = None  # Tu código aquí: partial(multiplicar, 2)
triple = None  # Tu código aquí
print(doble(5))   # 10
print(triple(5))  # 15


# Ejercicio 25: Pipeline de funciones
# Crea una función `pipeline` que reciba un valor inicial y una lista de funciones,
# y aplique cada función en secuencia al resultado de la anterior

def pipeline(valor_inicial, funciones):
    pass  # Tu código aquí (usa reduce o un bucle)

funciones = [
    lambda x: x + 2,
    lambda x: x * 3,
    lambda x: x - 5,
]
print(pipeline(5, funciones))  # ((5 + 2) * 3) - 5 = 16
