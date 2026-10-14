# ============================================================
# EJERCICIOS: STRINGS, FORMATO, SLICING, MÉTODOS
# ============================================================
# Cada ejercicio tiene instrucciones en comentarios (#).
# Escribe tu código debajo de cada instrucción.
# ============================================================

# ----------------------------------------------------------
# NIVEL FÁCIL (1-5)
# ----------------------------------------------------------

# 1. Crea un string saludo = "Hola, ¿cómo estás?" e imprímelo.
saludo="Hola, ¿cómo estás?"
print(saludo)
# 2. Usa el método upper() para convertir "python" a mayúsculas.
#    Imprime el resultado.
print("python".upper())
# 3. Usa el método lower() para convertir "PYTHON" a minúsculas.
#    Imprime el resultado.
print("PYTHON".lower())
# 4. Toma el string "  Hola mundo  " y usa strip() para eliminar
#    los espacios al inicio y al final. Imprime el resultado.
print( "            Hola mundo    ".strip())
# 5. Usa replace() para reemplazar "gato" por "perro" en el string
#    "El gato saltó". Imprime el resultado.
print("El gato salio".replace("El gato", "El perro"))
# ----------------------------------------------------------
# NIVEL MEDIO (6-15)
# ----------------------------------------------------------

# 6. Usa slicing para obtener:
#    a) Los primeros 3 caracteres de "Python"
#    b) Los últimos 3 caracteres de "Python"
#    c) El string "Python" al revés
print("python"[0:3]) 
print("python"[3:6])
print("python"[::-1])
# 7.Usa el método split() para dividir el string "manzana,pera,plátano"
#    en una lista usando la coma como separador. Imprime la lista.
compra="manzana,pera,platano".split(",")
print(compra)
# 8. Usa el método join() para unir la lista ["rojo", "verde", "azul"]
#    en un string separado por " - ". Imprime el resultado.
colores=["rojo","verde", "azul"]         
colores="-".join(colores)
print(colores)
# 9. Usa f-strings para crear un mensaje: "Me llamo Ana y tengo 25 años"
#    usando las variables nombre = "Ana" y edad = 25.
nombre="ana"
edad=25
print(f"me llamo {nombre} y tengo {edad}")
# 10. Usa .format() para crear: "El producto X cuesta Y euros"
#     con producto = "Portátil" y precio = 799.99.
# 11. Usa el formato con % para crear: "El número PI es 3.1416"
#     usando la variable pi = 3.14159265. Redondea a 4 decimales.
# 12. Encuentra la posición de la primera aparición de "mundo"
#     en "Hola mundo, mundo cruel" usando find(). Imprime el índice.
hola="Hola mundo, mundo cruel".find("mundo")
print(hola)
# 13. Cuenta cuántas veces aparece la letra "a" en "programación"
#     usando count(). Imprime el resultado.
a="programacion".count("a")
print(a)
# 14. Verifica si el string "Python" comienza con "Py" usando
#     startswith() y si termina con "on" usando endswith().
nombre="python".startswith("Py")
hola="python".endswith("on")
print(nombre)
print(hola)
# 15. Usa capitalize() para poner la primera letra en mayúscula
#     en . Luego usa title() para poner
#     en mayúscula la primera letra de cada palabra.
adios="python es divertido"
print(adios.capitalize())
amigo="python es divertido"
print(amigo.title())
# ----------------------------------------------------------
# NIVEL AVANZADO (16-25)
# ----------------------------------------------------------

# 16. Pide al usuario una frase. Muestra:
#     a) La frase en mayúsculas
#     b) La frase en minúsculas
#     c) La frase con la primera 
# letra de cada palabra en mayúscula
frase=input("Di una frase ")
print(frase.lower())
print(frase.capitalize())
print(frase.upper())
print(frase.title())
# 17. Toma el string "programacion" y extrae usando slicing:
#     a) Los caracteres en índices pares
#     b) Los caracteres en índices impares
#     c) Cada 2 caracteres empezando desde el índice 1
print("programacion"[1::2])
print("programacion"[::2])
print("programacion"[1::2])
# 18. Pide al usuario su nombre y apellidos. Muestra las iniciales
#     en mayúsculas separadas por puntos. Ej: "Juan Pérez López" -> "J.P.L."
nombre_apellidos=input("Di tu nombre y apelldios")
print(nombre_apellidos)
# 19. Crea un string multilínea usando triple comillas que contenga
#     un poema o una cita. Luego usa splitlines() para dividirlo
#     en líneas separadas.
print("""El agua corre y canta
,camino hacia la mar
,la brisa la levanta
,la invita a caminar
.El sauce la saluda,
la roca la ve ir,
la tarde queda mudaal
verla sonreír.""".splitlines())

# 20. Verifica si un string es un palíndromo (se lee igual al derecho
#     y al revés). Prueba con: "anilina", "reconocer", "python".
#     Ignora mayúsculas/minúsculas.


# 21. Pide al usuario su correo electrónico y extrae:
#     a) El nombre de usuario (antes del @)
#     b) El dominio (después del @)
#     c) Verifica si contiene "@" usando el operador "in"
correo=input("Di tu correo electronico")

# 22. Usa zfill() para rellenar el número "42" con ceros a la
#     izquierda hasta tener 5 dígitos. Imprime el resultado.

# 23. Dado el string "   espacios   sobrantes   ", usa una combinación
#     de strip() y replace() para eliminar todos los espacios
#     sobrantes y dejar solo un espacio entre palabras.

# 24. Escribe un programa que extraiga el dominio de una URL.
#     Ej: "https://www.python.org/about/" -> "python.org"
#     Usa replace() y strip() para limpiar.

# 25. Crea una tabla formateada con f-strings usando :< :> :^
#     para alinear texto. Muestra:
#     Nombre   Edad   Ciudad
#     Ana      25     Madrid
#     Luis     30     Barcelona
#     Carla    22     Valencia
#     Alinea los nombres a la izquierda, edades al centro
#     y ciudades a la derecha.
