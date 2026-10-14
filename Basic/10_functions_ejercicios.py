"""
===========================================
FUNCIONES - EJERCICIOS PRÁCTICOS
===========================================
Temas: def, parámetros posicionales/nominales, valores por defecto,
       return, type hints, *args
===========================================
"""

# -----------------------------------------
# NIVEL BÁSICO (Ejercicios 1-8)
# -----------------------------------------

# 1. Función sin parámetros
# Define una función llamada "saludar" que imprima "¡Hola, mundo!".
# Luego invócala.

def saludar():
    pass

# Invoca aquí

# 2. Función con un parámetro
# Crea una función "presentarse" que reciba un nombre (str) y
# imprima "Hola, me llamo [nombre]". Pruébala con tu nombre.

def presentarse(nombre: str):
    pass

# Pruébala aquí

# 3. Función con return
# Escribe una función "sumar_dos" que reciba un número y retorne
# ese número más 2. Muestra el resultado.

def sumar_dos(numero: int) -> int:
    pass

# Invoca y muestra el resultado aquí

# 4. Función con varios parámetros
# Define una función "area_rectangulo" que reciba base y altura,
# y retorne el área. Pruébala con base=5, altura=3.

def area_rectangulo(base: float, altura: float) -> float:
    pass

# Pruébala aquí

# 5. Parámetros con valores por defecto
# Crea una función "potencia" que reciba base y exponente (por defecto 2).
# Debe retornar base ** exponente. Pruébala con y sin el segundo argumento.

def potencia(base: float, exponente: float = 2) -> float:
    pass

# Pruébala aquí

# 6. Type hints básicos
# Define una función "calcular_imc" que reciba peso (float) y altura (float),
# retorne el IMC (peso / altura**2). Añade type hints a parámetros y retorno.

def calcular_imc(peso: float, altura: float) -> float:
    pass

# Pruébala aquí

# 7. Llamada con argumentos nominales
# Usando la función del ejercicio anterior, invócala usando argumentos
# nominales (keyword arguments) en orden inverso.

# Tu código aquí

# 8. Función que retorna múltiples valores
# Crea una función "dividir" que reciba dividendo y divisor, y retorne
# (cociente, resto). Desempaqueta el resultado al invocarla.

def dividir(dividendo: int, divisor: int):
    pass

# Invoca y desempaqueta aquí

# -----------------------------------------
# NIVEL MEDIO (Ejercicios 9-17)
# -----------------------------------------

# 9. Función que usa *args
# Escribe una función "sumar_todo" que acepte una cantidad variable de
# números (*args) y retorne su suma. Pruébala con 1, 2, 3, 4, 5.

def sumar_todo(*args: int) -> int:
    pass

# Pruébala aquí

# 10. Mezcla de parámetros comunes y *args
# Crea una función "mostrar_mensaje" que reciba un prefijo (str) y
# una cantidad variable de palabras (*args), e imprima el prefijo
# seguido de todas las palabras separadas por espacios.

def mostrar_mensaje(prefijo: str, *palabras: str):
    pass

# Pruébala aquí

# 11. Función con validación
# Define una función "raiz_cuadrada" que reciba un número. Si el número
# es negativo, retorna None. Si no, retorna la raíz cuadrada.

def raiz_cuadrada(numero: float):
    pass

# Pruébala aquí

# 12. Función que recibe otra función
# Crea una función "aplicar" que reciba una función f y un valor x,
# y retorne f(x). Pruébala con una función lambda que duplique.

def aplicar(f, x):
    pass

# Pruébala aquí

# 13. Documentación con docstring
# Escribe una función "factorial" que calcule el factorial de un número
# entero positivo. Incluye un docstring explicativo y type hints.

def factorial(n: int) -> int:
    pass

# Pruébala aquí

# 14. Parámetro booleano para cambiar comportamiento
# Define una función "tabla_multiplicar" que reciba un número y un
# booleano "invertido" (por defecto False). Si invertido es True,
# muestra la tabla del 10 al 1; si no, del 1 al 10.

def tabla_multiplicar(numero: int, invertido: bool = False):
    pass

# Pruébala aquí

# 15. Función con valores por defecto mutables (peligro)
# Crea una función "agregar_elemento" que reciba un elemento y una lista
# (por defecto []). Agrega el elemento a la lista y retórnala.
# Invócala varias veces sin pasar lista y observa el efecto.

def agregar_elemento(elemento, lista=None):
    pass

# Pruébala aquí

# 16. Función anidada
# Escribe una función "crear_multiplicador" que reciba un factor n y
# retorne una función interna que multiplique su argumento por n.

def crear_multiplicador(n: float):
    pass

# Pruébala aquí

# 17. Función con *args y **kwargs
# Define una función "configurar" que reciba *args (etiquetas) y
# **kwargs (pares clave=valor) e imprima ambos.

def configurar(*args, **kwargs):
    pass

# Pruébala aquí

# -----------------------------------------
# NIVEL AVANZADO (Ejercicios 18-22)
# -----------------------------------------

# 18. Mini-proyecto: Calculadora con menú
# Crea una función "calculadora" que muestre un menú (sumar, restar,
# multiplicar, dividir, salir), pida dos números y ejecute la operación
# usando funciones internas. Repite hasta que el usuario elija salir.

def calculadora():
    pass

# Descomentar para probar:
# calculadora()

# 19. Función recursiva
# Escribe una función recursiva "fibonacci" que reciba n y retorne
# el n-ésimo término de la sucesión de Fibonacci (n >= 0).
# fibonacci(0)=0, fibonacci(1)=1, fibonacci(n)=fibonacci(n-1)+fibonacci(n-2)

def fibonacci(n: int) -> int:
    pass

# Pruébala aquí

# 20. Función envolvente (decorador manual)
# Define una función "registrar_tiempo" que reciba una función f,
# y retorne una nueva función que mida el tiempo de ejecución de f
# y lo imprima, además de retornar el resultado de f.

import time

def registrar_tiempo(f):
    pass

def demo_lenta(segundos: float):
    pass

# Aplica registrar_tiempo a demo_lenta y pruébala

# 21. Mini-proyecto: Validador de contraseñas
# Crea una función "validar_contrasena" que reciba una contraseña y
# retorne un dict con:
#   - "valida": bool
#   - "errores": lista de strings
# Reglas: mínimo 8 caracteres, al menos 1 mayúscula, 1 minúscula,
# 1 dígito y 1 carácter especial (!@#$%^&*).

def validar_contrasena(contrasena: str) -> dict:
    pass

# Pruébala aquí

# 22. Función con type hints complejos
# Define una función "procesar_ventas" que reciba una lista de diccionarios
# (cada uno con "producto": str, "cantidad": int, "precio": float) y
# retorne un dict con "total_ingresos": float, "producto_mas_vendido": str.
# Usa type hints con List y Dict (de typing).

from typing import List, Dict

Venta = Dict[str, object]

def procesar_ventas(ventas: List[Venta]) -> Dict[str, object]:
    pass

ventas_ejemplo = [
    {"producto": "Laptop", "cantidad": 3, "precio": 15000.0},
    {"producto": "Mouse", "cantidad": 10, "precio": 250.0},
    {"producto": "Laptop", "cantidad": 2, "precio": 15000.0},
]

# Pruébala aquí
