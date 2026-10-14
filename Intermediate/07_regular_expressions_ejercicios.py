"""
Ejercicios de Expresiones Regulares
====================================
Temas: re.match(), re.search(), re.findall(), re.split(),
       re.sub(), patrones (\d, \w, \s, [a-z], etc.), re.I
"""

import re

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1
# Usa re.match() para verificar si la cadena "Hola mundo" comienza
# con "Hola". Muestra "Coincide" o "No coincide".
cadena = "Hola mundo"

# Ejercicio 2
# Usa re.search() para buscar "Python" en "Aprendiendo Python 3".
# Si lo encuentra, muestra la posición (start, end).
texto = "Aprendiendo Python 3"

# Ejercicio 3
# Usa re.findall() para encontrar todos los dígitos (\d) en
# "Mi código es 1234 y el tuyo es 5678".
numeros = "Mi código es 1234 y el tuyo es 5678"

# Ejercicio 4
# Usa re.findall() para encontrar todas las palabras (\w+) en
# "Hola, ¿cómo estás? Todo bien."
frase = "Hola, ¿cómo estás? Todo bien."

# Ejercicio 5
# Usa re.split() para dividir "manzana,pera;uva naranja" por
# comas, puntos y coma o espacios.
fruta = "manzana,pera;uva naranja"

# Ejercicio 6
# Usa re.sub() para reemplazar todos los dígitos en "abc123def456"
# por "X".
codigo = "abc123def456"

# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 7
# Encuentra todas las palabras que empiezan con "a" (minúscula)
# en "Ana ama a su abuelo Alberto". Usa re.findall() con el
# patrón adecuado y la bandera re.I (ignorar mayúsculas).

# Ejercicio 8
# Extrae todos los correos electrónicos del texto:
# "Contactos: ana@gmail.com, pedro@yahoo.es, info@empresa.org"
# Patrón básico: \w+@\w+\.\w+
emails = "Contactos: ana@gmail.com, pedro@yahoo.es, info@empresa.org"

# Ejercicio 9
# Valida si una cadena es un número de teléfono mexicano:
# formato: +52 1 55 1234 5678 (10 dígitos después de +52)
# Usa re.match() o re.fullmatch().
tel = "+52 55 1234 5678"

# Ejercicio 10
# Usa re.split() para dividir un texto por signos de puntuación
# (.,;:!¿?) y obtener solo las palabras.
texto_pun = "Hola, ¿cómo estás? Bien. Yo también; gracias!"

# Ejercicio 11
# Usa re.sub() para censurar números de tarjeta de crédito:
# "Mi tarjeta es 1234-5678-9012-3456" -> "Mi tarjeta es ****-****-****-3456"
# Reemplaza los primeros 12 dígitos (y guiones) por asteriscos.

# Ejercicio 12
# Encuentra todas las fechas en formato DD/MM/AAAA dentro de:
# "Hoy es 15/06/2025, ayer fue 14/06/2025, y nos vemos el 01/07/2025"
# El patrón debe validar que sean 2/2/4 dígitos.

# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 13
# Extrae todas las direcciones URL de un texto.
# Patrón: http:// o https:// seguido de dominio y opcionalmente /ruta
# Texto: "Visita https://python.org o http://ejemplo.com/pagina"
urls = "Visita https://python.org o http://ejemplo.com/pagina"

# Ejercicio 14
# Valida contraseñas seguras con las siguientes reglas:
# - Mínimo 8 caracteres
# - Al menos una mayúscula
# - Al menos una minúscula
# - Al menos un dígito
# - Al menos un carácter especial (@#$%&)
password = "Passw0rd#"

# Ejercicio 15
# Extrae todos los hashtags de un tweet:
# "Aprendiendo #Python con #ejercicios prácticos #2025 #regex"
# Los hashtags son palabras que empiezan con # seguidas de \w+.
tweet = "Aprendiendo #Python con #ejercicios prácticos #2025 #regex"

# Ejercicio 16
# Dado el siguiente HTML, extrae solo el texto dentro de las etiquetas
# <h1> y <p> (sin las etiquetas).
html = "<h1>Título Principal</h1><p>Esto es un párrafo.</p><p>Otro párrafo.</p>"

# Ejercicio 17
# Usa re.sub() para normalizar espacios en blanco: reemplaza
# múltiples espacios, tabs y saltos de línea por un solo espacio.
desordenado = "Esto    tiene\tdemasiados   \nespacios"

# Ejercicio 18
# Escribe una función validar_email(email) que devuelva True si
# el email tiene el formato correcto: nombre@dominio.extension
# donde nombre puede contener \w, ., -, _ y extensión es de 2 a 4 letras.

# Ejercicio 19
# Extrae todos los números (enteros y decimales) de un texto.
# "El precio es 12.50, hay 3 unidades, código 456 y descuento 0.15"
precios = "El precio es 12.50, hay 3 unidades, código 456 y descuento 0.15"

# Ejercicio 20
# Dado un log de servidor: "192.168.1.1 - GET /index.html 200 1234"
# usa re.search() para extraer: IP, método, ruta, código, y bytes
# usando grupos de captura.

# Ejercicio 21
# Escribe una función buscar_patron(patron, texto) que devuelva
# todas las coincidencias con sus posiciones de inicio y fin
# usando re.finditer().

# Ejercicio 22
# Limpia un texto eliminando caracteres especiales (todo lo que
# no sea \w, espacios o signos de puntuación básicos .,;:!?).
sucio = "Hola@#$% Mundo*** 2025!!! [Correo]"

# Ejercicio 23
# Valida un CURP (Clave Única de Registro de Población) mexicana:
# 4 letras + 6 dígitos + 1 letra + 1 dígito + 1 letra + 1 dígito
# Total: 18 caracteres alfanuméricos.
curp = "XAXX010101000"

# Ejercicio 24
# Escribe una función que reciba un texto y reemplace todas las
# vocales acentuadas (á,é,í,ó,ú,ü) por sus equivalentes sin acento
# (a,e,i,o,u,u). Usa re.sub() con un diccionario de reemplazos.

# Ejercicio 25
# Parsea el siguiente log con múltiples líneas y extrae solo las
# líneas que contienen "ERROR" junto con la fecha y hora entre
# corchetes. Formato: [2025-06-15 10:30:45] ERROR: mensaje
log = """[2025-06-15 10:30:45] INFO: Inicio del sistema
[2025-06-15 10:31:00] ERROR: Fallo en conexión BD
[2025-06-15 10:31:15] WARN: Memoria baja
[2025-06-15 10:31:30] ERROR: Timeout en API"""
