"""
EJERCICIOS DE LOOPS
Temas: while, for, range(), break, continue, else en loops,
       iterar listas/dicts/sets/strings
"""

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1
# Usa un bucle for con range() para imprimir los números del 1 al 10.
for gg in range(11):
    print(gg)
# Tu código aquí

# Ejercicio 2
# Usa un bucle while para imprimir los números del 1 al 5.
a=1
while a<=5:
    print(a)
    a+=1
# Tu código aquí

# Ejercicio 3
# Dada la lista frutas = ["manzana", "pera", "uva", "naranja"],
# usa un bucle for para imprimir cada fruta.

frutas = ["manzana", "pera", "uva", "naranja"]
# Tu código aquí
for adios in frutas:
    print(adios)
# Ejercicio 4
# Usa un bucle for para iterar sobre la cadena "Python" e imprime cada letra.
h="python"
for fg in h:
    print(fg)
# Tu código aquí

# Ejercicio 5
# Usa for con range() para imprimir los números pares del 2 al 20 (inclusive).
d=range(2,21)
for rgg in d:
    print(rgg)
# Tu código aquí

# Ejercicio 6
# Usa un bucle while para sumar los números del 1 al 10 e imprime el resultado.
hola1=0
while hola1 <10:
    hola1+=1
    print(hola1)
# Tu código aquí

# Ejercicio 7
# Dado el set numeros = {10, 20, 30, 40, 50}, usa un bucle for para
# iterar sobre él e imprimir cada elemento.


numeros_set = {10, 20, 30, 40, 50}
# Tu código aquí
for asj in numeros_set:
    print(asj)
# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 8
# Dado el diccionario edades = {"Ana": 25, "Luis": 30, "Sofía": 22},
# usa un bucle for con items() para imprimir "Nombre: X, Edad: Y".

edades = {"Ana": 25, "Luis": 30, "Sofía": 22}
# Tu código aquí
for nombre,edad in edades.items():
    print(f"me llamo {nombre}  y tengo {edad}")
# Ejercicio 9
# Usa un bucle for con range() y break para encontrar el primer número
# divisible por 7 entre 1 y 50. Imprime el número y sal del bucle.

# Tu código aquí
rango=range(1,51)
for h in rango :
    if h%7==0:
        print("Encontardo",h)
        break

# Ejercicio 10
# Usa un bucle for con continue para imprimir los números del 1 al 10
# saltándote el 5.
a=range(1,11)
for g in a :
    if g==5:
        continue
    print(g)
# Tu código aquí

# Ejercicio 11
# Usa un bucle for con else para buscar el número 15 en una lista.
# Si lo encuentras, imprime "Encontrado" y rompe el bucle.
# Si no, el else del bucle debe ejecutarse e imprimir "No encontrado".

numeros_lista = [3, 7, 11, 15, 19]
# Tu código aquí
for f in numeros_lista:
    if f==15:
        print("Encontrado")
    else:
        print("No encontardo")
# Ejercicio 12
# Dada la frase "Aprender Python es divertido", usa un bucle for para
# contar cuántas vocales tiene (a, e, i, o, u). No distingas mayúsculas.

frase = "Aprender Python es divertido"
vocales = "aeiou"
cuantas=0
# Tu código aquí
for letra in frase:
    if letra.lower() in vocales:
        cuantas+=1

print(f"Tiene {cuantas} vocales")

# Ejercicio 13
# Usa un bucle while para pedir al usuario que adivine un número secreto
# (simula con la variable adivinanza = 7). El bucle continúa hasta que acierte.
# Por cada intento, muestra "Intenta de nuevo".
secreto = 7

# Tu código aquí (usa input() para pedir el número)
contraseña_usario=int(input("Adivina el nuemro secreto "))
while secreto!=contraseña_usario:
    print("Fallaste")
    contraseña_usario=int(input("Adivina el nuemro secreto "))
    if contraseña_usario==secreto:
        print("Acertaste")
# Ejercicio 14
# Dada la lista precios = [150, 230, 75, 300, 45, 180], usa un bucle for
# para calcular e imprimir el precio total (suma de todos los elementos).

precios = [150, 230, 75, 300, 45, 180]
# Tu código aquí
suma=0
for i in precios:
    suma+=i
print(suma)
# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 15
# Usa un bucle for anidado para imprimir una tabla de multiplicar del 1 al 5.
# Cada fila debe mostrar: "1 x 1 = 1", etc.
for a in range(1,6):
    for df in range(1,6):
        hola=df*a
        print(df,"*",a,"=",hola)
# Tu código aqui
# Dada la lista palabras = ["sol", "mar", "montaña", "lago", "árbol"],
# usa un bucle for con enumerate() para imprimir cada palabra con su índice.

palabras = ["sol", "mar", "montaña", "lago", "árbol"]
# Tu código aquí
for palabras in enumerate(palabras):
    print(palabras)
# Ejercicio 17
# Usa un bucle while para implementar el juego de "FizzBuzz":
# Imprime los números del 1 al 30, pero para múltiplos de 3 imprime "Fizz",
# para múltiplos de 5 imprime "Buzz", y para ambos "FizzBuzz".

a = 1

while a <= 30:
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
        print(a)
    a += 1

# Ejercicio 18
# Dada la matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], usa bucles anidados
# para sumar todos los elementos e imprimir el resultado.


# Dado un rango de números del 1 al 20, usa un bucle for para encontrar
# e imprimir todos los números primos.

# Tu código aquí

# Ejercicio 20
# Usa un bucle for para iterar sobre los caracteres de "Python Programming"
# y crea una lista con los índices de las letras "o".

cadena = "Python Programming"
# Tu código aquí
for i in enumerate(cadena):
    if i == "0":
        print(i)
# Ejercicio 21
# Dada la lista anidada datos = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]],
# usa un bucle for para aplanarla en una sola lista.

datos = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
# Tu código aquí
for y in datos:
    
# Ejercicio 22
# Usa un bucle for con la función zip() para recorrer dos listas
# simultáneamente: nombres = ["Ana", "Luis", "Sofía"] y
# notas_lista = [8.5, 7.0, 9.5]. Imprime "Nombre: Nota".

nombres = ["Ana", "Luis", "Sofía"]
notas_lista = [8.5, 7.0, 9.5]
# Tu código aquí

# Ejercicio 23
# Usa un bucle while con break para encontrar el primer número mayor que 100
# que sea divisible por 7 y por 3 simultáneamente.

# Tu código aquí

# Ejercicio 24
# Dado el string "Hola Mundo", usa un bucle for para construir un nuevo string
# que contenga solo las consonantes.

texto = "Hola Mundo"
# Tu código aquí

# Ejercicio 25
# Escribe un programa que use un bucle for para calcular el factorial de un
# número n = 7. El factorial de n es n * (n-1) * (n-2) * ... * 1.

n = 7
# Tu código aquí
