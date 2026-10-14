"""
===========================================
EXCEPCIONES - EJERCICIOS PRÁCTICOS
===========================================
Temas: try/except/else/finally, capturar tipos específicos,
       TypeError, ValueError, ZeroDivisionError, raise, crear
       excepciones personalizadas
===========================================
"""

# -----------------------------------------
# NIVEL BÁSICO (Ejercicios 1-8)
# -----------------------------------------

# 1. try/except básico
# Encierra un código que divida 10 / 0 dentro de try/except para
# capturar ZeroDivisionError y mostrar un mensaje amigable.

# Tu código aquí


# 2. Capturar TypeError
# Pide al usuario que ingrese un número (input()). Convierte a int
# dentro de try/except para capturar ValueError si no es un número
# válido. Muestra "Debes ingresar un número válido".

# Tu código aquí


# 3. Múltiples except
# Crea una función "dividir_seguro" que reciba a y b. Dentro de
# try, retorna a / b. Captura ZeroDivisionError y TypeError por
# separado, mostrando mensajes distintos.

def dividir_seguro(a, b):
    pass

# Tu código aquí


# 4. Bloque else
# Usa try/except/else para intentar convertir a int un string.
# Si no hay error, en el bloque else imprime "Conversión exitosa".

entrada = "123"
# Tu código aquí


# 5. Bloque finally
# Crea un try/except/finally donde intentes abrir un archivo
# "no_existe.txt" con open(). Captura FileNotFoundError.
# En finally, imprime "Bloque finally ejecutado".

# Tu código aquí


# 6. raise básico
# Define una función "validar_edad" que reciba edad (int). Si edad
# es menor a 0 o mayor a 120, lanza un ValueError con el mensaje
# "Edad inválida".

def validar_edad(edad: int):
    pass

# Tu código aquí


# 7. Capturar excepción con alias
# Usa try/except ValueError as e para capturar un error de
# conversión de "abc" a int. Imprime el mensaje del error
# usando el alias.

# Tu código aquí


# 8. try/except anidado
# Escribe código donde dentro de un try externo (división) haya
# otro try interno (conversión a int). El interno captura ValueError,
# el externo ZeroDivisionError.

# Tu código aquí


# -----------------------------------------
# NIVEL MEDIO (Ejercicios 9-17)
# -----------------------------------------

# 9. raise con condicional
# Define una función "raiz_cuadrada" que reciba un número. Si es
# negativo, lanza ValueError("No existe raíz cuadrada de negativos").
# Si no, retorna la raíz.

def raiz_cuadrada(n: float) -> float:
    pass

# Tu código aquí


# 10. Re-lanzar excepción (raise sin argumentos)
# Escribe una función "procesar_dato" que intente convertir a int.
# Si falla, imprime "Error en procesar_dato" y luego re-lanza la
# misma excepción con raise.

def procesar_dato(valor):
    pass

# Tu código aquí


# 11. Crear excepción personalizada
# Define una clase "SaldoInsuficienteError" que herede de Exception.
# Luego, en una función "retirar_dinero(saldo, monto)", si monto > saldo,
# lanza SaldoInsuficienteError("No tienes suficiente saldo").

class SaldoInsuficienteError(Exception):
    pass

def retirar_dinero(saldo: float, monto: float):
    pass

# Tu código aquí


# 12. Excepción personalizada con atributos
# Crea "EdadInvalidaError" que reciba edad y un mensaje.
# Al capturarla, imprime "Edad [edad] inválida: [mensaje]".

class EdadInvalidaError(Exception):
    def __init__(self, edad: int, mensaje: str = "Edad fuera de rango"):
        pass

def verificar_edad(edad: int):
    pass

# Tu código aquí


# 13. else con finally combinados
# Crea una función "leer_numero" que pida un número al usuario,
# lo convierta a int y lo retorne. Usa try/except/else/finally.
# En finally imprime "Operación finalizada".

def leer_numero() -> int:
    pass

# Tu código aquí


# 14. Capturar múltiples excepciones en una línea
# Escribe código que intente acceder a una lista[10] (IndexError)
# y dividir "string" / 2 (TypeError). Captura ambos errores en
# un solo except usando una tupla de excepciones.

# Tu código aquí


# 15. Assert para validación
# Define una función "calcular_descuento" que reciba precio y
# descuento (0-100). Usa assert para verificar que ambos sean
# números positivos y que descuento <= 100.

def calcular_descuento(precio: float, descuento: float) -> float:
    pass

# Tu código aquí


# 16. try con recursos (simulado)
# Define una función "escribir_archivo_seguro" que intente escribir
# "Hola mundo" en "salida.txt". Usa try/except (IOError) y finally
# para cerrar el archivo si fue abierto.

def escribir_archivo_seguro(nombre_archivo: str, contenido: str):
    pass

# Tu código aquí


# 17. Excepción dentro de una función llamada desde otra
# Escribe una función "a" que llame a "b", y "b" lance ValueError.
# Captura el error en "a" y muestra un mensaje.

def a():
    pass

def b():
    pass

# Tu código aquí


# -----------------------------------------
# NIVEL AVANZADO (Ejercicios 18-22)
# -----------------------------------------

# 18. Mini-proyecto: Calculadora resistente a errores
# Crea una función "calculadora_segura" que pida dos números y una
# operación (+, -, *, /). Captura ValueError (entrada no numérica),
# ZeroDivisionError y cualquier otra excepción con Exception.
# Repite hasta que el usuario ingrese "salir".

def calculadora_segura():
    pass

# Descomentar para probar:
# calculadora_segura()


# 19. Mini-proyecto: Validador de entrada con reintentos
# Crea una función "solicitar_entero" que pida un número entero y
# solo retorne cuando se ingrese uno válido. Usa un bucle while
# con try/except. Límite de 3 intentos; si se agotan, lanza
# RuntimeError("Demasiados intentos fallidos").

def solicitar_entero(mensaje: str = "Ingresa un entero: ", intentos_max: int = 3) -> int:
    pass

# Tu código aquí


# 20. Encadenamiento de excepciones (raise ... from)
# Define una función "procesar_archivo" que intente leer un archivo.
# Si hay FileNotFoundError, captúralo y lanza un RuntimeError
# "No se pudo procesar el archivo" usando raise ... from para
# mantener la causa original.

def procesar_archivo(nombre: str):
    pass

# Tu código aquí


# 21. Mini-proyecto: Sistema de autenticación con excepciones
# Define excepciones personalizadas:
#   - UsuarioNoEncontradoError
#   - ContrasenaIncorrectaError
# Crea una función "autenticar(usuarios, usuario, contrasena)"
# donde usuarios es un dict {usuario: contrasena}. Lanza las
# excepciones según corresponda.

class UsuarioNoEncontradoError(Exception):
    pass

class ContrasenaIncorrectaError(Exception):
    pass

def autenticar(usuarios: dict, usuario: str, contrasena: str):
    pass

bd_usuarios = {"admin": "1234", "alumno": "python"}
# Tu código aquí


# 22. Mini-proyecto: Procesador de CSV manual
# Crea una función "procesar_csv" que reciba un string con datos
# CSV (una línea por fila, valores separados por coma). Para cada
# línea, intenta convertir cada valor a float y suma la fila.
# Si una línea tiene datos inválidos (ValueError), la salta y
# registra el error. Al final, imprime cuántas filas se
# procesaron correctamente y cuántas fallaron.

def procesar_csv(datos_csv: str):
    pass

datos = """1,2,3
4,5,6
7,8,x
10,20,30"""

# Tu código aquí
