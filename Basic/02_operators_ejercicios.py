# ============================================================
# EJERCICIOS: OPERADORES ARITMÉTICOS, COMPARACIÓN, LÓGICOS
# ============================================================
# Cada ejercicio tiene instrucciones en comentarios (#).
# Escribe tu código debajo de cada instrucción.
# ============================================================

# ----------------------------------------------------------
# NIVEL FÁCIL (1-5)
# ----------------------------------------------------------

# 1. Calcula e imprime el resultado de: 15 + 27
print(15+27)
# 2. Calcula e imprime los resultados de:
#    a) 20 - 8
#    b) 7 * 6
#    c) 81 / 9
print(20-8)
print(7*6)
# 3. Usa el operador ** para calcular 2 elevado a la 10.
#    Imprime el resultado.
print(2**10)
# 4. Usa el operador % (módulo) para calcular el resto de:
#    a) 17 dividido entre 5
#    b) 100 dividido entre 3
print(17%5)
print(100%3)
# 5. Usa el operador // (división entera) para calcular:
#    a) 20 // 6
#    b) 100 // 7
#    Imprime los resultados.
print(20//6)
print(100%7)
# ----------------------------------------------------------
# NIVEL MEDIO (6-15)
# ----------------------------------------------------------

# 6. Escribe comparaciones que devuelvan True o False:
#    a) ¿10 es mayor que 5?
#    b) ¿3 es igual a 3?
#    c) ¿7 es diferente de 8?
#    d) ¿15 es menor o igual que 10?
#    Imprime cada resultado.
print(10>5)
print(3==3)
print(7!=3)
print(15)
# 7. Combina operadores: Calcula (5 + 3) * 2 y 5 + 3 * 2.
#    ¿Son iguales? Explica la diferencia con un comentario.) 
print((5+3)*2)
print((2+5)*2)
# 8. Usa el operador lógico and para verificar si:
#    10 es mayor que 5 Y 20 es menor que 30.
#    Imprime el resultado.
print(10>25)
print(20<30)
# 9. Usa el operador lógico or para verificar si:
#    7 es igual a 5 o 8 es mayor que 3.
#    Imprime el resultado.
print(7==5 or 8>3)
# 10. Usa el operador not para negar la expresión:
#     10 > 5. Imprime el resultado.
print(not 10>5)
# 11. Escribe un programa que verifique si un número (ej: 15) es
#     par o impar usando el operador módulo (%).
print(15%2)
# 12. Crea una variable edad = 20. Verifica si la edad está entre
#     18 y 65 (incluidos) usando operadores de comparación y and.
#     Imprime "Dentro del rango laboral" si se cumple.
edad=20
print(edad>18 and edad<65)
# 13. Escribe expresiones para verificar si un año (ej: 2024) es
#     bisiesto. Un año es bisiesto si es divisible entre 4 pero
#     no entre 100, excepto si es divisible entre 400.
año = 2024
print((año%4==0 and not año%100==0) or (año%400==0))
# 14. Calcula el área de un rectángulo (base * altura) con base = 12
#     y altura = 5. Usa operadores aritméticos.
numero=12
numero2=5
print(numero* numero2)
# 15. Verifica con operadores lógicos si un número (num = 25) es
#     múltiplo de 3 y de 5 a la vez.
num=25
print(num%3==0 and num%5==0)
# ----------------------------------------------------------
# NIVEL AVANZADO (16-23)
# ----------------------------------------------------------

# 16. Escribe un programa que determine si tres longitudes (a, b, c)
#     pueden formar un triángulo. La suma de dos lados debe ser
#     mayor que el tercero para todos los casos.
#     Prueba con: 
a=5
b=7
c=10
suma=a+b+c
if suma>c:
    print("si")
# 17. Calcula el resultado de las siguientes expresiones combinadas
#     y explica el orden de evaluación (con un comentario):
#     a) 10 + 5 * 2 - 8 / 4
#     b) (10 + 5) * 2 - 8 / 4
#     c) 2 ** 3 + 4 * 2

# 18. Pide un número al usuario con input() y determina si es
#     positivo, negativo o cero usando operadores de comparación.
#     Imprime el resultado.
numero1=int(input("Di un numero"))
if numero1>0:
    print("Es un numero positivo")
elif numero1==0:
    print("Es cero")
else:
    print("es un numero negativo")
# 19. Escribe un programa que verifique si un número (ej: 123) es
#     capicúa (se lee igual al revés). Conviértelo a string y
#     usa slicing o comparación de dígitos.
numero=123321

# 20. Crea tres variables a, b, c con valores numéricos. Determina
#     cuál es el mayor de los tres solo con operadores de
#     comparación y operadores lógicos. No uses max().
a=9
b=19
c=393
if a>b and a<c:
    print("es mayor A")
elif b<a and b<c:
    print("el mayor es B")
else:
    print("el mayor es C")
# 21. Verifica con operadores lógicos si un carácter (ej: 'a') es
#     una vocal (a, e, i, o, u). Prueba con varios caracteres.
vocal="d"
if vocal == "a":
    print("es vocal")
elif vocal =="e":
    print("es vocal")
elif vocal=="i":
    print("es vocal")
elif vocal=="o":
    print("es vocal")
elif vocal=="u":
    print("es vocal")
# 22. Calcula el perímetro y el área de un círculo con radio = 7.
#     Usa pi = 3.1416. Redondea los resultados a 2 decimales.

# 23. Escribe un programa que, dados dos números (a=45, b=60),
#     calcule el máximo común divisor (MCD) usando el algoritmo
#     de Euclides y operadores aritméticos (módulo).
