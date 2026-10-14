# ============================================================
# EJERCICIOS: HOLA MUNDO, COMENTARIOS, type(), TIPOS BÁSICOS
# ============================================================
# Cada ejercicio tiene instrucciones en comentarios (#).
# Escribe tu código debajo de cada instrucción.
# ============================================================

# ----------------------------------------------------------
# NIVEL FÁCIL (1-5)
# ----------------------------------------------------------

# 1. Escribe un programa que imprima "¡Hola, mundo!" en la consola. print("HOLA,MUNDO")
print("HOLA,MUNDO")
# 2. Usa la función type() para mostrar el tipo de la variable
#    mensaje = " es Python genial". Imprime el resultado.
mensaje = " es Python genial"
print(type(mensaje))
# 3. Crea una variable llamada numero con el valor 42 y otra llamada
#    texto con el valor "42". Usa type() para mostrar el tipo de cada una.
numero=42
texto=42
print(type(numero))
print(type(texto))
# 4. Declara una variable decimal con el valor 3.1416. Imprime su valor
#    y su tipo usando type().
numero=3.1416
print(type(numero))
# 5. Crea una variable booleana llamada es_interesante con el valor True.
#    Imprime la variable y su tipo.
es_interesante= True
print (es_interesante)
# ----------------------------------------------------------
# NIVEL MEDIO (6-15)
# ----------------------------------------------------------

# 6. Escribe un programa que sume dos números enteros (10 y 20) e
#    imprima el resultado junto con el tipo de dato del resultado.
print(f"{10+20}  tipo de dato {type(10+20)}")

# 8. Declara tres variables de diferentes tipos (str, int, float).
#    Usa type() para imprimir un mensaje como:
#    "La variable X es de tipo <tipo>".
tirso="hola"
edad=10
dias=1.234
print(f"La variable {tirso} es de tipo {type(tirso)}")
print(f"La variable {edad} es de tipo {type(edad)}")
print(f"La variable {dias} es de tipo {type(dias)}")
# 9. Concatena tres strings: "Hola", " ", "mundo" y guarda el resultado
#    en una variable saludo. Imprime saludo y su tipo.
"Hola"+ " " +"mundo"
hola="Hola"+ " " +"mundo"
print(f"{hola}{type(hola)}")
# 10. Usa print() para mostrar el resultado de dividir 15 entre 4.
#     Luego muestra el tipo del resultado. ¿Qué observas?
print(f"{15/4}{type(15/4)}")

# 11. Suma un entero (5) y un float (2.5). Imprime el resultado y su
#     tipo. ¿Qué tipo prevalece?
print(f"{5+2.5}{type(5+2.5)}")
# 12. Crea una variable nombre con tu nombre y una variable edad con
#     tu edad. Imprime: "Me llamo [nombre] y tengo [edad] años".
#     Usa comas en print() para separar los elemento 
nombre="tirso"
edad=10
print(f"Me llamo {nombre} y tengo {edad} años")
# 13. Multiplica un string por un número entero. Por ejemplo, "Hola "
#     multiplicado por 3. Imprime el resultado.
print("hola "*5)
# 14. Declara una variable resultado = 100. Luego reasígnale el valor
#     "cien". Usa type() para mostrar cómo cambió el tipo.
numero=100
numero="cien"
print(type)
# 15. Crea una variable nulo que no tenga ningún valor (None). Imprime
#     la variable y su tipo.
variable=None
print(f"nombre{type(variable)}")
# ----------------------------------------------------------
# NIVEL AVANZADO (16-22)
# ----------------------------------------------------------

# 16. Escribe un programa que convierta un float (8.7) a int y luego
#     a str. Imprime cada conversión y su tipo. ¿Se pierde información?
print(int(8.7))
print(type(int(8.7)))
print(str(8.7))
print(type(str((8.7))))
# 17. Usa la función bool() para convertir los siguientes valores a
#     booleano: 0, 1, "", "Hola", [], [1, 2]. Imprime cada resultado
#     y explica por qué da True o False (en un comentario).
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("hola"))
print(bool([]))
print(bool([1,2]))
# 18. Escribe un programa que calcule el área de un círculo con radio 5.
#     Usa pi = 3.14159. Imprime el resultado y su tipo.

# 19. Crea un número complejo (2 + 3j) y otro (4 - 1j). Súmalos,
#     réstalos, multiplícalos y divídelos. Imprime cada resultado.
print(2+3j)
print(2-3j)
print(2*3j)
print(2/3j)
# 20. Usa print() con el parámetro sep para imprimir los números
#      separados por " - " en una sola línea.
print("1","2",sep="-")
# 21. Escribe un programa que pida al usuario su año de nacimiento
#     (como input), lo convierta a int, calcule la edad aproximada
#     y la muestre. (Asume año actual = 2026)
año=int(input("cual es tu año de nacimiento "))
print(2026-año)
# 22. Usa type() para verificar qué tipo tiene el resultado de las
#     siguientes operaciones e imprime cada uno
print(type(10 / 3))
print(type(10 // 3))
print(type(10 % 3))
print(type(10 ** 3))
# 23. Crea una variable con un número muy grande () y otra con
#     un número muy pequeño (). Imprime ambos y sus tipos.
numero_grande=10**100

print(numero_grande)
numero_pequeño=10**-100
print(numero_pequeño)
# 24. Intercambia los valores de dos variables (a = 5, b = 10) sin
#     usar una tercera variable temporal. Imprime a y b después.
a=5
b=10
a,b = b, a
print(a,b)
# 25. Escribe un programa que determine si una variable es de tipo
#     str usando type(). Prueba con diferentes valores.
variable="dd"
if type(variable)==str:
    print("es una str")
else:
    print("no es una str")
