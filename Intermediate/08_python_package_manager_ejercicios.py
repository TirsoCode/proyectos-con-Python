"""
Ejercicios de Gestión de Paquetes en Python
============================================
Temas: pip (install, list, uninstall), importar paquetes
       (numpy, pandas, requests), crear y usar paquetes locales
NOTA: Los imports de paquetes externos están comentados para
evitar errores si no están instalados. Descoméntalos al probar.
"""

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1
# ¿Cuál es el comando pip para instalar un paquete?
# Escribe el comando como comentario.
# Ejemplo: pip install nombre_paquete

# Ejercicio 2
# ¿Cuál es el comando pip para listar todos los paquetes instalados?
# Escribe el comando como comentario.

# Ejercicio 3
# ¿Cuál es el comando pip para desinstalar un paquete?
# Escribe el comando como comentario.

# Ejercicio 4
# ¿Cuál es el comando para mostrar información detallada de un paquete
# instalado (versión, dependencias, autor)?
# Escribe el comando como comentario.

# Ejercicio 5
# ¿Cuál es el comando para congelar las dependencias en un archivo
# requirements.txt?
# Escribe el comando como comentario.

# Ejercicio 6
# ¿Cuál es el comando para instalar todas las dependencias desde
# un archivo requirements.txt?
# Escribe el comando como comentario.

# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 7
# Importa el módulo math (biblioteca estándar, no requiere pip) y
# calcula la raíz cuadrada de 144.
import math

# Ejercicio 8
# Descomenta el siguiente código y usa numpy para crear un array
# con los números del 1 al 10 y calcular su suma.
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(np.sum(arr))

# Ejercicio 9
# Descomenta y usa pandas para crear un DataFrame con 3 columnas:
# "Nombre" (Ana, Luis, Pedro) y "Edad" (25, 30, 28), "Ciudad" (Madrid, Lima, México)
# import pandas as pd
# datos = { ... }
# df = pd.DataFrame(datos)
# print(df)

# Ejercicio 10
# Descomenta y usa requests para hacer una solicitud GET a
# https://api.github.com y mostrar el código de estado.
# import requests
# respuesta = requests.get("https://api.github.com")
# print(respuesta.status_code)

# Ejercicio 11
# Instala el paquete "requests" usando pip (escribe el comando como
# comentario), luego descomenta el código del ejercicio anterior
# y ejecútalo.

# Ejercicio 12
# Crea un archivo "requirements.txt" (como texto) con las siguientes
# dependencias: requests==2.31.0, numpy==1.24.0, pandas==2.0.0
# Luego escribe el comando para instalarlas desde requirements.txt.

# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 13
# Crea un paquete local llamado "utilidades" con la siguiente
# estructura de carpetas (como comentarios):
# utilidades/
#   __init__.py
#   calculos.py
#   textos.py
# Luego escribe cómo importarías una función desde calculos.py.

# Ejercicio 14
# Implementa el paquete local del ejercicio anterior. Dentro de
# utilidades/calculos.py crea una función sumar(a, b) que devuelva
# a + b. Dentro de utilidades/textos.py crea una función
# mayusculas(texto) que devuelva el texto en mayúsculas.
# Luego impórtalas y úsalas.
# (Crea los archivos físicamente en la misma carpeta que este script)

# Ejercicio 15
# Descomenta y usa numpy para crear una matriz de 3x3 con valores
# del 1 al 9. Luego calcula:
# - La transpuesta de la matriz
# - El determinante (si es posible)
# - La suma de todos los elementos
# import numpy as np

# Ejercicio 16
# Descomenta y usa pandas para leer un archivo CSV ("datos.csv")
# que creaste previamente. Muestra las primeras 3 filas, las
# columnas del DataFrame y las estadísticas descriptivas.
# import pandas as pd

# Ejercicio 17
# Usa el módulo datetime (biblioteca estándar) para obtener la
# fecha y hora actual. Luego usa el paquete requests (descomenta)
# para enviar la fecha a un servicio web simulado.
# import requests
# from datetime import datetime

# Ejercicio 18
# Crea un paquete local "mi_paquete" con un submódulo "matematicas"
# que contenga funciones: suma, resta, multiplica, divide.
# Luego crea "utilidades" con una función imprimir_resultado.
# Demuestra cómo se importan y usan desde este script.
# (Crea los archivos necesarios)

# Ejercicio 19
# Descomenta y usa numpy para generar 10 números aleatorios con
# np.random.rand(10). Luego calcula la media, mediana y desviación
# estándar.
# import numpy as np

# Ejercicio 20
# ¿Qué hace el comando "pip freeze"? Escríbelo como comentario.
# Luego simula su salida creando un diccionario Python con nombres
# de paquetes como claves y versiones como valores.
# Ejecuta el comando real (como comentario) para comparar.

# Ejercicio 21
# Descomenta y usa requests para consultar una API de clima
# (o cualquier API pública gratuita). Maneja posibles errores
# de conexión con try/except requests.exceptions.ConnectionError.
# import requests

# Ejercicio 22
# Crea un archivo "setup.py" simulado (como comentario) para
# un paquete llamado "mis_utilidades" con versión 1.0.0,
# descripción breve y dependencias requests y numpy.

# Ejercicio 23
# Descomenta y usa pandas para agrupar datos por columna.
# Crea un DataFrame con ventas (vendedor, producto, monto)
# y calcula el total de ventas por vendedor.
# import pandas as pd

# Ejercicio 24
# Investiga qué es un entorno virtual (virtualenv) y escribe
# los comandos para:
# 1. Crear un entorno virtual llamado "venv"
# 2. Activarlo (según tu sistema operativo)
# 3. Desactivarlo
# Escríbelos como comentarios con explicación breve.

# Ejercicio 25
# Instala un paquete específico con una versión exacta usando pip
# (como comentario). Luego descomenta el código para importarlo
# y usarlo. Finalmente desinstálalo (como comentario).
# Ejemplo con requests versión 2.28.0:
# pip install requests==2.28.0
# import requests
# r = requests.get("https://httpbin.org/get")
# print(r.json())
# pip uninstall requests
