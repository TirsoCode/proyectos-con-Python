"""
Ejercicios de Tipos de Error y Manejo de Excepciones
====================================================
Temas: SyntaxError, NameError, IndexError, KeyError, TypeError,
       ValueError, ZeroDivisionError, ImportError, AttributeError,
       ModuleNotFoundError, try/except/else/finally
"""

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1
# Corrige el SyntaxError en la siguiente línea (hay un error de sintaxis).
# Escribe la línea corregida debajo.
print("Hola mundo"

# Ejercicio 2
# El siguiente código lanza un NameError. ¿Por qué? Corrígelo.
# print(mensaje)
# mensaje = "Hola"

# Ejercicio 3
# Dada la lista colores, accede al índice 3 e investiga qué error ocurre.
# Luego corrígelo accediendo a un índice válido.
colores = ["rojo", "verde", "azul"]

# Ejercicio 4
# El siguiente diccionario lanza un KeyError al buscar "edad".
# Corrígelo usando .get() para evitar el error.
persona = {"nombre": "Ana", "ciudad": "Madrid"}

# Ejercicio 5
# ¿Qué TypeError ocurre aquí? Corrígelo convirtiendo los tipos adecuadamente.
resultado = "El número es: " + 42

# Ejercicio 6
# El siguiente código lanza ValueError. Corrígelo manejando la entrada.
numero = int("hola")

# Ejercicio 7
# Corrige el ZeroDivisionError sin modificar los valores originales.
a = 10
b = 0
division = a / b

# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 8
# Usa try/except para capturar un IndexError al acceder a una lista vacía.
# Muestra "Lista vacía" si ocurre el error.
datos = []

# Ejercicio 9
# Usa try/except para capturar un KeyError al acceder a un diccionario.
# Si la clave no existe, imprime "Clave no encontrada".
usuario = {"id": 1, "nombre": "Carlos"}

# Ejercicio 10
# Escribe una función dividir(a, b) que maneje ZeroDivisionError
# y devuelva "No se puede dividir por cero" en ese caso.

# Ejercicio 11
# Captura TypeError cuando intentas sumar un string y un número.
# Muestra "Tipos incompatibles para suma".
def suma(a, b):
    pass  # Escribe aquí

# Ejercicio 12
# Usa try/except/else para intentar convertir un string a entero.
# Si falla captura ValueError, si funciona muestra el número en else.
entrada = "123"

# Ejercicio 13
# Usa try/except/finally para abrir un archivo que no existe.
# Captura FileNotFoundError y en finally imprime "Bloque finally ejecutado".

# Ejercicio 14
# Importa la función inexistente "volar" desde el módulo "aves".
# Captura ImportError y muestra "Módulo o función no encontrada".

# Ejercicio 15
# Captura AttributeError al intentar llamar un método que no existe
# en un objeto string. Muestra "El método no existe".
texto = "Python"

# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 16
# Escribe una función procesar_lista(lista, indice) que maneje:
# - IndexError si el índice está fuera de rango
# - TypeError si lista no es una lista
# Devuelve el valor o un mensaje de error.

# Ejercicio 17
# Crea una función convertir_entero(valor) que intente convertir
# valor a entero. Captura ValueError y TypeError por separado,
# mostrando mensajes distintos para cada uno.

# Ejercicio 18
# Escribe un bucle que intente ejecutar 5 operaciones distintas
# (cada una con un error diferente). Usa un solo try/except
# y con múltiples bloques except captura cada error específico:
# ZeroDivisionError, TypeError, ValueError, IndexError, KeyError.

# Ejercicio 19
# Simula un módulo que no existe (ModuleNotFoundError) al intentar
# importar "modulo_inexistente". Captura el error y muestra
# "Módulo no instalado. Ejecuta: pip install modulo_inexistente".

# Ejercicio 20
# Crea un menú interactivo simple que pida al usuario dos números
# y una operación (sumar, restar, multiplicar, dividir).
# Usa try/except para manejar ValueError (entrada no numérica),
# ZeroDivisionError (división por cero) y cualquier otro error
# con un except genérico.

# Ejercicio 21
# Escribe una función analizar_datos(datos) que reciba una lista
# de números como string ("1", "2", "3a", etc.). Debe convertir
# cada elemento a entero. Los que fallen (ValueError) deben
# omitirse y registrarse en una lista de errores.
# Devuelve un diccionario {"exitosos": [...], "errores": [...]}.

# Ejercicio 22
# Simula el uso de try/except anidados. Dentro de un try externo
# que captura cualquier excepción, ten un try interno que capture
# específicamente ZeroDivisionError. Haz que ocurra primero un
# ZeroDivisionError y luego otro error distinto fuera del bloque
# interno pero dentro del externo.

# Ejercicio 23
# Escribe una función con raise personalizado. Si el usuario pasa
# un número negativo, lanza ValueError con el mensaje
# "No se permiten números negativos". Captúralo al llamar la función.

# Ejercicio 24
# Crea tu propia excepción heredando de Exception llamada
# SaldoInsuficienteError. Luego escribe una función retirar(saldo, monto)
# que lance esa excepción si monto > saldo. Captúrala al llamarla.

# Ejercicio 25
# Escribe un bloque try/except/else/finally completo donde:
# - try: abre un archivo, lee una línea, la convierte a entero
# - except ValueError: muestra "Error de conversión"
# - except FileNotFoundError: muestra "Archivo no encontrado"
# - except Exception: muestra "Error inesperado: {error}"
# - else: muestra "Conversión exitosa: {numero}"
# - finally: cierra el archivo si está abierto (usa un flag)
