# ============================================================
# EJERCICIOS: VARIABLES, ASIGNACIÓN, input(), len(), 
#             TIPO DINÁMICO, TYPE HINTS
# ============================================================
# Cada ejercicio tiene instrucciones en comentarios (#).
# Escribe tu código debajo de cada instrucción.
# ============================================================

# ----------------------------------------------------------
# NIVEL FÁCIL (1-5)
# ----------------------------------------------------------

# 1. Crea una variable llamada mensaje con el valor "Aprendiendo Python"
#    e imprímela.
mensaje="Aprendiendo Python"
print(mensaje)
# 2. Crea una variable edad y asígnale un número. Luego imprime:
#    "Tengo X años" usando la variable.
edad=10
print(f"tengo {edad} años")
# 3. Usa input() para preguntar al usuario "¿Cómo te llamas?" y
#    guarda la respuesta en una variable nombre. Luego imprime
#    "Hola, [nombre]".

# 4. Pide al usuario su edad con input(), conviértela a int y
#    luego imprime "El año que viene tendrás X años".

# 5. Crea tres variables en una sola línea: a, b, c = 1, 2, 3.
#    Imprime la suma de las tres.
a=1
b=2
c=3
print(1+2+3)
# ----------------------------------------------------------
# NIVEL MEDIO (6-15)
# ----------------------------------------------------------

# 6. Pide al usuario dos números (con input()), conviértelos a int,
#    súmalos y muestra el resultado.
# 7. Usa len() para mostrar la longitud de las siguientes palabras:
#    "Python", "programación", "Hola mundo".
palabra="Python"
hola="programacion"
print(len(palabra))
print(len(hola))
# 8. Crea una variable texto con el valor "Python es dinámico".
#    Luego reasígnale el valor 42. Imprime la variable y su tipo
#    después de cada asignación para ver el tipo dinámico.
hola="Python es dinámico"
print(type(hola))
hola=42
print(type(hola))
# 9. Pide al usuario una palabra y muestra cuántas letras tiene
#    usando len().
palabra=input("di una palabra")
print(len(palabra))
# 10. Declara una variable con type hint indicando que es str:
#     saludo: str = "Hola". Luego intenta reasignarle un número.
#     ¿Qué ocurre? (Funciona aunque el hint diga otra cosa)
saludo:str=hola
saludo
# 11. Pide al usuario su ciudad y país (dos inputs separados).
#     Luego imprime: "Vives en [ciudad], [país]".
ciudad=input ("Donde vives ")
pais=input ("En que pais vives ")
print("vives en",(ciudad),(pais))
# 13. Intercambia los valores de dos variables x e y usando una
#     variable temporal tmp. x=7, y=14. Imprime antes y después.
x=7
e=14
print(x)
print(e)
e=14
print(e)
x=7
print(x)
# 14. Pide al usuario su nombre completo y muestra cuántos caracteres
#     tiene (incluyendo espacios).
nombre=input("Di tu nombre completo ")
print(len(nombre))
# 15. Crea una variable nota1 = 8.5 y nota2 = 7.3. Calcula el promedio
#     y guárdalo en una variable promedio. Imprime el resultado.s
nota1=8.5
nota2=7.3
divison=nota2+nota1
hola=divison/2
print(hola)
# ----------------------------------------------------------
# NIVEL AVANZADO (16-24)
# ----------------------------------------------------------

# 16. Pide al usuario tres números enteros. Calcula el promedio,
#     la suma y el producto. Muestra todos los resultados.
numero1=int(input("di un numero "))
numero2=int(input("di un numero "))
numero3=int(input("di un numero "))
print("la suma",numero1+numero2+numero3)
print("la multiplicacion",numero1*numero2*numero3)

# 17. Crea una variable frase = "Aprender Python es divertido".
#     Usa len() para calcular cuántos caracteres tiene y muestra
#     la frase centrada en un marco de asteriscos. Por ejemplo:
#     ******************************
#     * Aprender Python es divertido *
#     ******************************
#     (Ajusta los asteriscos según la longitud)
frase = "Aprender Python es divertido"
len(frase)
# 18. Pide al usuario su año de nacimiento y calcula si es mayor de
#     edad (18 años). Asume año actual = 2026. Imprime True o False.
nacimiento=int(input("Cual es tu año de nacimiento "))
años=2026-nacimiento
if años>17:
    print(True)
else:
    print(False)
# 19. Escribe un programa que pida al usuario 4 notas (con input()),
#     las convierta a float, calcule el promedio y muestre si
#     el promedio es mayor o igual a 5.0 (aprobado). Usa una
#     variable booleana aprobado.
nota0=float(input("Di una nota"))
nota1=float(input("Di una nota" ))
nota2=float(input("Di una nota" ))
nota3=float(input("Di una nota" ))
total=nota0+nota1+nota2+nota3
dividio=total/4
if dividio>=5:
    print(True)
else:
    print(False)

# 20. Crea variables con type hints para cada tipo básico:
#     nombre: str, edad: int, altura: float, es_estudiante: bool.
#     Asígnales valores e imprímelos.
nombre:str="Tirso"
edad:int=10
altura:float=1.47
es_estudiante:bool=True
# 21. Pide al usuario una frase y cuenta cuántas vocales (a, e,i, o, u) 
#     tiene, usando len() y count() para cada vocal.
frase=input("Di una frase")
print(frase.count("a""e""i""o""u"))
# 22. Escribe un programa que calcule el índice de masa corporal (IMC)
#     con la fórmula: peso / (altura ** 2). Pide peso (kg) y altura (m)
#     con input(). Muestra el IMC con 2 decimales.
peso=int(input("Di tu peso en kilos"))
altura=float(input("Di tu altura en metros"))
imc= peso / (altura ** 2)
print("Tu IMC es ",peso)
# 23. Crea una variable resultado con el valor 0. Luego asígnale en
#     orden: un string, un float, un booleano y una lista. Después
#     de cada asignación, imprime la variable y su tipo.
resultado=0
resultado="hola"
print(resultado)
print(type(resultado))
resultado=1.45
print(resultado)
print(type(resultado))
print(resultado)
print(type(resultado))
resultado=False
print(resultado)
print(type(resultado))
resultado=["hola,1.45,35"]
print(resultado)
print(type(resultado))
# 24. Escribe un programa que lea 3 palabras con input(), las guarde
#     en variables pal1, pal2, pal3 y muestre cuál tiene más letras
#     (usando len() y comparaciones)
pal1=input("Di una palabra")
pal2=input("Di una palabra")
pal3=input("Di una palabra")
len1=len(pal1)
len2=len(pal2)
len3=len(pal3)
if len1 >= len2 and len1 >= len3:
    print("La palabra con más letras ",pal1)
elif len2 >= len1 and len2 >= len3:
    print("La palabra con más letras es" ,pal2)
else:
    print("La palabra con más letras es",pal3 )