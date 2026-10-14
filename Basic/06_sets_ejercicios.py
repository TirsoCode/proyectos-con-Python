"""
EJERCICIOS DE SETS
Temas: sets, add(), remove(), pop(), in, union(), intersection(),
    difference(), symmetric_difference()
"""

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1
# Crea un set llamado 'frutas' con los elementos: "manzana", "banana", "naranja".
# Luego imprime el set.

frutas = {"manzana", "banana", "naranja"}
# Tu código aquí
print(frutas)
# Ejercicio 2
# Dado el set numeros = {1, 2, 3, 4, 5}, agrega el número 6 usando add().
# Luego imprime el set.

numeros = {1, 2, 3, 4, 5}
# Tu código aquí
(numeros.add(6))
print(numeros)
# Ejercicio 3
# Dado el set letras = {"a", "b", "c"}, intenta agregar "b" nuevamente con add().
# Imprime el set y observa que no cambia.

letras = {"a", "b", "c"}
# Tu código aquí
(letras.add("b"))
print(letras)
# Ejercicio 4
# Dado el set colores = {"rojo", "verde", "azul", "amarillo"},
# elimina "verde" usando remove(). Imprime el set resultante.

colores = {"rojo", "verde", "azul", "amarillo"}
# Tu código aquí
(colores.remove("verde"))
print(colores)
# Ejercicio 5
# Dado el set mascotas = {"perro", "gato", "pez"}, usa pop() para eliminar
# un elemento aleatorio e imprímelo.

mascotas = {"perro", "gato", "pez"}
# Tu código aquí
(mascotas.pop())
print(mascotas)
# Ejercicio 6
# Dado el set pares = {2, 4, 6, 8, 10}, verifica si el número 4 está presente
# usando el operador in. Imprime el resultado.

pares = {2, 4, 6, 8, 10}
# Tu código aquí
print( 4 in pares)
# Ejercicio 7
# Convierte la lista duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5] en un set
# para eliminar duplicados. Luego imprime el set.

duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5]
# Tu código aquí
duplicados = set(duplicados)
print(duplicados)

# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 8
# Crea dos sets: A = {1, 2, 3, 4, 5} y B = {4, 5, 6, 7, 8}.
# Calcula e imprime la unión de ambos sets (todos los elementos sin repetir).

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Tu código aquí
print(A,B)
# Ejercicio 9
# Usando los mismos sets A y B del ejercicio anterior, calcula e imprime
# la intersección (elementos comunes).

# Tu código aquí
print(A.intersection(B))
# Ejercicio 10
# Usando los mismos sets A y B, calcula e imprime la diferencia A - B
# (elementos que están en A pero no en B).

# Tu código aquí
print(A.difference(B))
# Ejercicio 11
# Usando los mismos sets A y B, calcula e imprime la diferencia simétrica
# (elementos que están en A o en B pero no en ambos).
print(A.symmetric_difference(B))
# Tu código aquí

# Ejercicio 12
# Dado el set notas = {7.5, 8.0, 6.5, 9.0, 5.5}, usa un bucle for para
# calcular el promedio de las notas.

notas = {7.5, 8.0, 6.5, 9.0, 5.5}
# Tu código aquí

# Ejercicio 13
# Crea un set vacío llamado 'vocales_enconCdas'. Pide al usuario que ingrese
# una palabra (simula con una variable) y agrega al set cada vocal que aparezca.
# Finalmente imprime qué vocales se encontraron.

palabra = "murcielago"
# Tu código aquí
vocales=set()
palabra_usuario=input("Di una palabra ")
vocales.add(palabra_usuario)
print(vocales)
# Ejercicio 14
# Dado el set edades = {18, 25, 30, 18, 25, 40, 30}, observa que los duplicados
# se eliminan automáticamente. Imprime el set y su longitud.

edades = {18, 25, 30, 18, 25, 40, 30}
# Tu código aquí
print(edades)
print(len(edades))
# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 15
# Dadas las listas lista_a = [1, 2, 3, 4, 5] y lista_b = [4, 5, 6, 7, 8],
# encuentra los elementos que aparecen en ambas listas sin usar sets,
# pero luego verifica tu resultado convirtiendo a sets.

lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]
# Tu código aquí

# Ejercicio 16
# Dado el conjunto universo = set(range(1, 21)), crea un subconjunto 'pares'
# con los números pares y otro 'multiplos3' con los múltiplos de 3.
# Luego encuentra los números que son pares Y múltiplos de 3.

universo = set(range(1, 21))
# Tu código aquí

# Ejercicio 17
# Escribe una función 'letras_unicas' que reciba una cadena y devuelva un set
# con las letras que aparecen (sin espacios, sin signos, sin distinguir mayúsculas).

def letras_unicas(cadena):
    pass

# Tu código aquí (llama a la función con un ejemplo)

# Ejercicio 18
# Dado el set alumnos_primero = {"Ana", "Luis", "Sofía", "Carlos"} y
# alumnos_segundo = {"Luis", "Carlos", "Pedro", "María"}, encuentra:
# - Quiénes están en ambos cursos (intersección)
# - Quiénes están solo en primero (diferencia)
# - Quiénes están solo en segundo (diferencia)

alumnos_primero = {"Ana", "Luis", "Sofía", "Carlos"}
alumnos_segundo = {"Luis", "Carlos", "Pedro", "María"}
# Tu código aquí
print(alumnos_primero.intersection(alumnos_segundo))
print(alumnos_segundo.difference(alumnos_primero))
print(alumnos_segundo.difference(alumnos_primero))
# Ejercicio 19
# Escribe una función 'tiene_duplicados' que reciba una lista y devuelva True
# si tiene elementos repetidos, False en caso contrario. Usa set().

def tiene_duplicados(lista):
    pass

# Tu código aquí (llama a la función con ejemplos)

# Ejercicio 20
# Dado un set de números, usa remove() para eliminar un elemento que NO existe.
# Captura la excepción KeyError y muestra un mensaje amigable.
numero={0,1,6,64,67,78,78,7,}
#numero.remove(5478675)

# Tu código aquí

# Ejercicio 21
# Crea un set comprehension que genere los cuadrados de los números del 1 al 10.

# Tu código aquí

# Ejercicio 22
# Dados tres sets: X = {1, 2, 3}, Y = {3, 4, 5}, Z = {5, 6, 7},
# encuentra los elementos que están en exactamente dos de los tres sets.

X = {1, 2, 3}
Y = {3, 4, 5}
Z = {5, 6, 7}
# Tu código aquí
print(X.difference(Y))
print(Z.difference(X))
print(Y.difference(Z))
# Ejercicio 23
# Dado el set paises = {"México", "España", "Argentina", "Chile", "Perú"},
# usa discard() para eliminar "Brasil" (que no existe). A diferencia de remove(),
# discard() no lanza error. Verifica este comportamiento.

paises = {"México", "España", "Argentina", "Chile", "Perú"}
# Tu código aquí
print(paises.discard("Brasil"))
# Ejercicio 24
# Escribe una función 'elementos_unicos_de_dos_listas' que reciba dos listas
# y devuelva un set con los elementos que están en una lista o en la otra,
# pero no en ambas (diferencia simétrica).

def elementos_unicos_de_dos_listas(l1, l2):
    pass

# Tu código aquí (llama a la función con un ejemplo)

# Ejercicio 25
# Dada la cadena "La programación en Python es divertida y Python es poderoso",
# usa sets para encontrar las palabras únicas (sin signos de puntuación).

texto = "La programación en Python es divertida y Python es poderoso"
# Tu código aquí
print(set(texto))

