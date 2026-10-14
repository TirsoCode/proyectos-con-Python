"""
===========================================
MÓDULOS - EJERCICIOS PRÁCTICOS
===========================================
Temas: import, from...import, alias con as, módulos propios,
       math (pi, sqrt, floor, ceil, etc.)
===========================================
"""

# -----------------------------------------
# NIVEL BÁSICO (Ejercicios 1-8)
# -----------------------------------------

# 1. Import básico de math
# Importa el módulo math y usa math.sqrt(25) y math.pi.
# Imprime ambos valores.

import math
# Tu código aquí


# 2. from ... import
# Del módulo math, importa solo sqrt y pi. Úsalos directamente
# sin prefijo "math.".

# Tu código aquí


# 3. Alias con as
# Importa el módulo math con el alias m. Usa m.sqrt y m.pi.

# Tu código aquí


# 4. from con alias
# Del módulo math, importa factorial con el alias fact.
# Calcula el factorial de 5 y 7.

# Tu código aquí


# 5. Usar math.floor y math.ceil
# Importa math y muestra el uso de floor (redondeo hacia abajo)
# y ceil (redondeo hacia arriba) con el número 3.7.

import math
# Tu código aquí


# 6. math.pow vs operador **
# Usa math.pow(2, 10) y compáralo con 2 ** 10.
# ¿Notas la diferencia en el tipo de retorno?

import math
# Tu código aquí


# 7. Importar todo con *
# Del módulo math, importa todo con from math import *.
# Usa sin, cos y tan con el valor pi/4.

# Tu código aquí


# 8. math.radians y math.degrees
# Convierte 180 grados a radianes con math.radians.
# Convierte pi radianes a grados con math.degrees.
# Importa math de la forma que prefieras.

import math
# Tu código aquí


# -----------------------------------------
# NIVEL MEDIO (Ejercicios 9-17)
# -----------------------------------------

# 9. math.hypot
# Usa math.hypot para calcular la hipotenusa de un triángulo
# con catetos 3 y 4. Verifica que da 5.0.

import math
# Tu código aquí


# 10. math.isclose
# Compara 0.1 + 0.2 == 0.3 usando == (verás que da False).
# Luego usa math.isclose(0.1 + 0.2, 0.3) para obtener True.

import math
# Tu código aquí


# 11. math.gcd
# Calcula el máximo común divisor de 48 y 18 usando math.gcd.

import math
# Tu código aquí


# 12. math.log y math.log10
# Calcula el logaritmo natural de 10 (math.log) y
# el logaritmo base 10 de 1000 (math.log10).

import math
# Tu código aquí


# 13. math.comb y math.perm
# Usa math.comb(5, 2) para combinaciones y math.perm(5, 2)
# para permutaciones. ¿Son los valores esperados?

import math
# Tu código aquí


# 14. Módulo random (combinado con math)
# Importa random y math. Genera un número aleatorio entre 0 y 10
# con random.random() * 10, redondéalo con math.floor y
# muéstralo.

import random
import math
# Tu código aquí


# 15. from ... import con alias parcial
# Del módulo random, importa randint como ri y uniform como u.
# Genera un entero aleatorio entre 1 y 6 (dado) y un float
# aleatorio entre 0 y 1.

# Tu código aquí


# 16. Usar módulo datetime
# Importa datetime y obtén la fecha y hora actual con
# datetime.datetime.now(). Muestra solo el año, mes y día.

import datetime
# Tu código aquí


# 17. from datetime import date
# Del módulo datetime, importa date. Crea una fecha con
# date(2025, 12, 25) y muestra el día de la semana con .weekday()
# (lunes=0, domingo=6).

# Tu código aquí


# -----------------------------------------
# NIVEL AVANZADO (Ejercicios 18-22)
# -----------------------------------------

# 18. Mini-proyecto: Estadísticas con math
# Crea una función "estadisticas" que reciba una lista de números
# y retorne un dict con: media, varianza, desviación estándar
# (usa math.sqrt para la desviación).

import math

def estadisticas(numeros: list) -> dict:
    pass

datos = [10, 12, 23, 23, 16, 23, 21, 16]
# Tu código aquí


# 19. Mini-proyecto: Geometría con math
# Crea funciones area_circulo(radio), area_rectangulo(base, altura)
# y area_triangulo(base, altura) usando math.pi donde corresponda.
# Prueba todas.

import math

def area_circulo(radio: float) -> float:
    pass

def area_rectangulo(base: float, altura: float) -> float:
    pass

def area_triangulo(base: float, altura: float) -> float:
    pass

# Tu código aquí


# 20. Módulo propio (simulado)
# Crea un módulo simulado dentro de este archivo: define un
# diccionario "operaciones_matematicas" que contenga funciones
# como "suma", "resta", "multiplica", "divide". Luego impórtalo
# (como si fuera un módulo separado) usando from ... import.
# Como está en el mismo archivo, simula el acceso directo.

# --- operaciones.py (simulado) ---
def suma(a, b):
    pass

def resta(a, b):
    pass

def multiplica(a, b):
    pass

def divide(a, b):
    pass

# --- Uso como si importáramos ---
# Tu código aquí


# 21. Mini-proyecto: Conversor de unidades con math
# Define un módulo (en el mismo archivo) "conversor" con funciones:
#   - grados_a_radianes(grados)
#   - radianes_a_grados(radianes)
#   - km_a_millas(km)  (1 km = 0.621371 millas)
#   - celsius_a_fahrenheit(celsius)
# Usa math donde sea necesario (pi para las conversiones angulares).

import math

def grados_a_radianes(grados: float) -> float:
    pass

def radianes_a_grados(radianes: float) -> float:
    pass

def km_a_millas(km: float) -> float:
    pass

def celsius_a_fahrenheit(celsius: float) -> float:
    pass

# Tu código aquí


# 22. Mini-proyecto: Juego de adivinanza
# Usa random.randint para generar un número secreto entre 1 y 100.
# El usuario tiene que adivinarlo. Pídele números hasta que acierte.
# Usa math.inf para establecer puntuación inicial o simplemente
# cuenta los intentos. Muestra "¡Correcto!" y el número de intentos.

import random
import math

def juego_adivinanza():
    pass

# Descomentar para jugar:
# juego_adivinanza()
