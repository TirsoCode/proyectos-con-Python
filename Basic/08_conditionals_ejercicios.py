"""
EJERCICIOS DE CONDICIONALES
Temas: if/elif/else, operadores de comparación encadenados, truthiness
"""

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1
# Declara una variable edad = 18. Usa un if para imprimir "Eres mayor de edad"
# si edad es mayor o igual a 18.

edad = 18
# Tu código aquí
if edad>18 or edad==18:
    print("Eres mayor de edad")

# Ejercicio 2
# Declara una variable numero = 7. Usa if/else para imprimir "Par" si el número
# es par, o "Impar" si es impar.

numero = 7
# Tu código aquí
if numero % 2 == 0:
    print("es par")
else:
    print("es impar")
# Ejercicio 3
# Declara una variable temperatura = 30. Usa if/elif/else para imprimir:
# "Hace calor" si temp > 25, "Temperatura agradable" si temp entre 15 y 25,
# "Hace frío" si temp < 15 

temperatura = 30
# Tu código aquí
if temperatura > 25:
    print("hace calor")
elif temperatura < 15 and temperatura > 15:
    print("Temperatura agradable")
elif temperatura < 15:
    print("hace frio")
# Ejercicio 
# Declara una variable nota = 85. Usa if/elif/else para asignar una calificación:
# >= 90: "Excelente", >= 70: "Aprobado", >= 50: "Suficiente", < 50: "Reprobado".

nota = 85
# Tu código aquí
if nota >=90:
    print("excelente")
elif nota >= 70:
    print("Aprobado")
elif nota >= 50:
    print("suficiente")
elif nota < 50:
    print("reprobado")


# Usa un operador de comparación encadenado para verificar si el valorsss
# x = 10 está entre 5 y 20 (inclusive). Imprime el resultado.

x = 10
# Tu código aquí
if x > 5 and x < 20:
    print("si")

# Ejercicio 6
# Declara una variable password = "python123". Usa if para verificar si la
# longitud de password es mayor o igual a 8 caracteres. Si es así, imprime
# contarseña segura.

password = "python123"
# Tu código aquí
if  len(password) > 7:
    print("contarseña segura")
# Ejercicio 7
# Declara una variable usuario = "" (cadena vacía). Usa un if para verificar
# si usuario es truthy o falsy. Imprime "Usuario válido" o "Usuario inválido".

usuario = ""
# Tu código aquí
if usuario=="":
    print("Usuario inválido")
else:
    print("Usuario válido")

# ============================================================
# NIVEL MEDIO
# ============================================================

# Tu código aquí
# Ejercicio 9
# Declara un año = 2024. Determina si es bisiesto usando condicionales.
# Un año es bisiesto si es divisible por 4, pero no por 100, a menos que
# también sea divisible por 400.

anio = 2024
# Tu código aquí
if anio % 4 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")
# Ejercicio 10
# Declara una variable character = "a". Usa condicionales para determinar si
# es una vocal (a, e, i, o, u) o una consonante. Asume que es una letra.
character = "a"
vocales = "aeiou"
# Tu código aquí
if character in vocales:
    print("es vocal")
else:
    print("no es vocal")
# Ejercicio 11
# Declara una lista numeros = [1, 2, 3, 4, 5]. Usa un if para verificar si
# la lista tiene elementos (es truthy). Si tiene, imprime su longitud.

numeros_lista = [1, 2, 3, 4, 5]
# Tu código aquí
if len(numeros_lista)==0:
    print("no tiene elementos")
else:
    print("si tiene elementos")
    print(len(numeros_lista))
# Ejercicio 12
# Declara una variable calificacion = 75. Usa un operador ternario para asignar
# el texto "Aprobado" si calificacion >= 60, o "Reprobado" en caso contrario.

calificacion = 75
# Tu código aquí
# print(resultado)
if calificacion>=60:
    print("aprobado")
else:
    print("reporbado")
# Ejercicio 13

# Declara tres longitudes de lados de un triángulo: lado1, lado2, lado3.
# Determina si el triángulo es equilátero (3 lados iguales), isósceles (2 iguales)
# o escaleno (todos diferentes).

lado1, lado2, lado3 = 5, 5, 8
# Tu código aquí
if lado1==lado2 and lado2==3:
    print("equilatero")
elif lado1 or lado2 ==lado3:
    print("isosceles")
else:
    print("escaleno")
# Ejercicio 14
# Declara una variable dia = 3. Usa match/case (Python 3.10+) o if/elif
# para imprimir el nombre del día correspondiente (1 = lunes, ..., 7 = domingo).

dia = 3
# Tu código aquí
match dia:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("miercoles")
    case 4:
        print("jueves")
    case 5:
        print("viernes")
    case 6:
        print("sabado")
    case 7:
        print("domingo")

# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 15
# Declara ingresos = 45000 y deudas = 10000. Usa condicionales para simular
# una aprobación de crédito: se aprueba si ingresos >= 30000 Y deudas < 5000,
# o si ingresos  50000 Y deudas < 15000. Si no, se rechaza.

ingresos = 45000
deudas = 10000
# Tu código aquí
if ingresos>=3000 and deudas <500:
    print("Se aprueba")
elif ingresos  >=5000 and deudas<15000:
    print("Aprobado")
else:
    print("Rechazado")
# Ejercicio 16
# Declara una variable valor = 0. Escribe condicionales que muestren cómo
# Python evalúa los siguientes valores como booleanos: 0, None, "" (cadena vacía),
# [] (lista vacía). Imprime "Falsy" o "Truthy" para cada uno.

valor = 0

# Tu código aquí para valor = 0
# Repite para None, "", []
# Tu código aquí para None
# Tu código aquí para ""
# Tu código aquí para []
if valor ==0 or "" or [] or None:
    print("Falsy")
else:
    print("Truthy")

# Ejercicio 17
# Declara una variable letra = "z". Usa condicionales encadenados para verificar
# si es una letra mayúscula, minúscula, o un dígito.

letra = "z"
# Tu código aquí
if letra.islower():
    print("Es una minuscula")
elif letra.isupper():
    print("Es mayuscula")
elif letra.isnumeric():
    print("es un numero")
# Ejercicio 18
# Declara x = 10, y = 10, z = 10. Usa un operador encadenado para verificar
# si los tres son iguales. Imprime "Todos iguales" o "No todos iguales".

x_18, y_18, z_18 = 10, 10, 10
# Tu código aquí
if x_18 ==y_18==z_18:
    print("son iguales")
else:
    print("No son iguales") 
# Ejercicio 19
# Escribe un programa que simule una calculadora básica con dos números
# y un operador (+, -, *, /). Usa if/elif para realizar la operación.
# Si el operador no es válido, imprime "Operador no válido".

num1, num2, operador = 10, 5, "+"
# Tu código aquí
if operador=="+":
    print("Suma")
    print(num1+num2)
# Ejercicio 20
# Declara una variable edad_persona = 20 y tiene_licencia = True.
# Usa una expresión condicional compuesta para determinar si puede conducir:
# mayor de 18 Y tener licencia.

edad_persona = 20
tiene_licencia = True
# Tu código aquí
if edad_persona<=18:
    print("Es mayor de edad")
if tiene_licencia==True:
    print("Tine licencia")
# Ejercicio 21
# Declara una variable puntos = 150 y nivel = "principiante".
# Usa condicionales para determinar el rango:
# puntos >= 200 -> "Avanzado", puntos >= 100 -> "Intermedio", sino "Principiante".
# Si nivel es "principiante" Y puntos >= 100, suma 10 puntos extra.

puntos = 99
nivel = "principiante"
# Tu código aquí
if puntos >=200:
    print("Es avanzado")
elif puntos >=100:
    print("Es intermedio")
elif puntos<100:
    print("Es princicpinate")

if puntos > 100 and nivel=="principiante":
    print("Es principiante")
puntos+=10
print(puntos)

# Ejercicio 22
# Usa condicionales para simular un inicio de sesión.
# usuario_correcto = "admin", password_correcto = "1234".
# Verifica ambos campos e imprime mensajes específicos si el usuario no existe
# o si la contraseña es incorrecta.

usuario_correcto = "admin"
password_correcto = "1234"
usuario_input =input("Ususario: ")
password_input = input("Contraseña: ")
# Tu código aquí
if usuario_input==usuario_correcto and password_correcto==password_input:
    print("contraseña e usuario correcto")
else:
    print("usuario o contraseña incorrecto")
# Ejercicio 23
# Declara una variable hora = 14. Usa condicionales para saludar según la hora:
# 6-12: "Buenos días", 12-18: "Buenas tardes", 18-24: "Buenas noches",
# 0-6: "Es de madrugada".

hora = 14
# Tu código aquí
if hora>=12:
    print("Buenos dias")
elif hora>=18:
    print("Buenoas tardes")
# Ejercicio 24
# Declara una variable monto_compra = 250. Aplica descuentos escalonados:
# >= 500: 20%, >= 300: 15%, >= 100: 10%, sino 0%.
# Calcula e imprime el monto final con descuento.

monto_compra = 250
# Tu código aquí
if monto_compra==500:
    print("Descuento del 25 por ciento")
elif monto_compra==3000:
    print("Descuento del 15 por ciento")
elif monto_compra==100:
    print("Descuento del 10 porciento")
else:
    print("Descuento 0")
# Ejercicio 25

# Declara tres variables a_25, b_25, c_25 con valores numéricos.
# Verifica si pueden formar un triángulo (cada lado debe ser menor que la suma
# de los otros dos). Si es válido, clasifícalo (equilátero, isósceles, escaleno).

a_25, b_25, c_25 = 7, 10, 5
# Tu código aquí
if (a_25 < b_25 + c_25) and (b_25 < a_25 + c_25) and (c_25 < a_25 + b_25):
    print("Puedes formar un triángulo.")
else:
    print("No puedes formar un  triángulo.")
