"""
Ejercicios de Manejo de Archivos
================================
Temas: open(), read(), write(), append(), with, json (dump/load),
       csv (reader/writer), archivos .txt
"""

import json
import csv
import os
import tempfile

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1
# Crea un archivo "mensaje.txt" y escribe "Hola, mundo!" en él.
# Usa open() en modo escritura ('w').

# Ejercicio 2
# Abre el archivo "mensaje.txt" en modo lectura ('r') y muestra
# su contenido en pantalla.

# Ejercicio 3
# Abre "mensaje.txt" en modo append ('a') y añade la línea
# "Segunda línea" al final. Luego lee y muestra el contenido completo.

# Ejercicio 4
# Escribe 3 líneas en "poema.txt" usando writelines() con una lista
# de strings. Cada string debe terminar en "\n".

# Ejercicio 5
# Lee "poema.txt" línea por línea usando un bucle for e imprime
# cada línea con su número (1, 2, 3...).

# Ejercicio 6
# Usa el bloque with para abrir "datos.txt", escribir los números
# del 1 al 10 (uno por línea) y asegurar que se cierre automáticamente.

# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 7
# Lee "datos.txt" y calcula la suma de todos los números.
# Convierte cada línea a int. Usa with.

# Ejercicio 8
# Crea un diccionario {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
# y guardalo como JSON en "persona.json" usando json.dump().

# Ejercicio 9
# Lee "persona.json" usando json.load() y muestra cada clave y valor
# en formato "clave: valor".

# Ejercicio 10
# Crea un archivo CSV "productos.csv" con las columnas:
# nombre, precio, cantidad
# Escribe 3 productos usando csv.writer().

# Ejercicio 11
# Lee "productos.csv" usando csv.reader() y muestra cada fila
# en formato "Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}".

# Ejercicio 12
# Abre "notas.txt" y escribe 5 líneas. Luego usa seek(0) para
# volver al inicio y lee el contenido de nuevo. Muestra la posición
# después de escribir y después de seek() con tell().

# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 13
# Crea un archivo temporal con tempfile.NamedTemporaryFile y:
# - Escribe "contenido temporal" en él
# - Lee el contenido
# - Muestra la ruta del archivo
# El archivo debe eliminarse al cerrarse.

# Ejercicio 14
# Escribe una función copiar_archivo(origen, destino) que copie
# el contenido de un archivo a otro usando lectura/escritura.
# Si el origen no existe, captura FileNotFoundError.

# Ejercicio 15
# Escribe una función contar_palabras(archivo) que lea un .txt
# y devuelva el número total de palabras (separadas por espacios).

# Ejercicio 16
# Lee "productos.csv" y calcula el valor total del inventario
# (suma de precio * cantidad para cada producto).

# Ejercicio 17
# Añade un cuarto producto a "productos.csv" usando append.
# Lee el archivo completo después para verificar.

# Ejercicio 18
# Escribe un programa que lea "datos.txt", filtre los números
# pares y los guarde en "pares.txt" (uno por línea).

# Ejercicio 19
# Crea una lista de diccionarios con 3 estudiantes (nombre, nota1, nota2).
# Guárdalos como JSON en "estudiantes.json".
# Luego léelos y calcula el promedio de cada estudiante.

# Ejercicio 20
# Lee "estudiantes.json" y modifica la nota1 del segundo estudiante
# a 10. Escribe el resultado de vuelta al archivo.

# Ejercicio 21
# Escribe una función buscar_en_archivo(archivo, palabra) que busque
# una palabra en un archivo de texto y devuelva una lista con los
# números de línea donde aparece (case-insensitive).

# Ejercicio 22
# Combina lectura de archivos y manejo de excepciones:
# - Pide al usuario un nombre de archivo
# - Intenta abrirlo y mostrar su contenido
# - Captura FileNotFoundError, PermissionError, IsADirectoryError
# - Usa finally para imprimir "Operación finalizada"

# Ejercicio 23
# Crea el archivo "agenda.csv" con columnas: nombre, telefono, email
# Escribe 3 contactos. Luego crea una función agregar_contacto(nombre, telefono, email)
# que añada una fila al CSV sin sobrescribir los existentes.

# Ejercicio 24
# Escribe una función fusionar_archivos(lista_archivos, salida) que
# reciba una lista de nombres de archivo, los lea todos y fusione
# su contenido en un solo archivo de salida (cada archivo separado
# por una línea "--- FIN ARCHIVO ---").

# Ejercicio 25
# Crea un gestor de tareas simple con persistencia en JSON.
# Funciones: agregar_tarea(tarea), listar_tareas(), completar_tarea(indice)
# Las tareas se guardan en "tareas.json" como una lista de diccionarios
# con claves: "descripcion", "completada" (bool).
