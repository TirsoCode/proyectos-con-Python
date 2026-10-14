"""
Ejercicios de Funciones Lambda en Python
Temas: lambda, lambda con map/filter/sort, closures con lambda
"""

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1: Lambda simple
# Crea una función lambda que sume 10 a un número y asígnala a la variable `sumar_10`
# Llámala con el valor 5

sumar_10 = None  # Tu código aquí: lambda x: x + 10
print(sumar_10(5))  # 15


# Ejercicio 2: Multiplicar con lambda
# Crea una lambda que multiplique dos números y pruébala

multiplicar = None  # Tu código aquí: lambda a, b: a * b
print(multiplicar(4, 5))  # 20


# Ejercicio 3: Lambda condicional
# Crea una lambda que devuelva "par" si el número es par, o "impar" si es impar

par_impar = None  # Tu código aquí
print(par_impar(4))  # "par"
print(par_impar(7))  # "impar"


# Ejercicio 4: Lambda con un solo argumento por defecto
# Crea una lambda que eleve un número a una potencia (por defecto al cuadrado)

potencia = None  # Tu código aquí: lambda x, exp=2: x ** exp
print(potencia(5))    # 25
print(potencia(2, 3)) # 8


# Ejercicio 5: Lambda con strings
# Crea una lambda que tome un string y devuelva la primera letra en mayúscula

primera_mayus = None  # Tu código aquí
print(primera_mayus("python"))  # "P"


# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 6: Lambda con map() - elevar al cuadrado
# Usa map() con una lambda para elevar al cuadrado todos los elementos de una lista

numeros = [1, 2, 3, 4, 5]
cuadrados = None  # Tu código aquí: list(map(lambda x: x**2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]


# Ejercicio 7: Lambda con map() - convertir a Fahrenheit
# Convierte una lista de temperaturas Celsius a Fahrenheit usando map() con lambda

celsius = [0, 10, 20, 30, 40]
fahrenheit = None  # Tu código aquí
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]


# Ejercicio 8: Lambda con filter() - números pares
# Usa filter() con una lambda para obtener solo los números pares de una lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = None  # Tu código aquí: list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]


# Ejercicio 9: Lambda con filter() - palabras cortas
# Filtra las palabras que tienen 4 o menos letras usando filter() con lambda

palabras = ["sol", "universo", "luz", "computadora", "mar", "python"]
cortas = None  # Tu código aquí
print(cortas)  # ["sol", "luz", "mar"]


# Ejercicio 10: Lambda con sorted() - ordenar por longitud
# Ordena una lista de palabras por su longitud usando sorted() con lambda como key

palabras = ["python", "java", "c", "javascript", "rust", "go"]
ordenadas = None  # Tu código aquí: sorted(palabras, key=lambda x: len(x))
print(ordenadas)  # ["c", "go", "java", "rust", "python", "javascript"]


# Ejercicio 11: Lambda con sorted() - ordenar por el último carácter
# Ordena una lista de palabras por su último carácter

palabras = ["manzana", "banana", "cereza", "dátil", "uva"]
ordenadas = None  # Tu código aquí
print(ordenadas)


# Ejercicio 12: Lambda con sorted() - ordenar tuplas
# Dada una lista de tuplas (nombre, edad), ordena por edad ascendente

personas = [("Ana", 25), ("Luis", 30), ("Marta", 22), ("Carlos", 28)]
ordenadas_edad = None  # Tu código aquí
print(ordenadas_edad)
# [("Marta", 22), ("Ana", 25), ("Carlos", 28), ("Luis", 30)]


# Ejercicio 13: Lambda con max() y min()
# Usa lambda para encontrar la palabra más larga y la más corta en una lista

palabras = ["python", "java", "javascript", "rust", "go"]
mas_larga = None  # Tu código aquí: max(palabras, key=lambda x: len(x))
mas_corta = None  # Tu código aquí
print(f"Más larga: {mas_larga}, Más corta: {mas_corta}")


# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 14: Lambda con map() y filter() combinados
# Primero filtra los números impares de una lista, luego eleva cada uno al cubo

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubos_impares = None  # Tu código aquí
print(cubos_impares)  # [1, 27, 125, 343, 729]


# Ejercicio 15: Ordenar lista de diccionarios con lambda
# Dada una lista de diccionarios, ordénalos por el valor de la clave "edad"

estudiantes = [
    {"nombre": "Ana", "edad": 25, "nota": 8.5},
    {"nombre": "Luis", "edad": 22, "nota": 7.0},
    {"nombre": "Marta", "edad": 28, "nota": 9.2},
    {"nombre": "Carlos", "edad": 20, "nota": 6.8},
]
ordenados_edad = None  # Tu código aquí
print(ordenados_edad)


# Ejercicio 16: Closure con lambda
# Crea una función crear_multiplicador que acepte un factor n y devuelva
# una lambda que multiplique su argumento por ese factor

def crear_multiplicador(n):
    pass  # Tu código aquí: return lambda x: x * n

multiplicar_por_3 = crear_multiplicador(3)
multiplicar_por_5 = crear_multiplicador(5)
print(multiplicar_por_3(10))  # 30
print(multiplicar_por_5(10))  # 50


# Ejercicio 17: Calculadora con lambda
# Crea un diccionario que asocie operadores ("+", "-", "*", "/") con lambdas
# que realicen la operación correspondiente

calculadora = {
    "+": lambda a, b: a + b,
    "-": None,  # Tu código aquí
    "*": None,  # Tu código aquí
    "/": None,  # Tu código aquí
}

print(calculadora["+"](10, 5))   # 15
print(calculadora["-"](10, 5))   # 5
print(calculadora["*"](10, 5))   # 50
print(calculadora["/"](10, 5))   # 2.0


# Ejercicio 18: Ordenar números según su valor absoluto
# Dada una lista con números negativos y positivos, ordénalos por valor absoluto

numeros = [-5, 3, -2, 8, -1, 0, -4]
ordenados_abs = None  # Tu código aquí: sorted(numeros, key=lambda x: abs(x))
print(ordenados_abs)  # [0, -1, -2, 3, -4, -5, 8]


# Ejercicio 19: Lambda con reduce() - producto de una lista
# Usa reduce() del módulo functools con una lambda para multiplicar todos los elementos

from functools import reduce

numeros = [1, 2, 3, 4, 5]
producto = None  # Tu código aquí: reduce(lambda x, y: x * y, numeros)
print(producto)  # 120


# Ejercicio 20: Lambda con reduce() - encontrar el máximo
# Usa reduce() con lambda para encontrar el número más grande en una lista

numeros = [23, 45, 12, 67, 34, 89, 5]
maximo = None  # Tu código aquí
print(maximo)  # 89


# Ejercicio 21: Ordenar strings por número de vocales
# Dada una lista de palabras, ordénalas de mayor a menor número de vocales

palabras = ["python", "programacion", "lambda", "funcion", "ordenador"]
ordenadas_vocales = None  # Tu código aquí (sorted con reverse=True y key=lambda)
print(ordenadas_vocales)
# ["programacion", "ordenador", "funcion", "python", "lambda"]


# Ejercicio 22: Lambda para filtrar por múltiples condiciones
# Filtra los números que son divisibles por 2 y por 3 (es decir, por 6)

numeros = list(range(1, 51))
divisibles_6 = None  # Tu código aquí
print(divisibles_6)  # [6, 12, 18, 24, 30, 36, 42, 48]


# Ejercicio 23: Comprobar si todos/algún elemento cumple una condición con lambda
# Usa all() y any() con lambda para verificar condiciones en una lista

numeros = [2, 4, 6, 8, 10]
todos_pares = None       # Tu código aquí: all(map(lambda x: x % 2 == 0, numeros))
hay_impares = None       # Tu código aquí: any(map(lambda x: x % 2 != 0, numeros))
print(f"¿Todos pares? {todos_pares}")     # True
print(f"¿Hay impares? {hay_impares}")     # False


# Ejercicio 24: Mapeo condicional con lambda
# Usa map() con una lambda que aplique una transformación diferente según el valor:
# - Si el número es par, devuelve su cuadrado
# - Si es impar, devuelve su cubo

numeros = [1, 2, 3, 4, 5, 6]
transformados = None  # Tu código aquí
print(transformados)  # [1, 4, 27, 16, 125, 36]


# Ejercicio 25: Closure contador con lambda
# Crea una función crear_contador que devuelva una lambda que incremente
# y devuelva un contador cada vez que se llame

def crear_contador():
    cuenta = 0
    # Devuelve una lambda que incrementa cuenta en 1 cada vez y devuelve el nuevo valor
    pass  # Tu código aquí

contador_1 = crear_contador()
print(contador_1())  # 1
print(contador_1())  # 2
print(contador_1())  # 3

contador_2 = crear_contador()
print(contador_2())  # 1 (contador independiente)
