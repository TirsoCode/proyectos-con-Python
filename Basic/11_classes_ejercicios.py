"""
===========================================
CLASES - EJERCICIOS PRÁCTICOS
===========================================
Temas: class, __init__, self, atributos públicos/privados,
       name mangling (__), métodos de instancia, encapsulamiento
===========================================
"""

# -----------------------------------------
# NIVEL BÁSICO (Ejercicios 1-8)
# -----------------------------------------

# 1. Clase vacía y atributos dinámicos
# Define una clase "Persona" sin ningún método. Crea una instancia
# llamada "p1" y asígnale los atributos nombre="Ana" y edad=25.
# Imprime ambos atributos.

class Persona:
    pass

p1 = Persona()
# Tu código aquí


# 2. Clase con __init__
# Define una clase "Usuario" cuyo __init__ reciba nombre y email,
# y los asigne como atributos de instancia. Crea un usuario y
# muestra sus datos.

class Usuario:
    def __init__(self, nombre: str, email: str):
        pass

# Tu código aquí


# 3. Método de instancia
# Agrega un método "presentarse" a la clase Usuario que retorne
# un string como "Soy [nombre], mi email es [email]".

class Usuario:
    def __init__(self, nombre: str, email: str):
        pass

    def presentarse(self) -> str:
        pass

# Tu código aquí


# 4. Método que modifica atributos
# Define una clase "Contador" con un atributo "valor" inicializado
# en 0. Agrega métodos "incrementar" (suma 1) y "obtener_valor"
# (retorna el valor actual).

class Contador:
    def __init__(self):
        pass

    def incrementar(self):
        pass

    def obtener_valor(self) -> int:
        pass

# Tu código aquí


# 5. Atributos con valores por defecto
# Crea una clase "Producto" con __init__ que reciba nombre y precio,
# y tenga un atributo "cantidad" con valor por defecto 0.
# Agrega un método "mostrar_info" que imprima los datos.

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int = 0):
        pass

    def mostrar_info(self):
        pass

# Tu código aquí


# 6. Método que llama a otro método
# Define una clase "Rectangulo" con base y altura. Agrega un método
# "area" que retorne base * altura, y otro "es_cuadrado" que retorne
# True si base == altura (usando self.area).

class Rectangulo:
    def __init__(self, base: float, altura: float):
        pass

    def area(self) -> float:
        pass

    def es_cuadrado(self) -> bool:
        pass

# Tu código aquí


# 7. Método con validación
# Crea una clase "CuentaBancaria" con titular y saldo (por defecto 0).
# Agrega un método "depositar" que sume al saldo solo si la cantidad
# es positiva. Si no, imprime un mensaje de error.

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        pass

    def depositar(self, cantidad: float):
        pass

# Tu código aquí


# 8. Método que retorna un valor calculado
# Define una clase "Auto" con atributos marca, modelo, año y
# kilometraje (por defecto 0). Agrega un método "edad" que reciba
# el año actual y retorne la antigüedad del auto.

class Auto:
    def __init__(self, marca: str, modelo: str, anno: int, kilometraje: int = 0):
        pass

    def edad(self, anno_actual: int) -> int:
        pass

# Tu código aquí


# -----------------------------------------
# NIVEL MEDIO (Ejercicios 9-17)
# -----------------------------------------

# 9. Atributo privado (convención _)
# Modifica la clase "CuentaBancaria" para que el atributo saldo sea
# "privado" (convención _saldo). Agrega un método getter "obtener_saldo"
# y un método "retirar" que valide que haya fondos suficientes.

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        pass

    def depositar(self, cantidad: float):
        pass

    def retirar(self, cantidad: float) -> bool:
        pass

    def obtener_saldo(self) -> float:
        pass

# Tu código aquí


# 10. Name mangling (__atributo)
# Crea una clase "Secreto" con un atributo "__mensaje" y un método
# "decir" que lo retorne. Fuera de la clase, intenta acceder
# directamente y también mediante name mangling (_Secreto__mensaje).

class Secreto:
    def __init__(self, mensaje: str):
        pass

    def decir(self) -> str:
        pass

# Tu código aquí


# 11. Propiedades (@property)
# Define una clase "Termometro" con un atributo privado __celsius.
# Usa @property para getter y setter de celsius. En el setter,
# valida que la temperatura no sea menor a -273.15 (cero absoluto).

class Termometro:
    def __init__(self, celsius: float = 0.0):
        pass

    @property
    def celsius(self) -> float:
        pass

    @celsius.setter
    def celsius(self, valor: float):
        pass

    @property
    def fahrenheit(self) -> float:
        pass

# Tu código aquí


# 12. Método que usa otro objeto
# Crea una clase "Libro" con titulo, autor y paginas.
# Crea una clase "Biblioteca" que tenga una lista de libros y
# métodos "agregar_libro" y "total_paginas".

class Libro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        pass

class Biblioteca:
    def __init__(self):
        pass

    def agregar_libro(self, libro: Libro):
        pass

    def total_paginas(self) -> int:
        pass

# Tu código aquí


# 13. Representación con __str__
# Agrega un método __str__ a la clase "Libro" que retorne
# "Título: [titulo] - Autor: [autor] ({paginas} págs.)"

class Libro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        pass

    def __str__(self) -> str:
        pass

# Tu código aquí


# 14. Método de clase (@classmethod)
# Define una clase "Persona" con atributos nombre y edad.
# Agrega un classmethod "desde_nacimiento" que reciba nombre y
# año de nacimiento, calcule la edad (suponiendo año actual 2025)
# y retorne una instancia de Persona.

class Persona:
    def __init__(self, nombre: str, edad: int):
        pass

    @classmethod
    def desde_nacimiento(cls, nombre: str, ano_nacimiento: int):
        pass

# Tu código aquí


# 15. Método estático (@staticmethod)
# Agrega un staticmethod "es_mayor_edad" a Persona que reciba
# una edad y retorne True si es >= 18.

class Persona:
    def __init__(self, nombre: str, edad: int):
        pass

    @staticmethod
    def es_mayor_edad(edad: int) -> bool:
        pass

# Tu código aquí


# 16. Clase con atributo de clase
# Define una clase "Empleado" con un atributo de clase "contador"
# inicializado en 0. En __init__, incrementa el contador.
# Agrega un classmethod "total_empleados" que retorne el contador.

class Empleado:
    contador = 0

    def __init__(self, nombre: str):
        pass

    @classmethod
    def total_empleados(cls) -> int:
        pass

# Tu código aquí


# 17. Encapsulamiento completo con getters/setters
# Crea una clase "TarjetaCredito" con titular y __numero (str de 16 dígitos).
# El getter debe mostrar solo los últimos 4 dígitos (ej: "****-****-****-1234").
# El setter debe validar que el número tenga exactamente 16 dígitos.

class TarjetaCredito:
    def __init__(self, titular: str, numero: str):
        pass

    @property
    def numero(self) -> str:
        pass

    @numero.setter
    def numero(self, valor: str):
        pass

# Tu código aquí


# -----------------------------------------
# NIVEL AVANZADO (Ejercicios 18-22)
# -----------------------------------------

# 18. Mini-proyecto: Sistema de inventario
# Crea una clase "Inventario" que gestione productos (usa la clase
# Producto del ejercicio 5). Métodos:
#   - agregar_producto(producto)
#   - buscar_producto(nombre) -> Producto o None
#   - valor_total() -> float (suma de precio * cantidad de cada producto)

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int = 0):
        pass

class Inventario:
    def __init__(self):
        pass

    def agregar_producto(self, producto: Producto):
        pass

    def buscar_producto(self, nombre: str):
        pass

    def valor_total(self) -> float:
        pass

# Tu código aquí


# 19. Clase con operador (__add__)
# Define una clase "Vector2D" con x e y. Implementa __add__ para
# sumar dos vectores (retorna nuevo Vector2D) y __str__ para
# mostrarlo como "(x, y)".

class Vector2D:
    def __init__(self, x: float, y: float):
        pass

    def __add__(self, otro):
        pass

    def __str__(self) -> str:
        pass

# Tu código aquí


# 20. Clase anidada (composición)
# Crea una clase "Motor" con atributos tipo (str) y caballos (int).
# Crea una clase "Coche" que tenga un Motor como atributo y
# un método "info" que muestre los datos del coche y del motor.

class Motor:
    def __init__(self, tipo: str, caballos: int):
        pass

class Coche:
    def __init__(self, marca: str, modelo: str, motor: Motor):
        pass

    def info(self):
        pass

# Tu código aquí


# 21. Mini-proyecto: Banco con múltiples cuentas
# Define una clase "Banco" que contenga varias cuentas (diccionario
# con key = número de cuenta). Métodos:
#   - crear_cuenta(titular, saldo_inicial=0) -> num_cuenta
#   - transferir(origen, destino, monto) -> bool
# Usa la clase CuentaBancaria del ejercicio 9.

import random

class Banco:
    def __init__(self, nombre: str):
        pass

    def _generar_numero(self) -> str:
        pass

    def crear_cuenta(self, titular: str, saldo_inicial: float = 0.0) -> str:
        pass

    def transferir(self, origen: str, destino: str, monto: float) -> bool:
        pass

    def saldo_cuenta(self, numero: str):
        pass

# Tu código aquí


# 22. Mini-proyecto: Simulador de pedidos
# Crea las clases:
#   - "Articulo" con nombre y precio
#   - "Pedido" que contenga una lista de artículos y sus cantidades.
#     Métodos: agregar(articulo, cantidad), total(), __str__.
#     Si se agrega un artículo ya existente, incrementa la cantidad.

class Articulo:
    def __init__(self, nombre: str, precio: float):
        pass

class Pedido:
    def __init__(self):
        pass

    def agregar(self, articulo: Articulo, cantidad: int = 1):
        pass

    def total(self) -> float:
        pass

    def __str__(self) -> str:
        pass

# Tu código aquí
