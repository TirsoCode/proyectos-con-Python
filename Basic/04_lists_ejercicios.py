# ============================================================
# EJERCICIOS: LISTAS, INDEXING, MÉTODOS, SLICING, COPY
# ============================================================
# Cada ejercicio tiene instrucciones en comentarios (#).
# Escribe tu código debajo de cada instrucción.
# ============================================================

# ----------------------------------------------------------
# NIVEL FÁCIL (1-5)
# ----------------------------------------------------------

# 1. Crea una lista llamada frutas con los elementos:
#    ". Imprime la lista.
lista_compra=["manzana","banana", "naranja"]
print(lista_compra)
# 2. Imprime el primer elemento de la lista frutas (índice 0)
#    y el último elemento (índice -1).
print(lista_compra[-1])
print(lista_compra[0])
# 3. Agrega "uva" al final de la lista frutas usando append().
#    Imprime la lista actualizada.
print(lista_compra.append("uva"))
print(lista_compra)
# 4. Crea una lista numeros = [10, 20, 30, 40, 50]. Imprime
#    la longitud de la lista usando len().
numeros = [10, 20, 30, 40, 50]
print(len(numeros))
# 5. Inserta "fresa" en la posición 0 de la lista frutas
#    usando insert(). Imprime la lista.
(lista_compra.insert(0,"fresa"))
print(lista_compra)
# ----------------------------------------------------------
# NIVEL MEDIO (6-15)
# ----------------------------------------------------------s

# 6. Elimina "banana" de la lista frutas usando remove().
#    Si el elemento no existe, ¿qué ocurre? Imprime la lista.
(lista_compra).remove("banana")
print(lista_compra)
# 7. Usa pop() para eliminar y obtener el último elemento de
#    la lista numeros = [10, 20, 30, 40, 50]. Imprime el
#    elemento eliminado y la lista restante.

# 8. Invierte el orden de la lista numeros usando reverse().
#    Imprime la lista invertida.
(numeros.reverse())
print(numeros)
# 9. Ordena la lista edades = [25, 18, 30, 22, 27] de forma
#    ascendente usando sort(). Imprime el resultado.
edades = [25, 18, 30, 22, 27.] 
(edades.sort())
# 10. Crea una copia de la lista frutas llamada frutas_copia
#     usando copy(). Agrega "kiwi" a frutas_copia. Imprime
#     ambas listas para verificar que son independientes.
frutas_copia=lista_compra
frutas_copia.append("kiwi")
print(frutas_copia)
print(lista_compra)
# 11. Usa slicing para obtener los primeros 3 elementos de la
letras = ["a", "b", "c", "d", "e", "f"]
print(letras[0:3])
# 12. Usa slicing para obtener los elementos en posiciones
#     pares de letras (índices 0, 2, 4).

#     Imprime el tipo de cada elemento usando type() dentro
#     de un bucle o de forma individual.

# 14. Usa el operador + para concatenar 
#     y . Guarda el resultado en listas_c.
listas_a = [1, 2, 3]
listas_b = [4, 5, 6]
lista_c=listas_a+listas_b
# 15. Usa el operador * para repetir la lista [0, 1] tres veces.
#     Imprime el resultado.
lista = [0,1*3]
print(lista)
print(lista*3)
# ----------------------------------------------------------
# NIVEL AVANZADO (16-25)
# ----------------------------------------------------------

# 16. Pide al usuario 5 números (con input()), conviértelos a int,
#     guárdalos en una lista. Luego calcula e imprime:
#     - El menor número (con min())
#     - El mayor número (con max())
#     - La suma (con sum())

# 17. Dada la lista nums = [3, 7, 2, 9, 5, 1, 8], ordénala de
#     forma descendente. Luego reemplaza el elemento del medio
#     por 0 (si la lista tiene longitud impar). Imprime la lista.
nums = [3, 7, 2, 9, 5, 1, 8]
nums.sort(reverse=True)

# 18. Escribe un programa que elimine los elementos duplicados
#     de la lista duplicados = [1, 2, 2, 3, 4, 4, 5, 1].
#     Mantén el orden original. (Pista: crea una nueva lista
#     y usa el operador "in" o not in)
duplicados = [1, 2, 2, 3, 4, 4, 5, ]
my_st=set(duplicados)
print(my_st)
# 19. Dada una lista de palabras = ["sol", "luna", "mar", "estrella",
#     "cielo", "nube"], crea una nueva lista que contenga solo
#     las palabras con más de 3 letras.
palabras = ["sol", "luna", "mar", "estrella","cielo", "nube"]
# 20. Crea una matriz de 3x3 (lista de listas) con números del
#     1 al 9. Luego imprime:
#     a) La primera fila
#     b) El elemento en la fila 1, columna 2
#     c) La última columna de toda la matriz

# 21. Dada la lista ,original = [1, 2, 3, 4, 5] crea una "copia
#     superficial" usando slicing ([:]). Modifica un elemento
#     en la copia. ¿Se modifica la original? Explica con un
#     comentario.
original = [1, 2, 3, 4, 5]
copia=original
print(copia.pop())
print(copia)
print(original)
# 22. Pide al usuario una frase y conviértela en una lista de
#     palabras usando split(). Luego invierte el orden de las
#     palabras y vuelve a unirlas con join(). Muestra la frase
#     invertida. Ej: "Hola mundo" -> "mundo Hola"
frase=input("Di una frase ")
frase2=frase.split()
print(frase2)
frase2.reverse()
print(frase2)
frase3="".join(frase2)
print(frase3)
frase4=frase3
print(frase3)
# 23. Crea dos listas: estudiantes = ["Ana", "Luis", "Carlos"]
#     y notas = [85, 92, 78]. Combínalas en una lista de listas
#     donde cada sublista sea [nombre, nota]. Usa zip() dentro
#     de list().
estudiantes = ["Ana", "Luis", "Carlos"]
notas = [85, 92, 78]
resultado=zip(notas,estudiantes)
print(list(resultado))