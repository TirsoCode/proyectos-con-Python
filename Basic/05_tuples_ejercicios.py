"""
EJERCICIOS DE TUPLAS
Temas: tuplas, count(), index(), inmutabilidad, desempaquetado
"""

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1
# Crea una tupla llamada 'colores' con los valores: "rojo", "verde", "azul".
# Luego imprime la tupla completa.
colores = ("rojo", "verde", "azul")
# Tu código aquí
print(colores)

# Ejercicio 2
# Dada la tupla numeros = (10, 20, 30, 40, 50), imprime el primer y el último elemento.

numeros = (10, 20, 30, 40, 50)
# Tu código aquí
print(numeros[0])
print(numeros[-1])
# Ejercicio 3
# Dada la tupla mixta = (1, "hola", 3.14, True), imprime el tipo de cada elemento
# usando type() dentro de un bucle for.

mixta = (1, "hola", 3.14, True)
# Tu código aquí

# Ejercicio 4
# Intenta modificar el segundo elemento de la tupla frutas = ("manzana", "pera", "uva")
# Asígnale "naranja". Ejecuta el código y observa el error. Luego comenta esa línea.

frutas = ("manzana", "pera", "uva")
# Tu código aquí

# Ejercicio 
# Dada la tupla valores = (5, 10, 5, 20, 5, 30), usa el método count()
# para contar cuántas veces aparece el número 5.

valores = (5, 10, 5, 20, 5, 30)
# Tu código aquí
print(valores.count(5))
# Ejercicio 6
# Dada la tupla animales = ("gato", "perro", "conejo", "perro", "hamster"),
# usa el método index() para encontrar la posición de "conejo".

animales = ("gato", "perro", "conejo", "perro", "hamster")
# Tu código aquí
print(animales.index("conejo"))
# Ejercicio 7
# Dada la tupla letras = ("a", "b", "c"), usa el operador in para verificar
# si "b" está dentro de la tupla. Imprime True o False.

letras = ("a", "b", "c")
# Tu código aquí
print("b" in letras)
# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 8
# Dada la tupla edades = (25, 30, 18, 42, 30, 25, 30),
# usa count() para determinar qué edad aparece más veces e imprímela.

edades = (25, 30, 18, 42, 30, 25, 30)
# Tu código aquí

# Ejercicio 9
# Dada la tupla datos = (3, 6, 2, 8, 1, 9, 4), encuentra el valor máximo
# y el valor mínimo sin usar max() ni min(). Usa un bucle for.

datos = (3, 6, 2, 8, 1, 9, 4)
# Tu código aquí

# Ejercicio 10
# Desempaqueta la tupla persona = ("María", 29, "Ingeniera") en tres variables
# llamadas nombre, edad, profesion. Luego imprime cada una.

persona = ("María", 29,"ingeniera")
# Tu código aquí
nombre,edad,profesion=persona
print(nombre)
print(edad)
print(profesion)
# Ejercicio 11
# Dada la tupla anidada matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
# accede al número 5 e imprímelo.

matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# Tu código aquí
hola=matriz[1][1]
print(hola)
# Ejercicio 12
# Convierte la lista lista_nombres = ["Ana", "Luis", "Sofía"] en una tupla
# usando tuple(). Imprime la tupla resultante.

lista_nombres = ["Ana", "Luis", "Sofía"]
# Tu código aquí
print(tuple(lista_nombres))
# Ejercicio 13
# Dada la tupla puntos = ((1, 2), (3, 4), (5, 6)), usa un bucle for para
# desempaquetar cada par de coordenadas e imprimirlas como "x: 1, y: 2".

puntos = ((1, 2), (3, 4), (5, 6))
# Tu código aquí

# Ejercicio 14
# Crea una tupla de un solo elemento que contenga el número 42.
# Imprime la tupla y su tipo.
hola=(42)
# Tu código aquí
print(type(hola))
print(hola)
# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 15
# Dada la tupla numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
# crea una nueva tupla que contenga solo los números pares.
# Usa una comprensión de tupla con tuple(generador).

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Tu código aquí
# Ejercicio 16
# Desempaqueta la tupla valores = (100, 200, 300, 400, 500) de forma que
# el primer valor vaya a 'a', el último a 'e', y los del medio a una lista 'resto'.
# Usa el operador *.

valores = (100, 200, 300, 400, 500)
# Tu código aquí

# Ejercicio 17
# Escribe una función llamada 'intercambiar' que reciba una tupla de dos elementos
# y devuelva una nueva tupla con los elementos en orden inverso.

def intercambiar(tupla):
    pass

# Tu código aquí (llama a la función con un ejemplo)

# 



# Ejercicio 20
# Escribe una función 'contar_hasta' que reciba un número n y devuelva una tupla
# con los números del 1 al n (inclusive). Usa range() y tuple().

def contar_hasta(n):
    pass

# Tu código aquí (llama a la función con un ejemplo)

# Ejercicio 21
# Dada la tupla mezclada = (1, "dos", 3.0, "cuatro", 5, "seis"),
# crea dos tuplas separadas: una solo con elementos de tipo int y float,
# y otra solo con elementos de tipo str. Usa isinstance().

mezclada = (1, "dos", 3.0, "cuatro", 5, "seis")
# Tu código aquí


# Ejercicio 22
# Dada la frase "Python es genial", conviértela en una tupla de palabras
# usando split(). Luego desempaqueta cada palabra en variables e imprímelas.

frase = "Python es genial"
# Tu código aquí
desempaquetado=frase.split()
print(desempaquetado)
pal1,pal2,pal3=desempaquetado
print(pal1)
print(pal2)
print(pal3)
# Ejercicio 23
# Investiga qué ocurre si intentas usar index() con un valor que no existe
# en la tupla. Crea un ejemplo donde captures la excepción ValueError con try/except.

# Tu código aquí

# Ejercicio 24
# Dadas dos tuplas a = (1, 2, 3) y b = (4, 5, 6), crea una tercera tupla c
# que sea la concatenación de ambas. Luego crea otra tupla d que repita a tres veces.

a = (1, 2, 3)
b = (4, 5, 6)
# Tu código aquí
c=a+b
print(c)
d=a*3
print(d)