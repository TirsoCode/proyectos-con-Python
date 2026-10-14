"""
EJERCICIOS DE DICCIONARIOS
Temas: diccionarios, keys(), values(), items(), get(), pop(),
update(), fromkeys()
"""

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1
# Crea un diccionario llamado 'persona' con las llaves "nombre", "edad", "ciudad"
# y asígnales los valores "Carlos", 30, "Madrid". Imprime el diccionario.

persona = {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}
# Tu código aquí
print(persona)
# Ejercicio 2
# Dado el diccionario persona del ejercicio anterior, accede al valor de "nombre"
# usando la sintaxis de corchetes e imprímelo.
# Tu código aquí
print(persona["nombre"])
# Ejercicio 3
# Dado el diccionario producto = {"nombre": "Laptop", "precio": 1200, "stock": 10},
# usa el método get() para obtener el precio. Si no existe, devuelve 0.

producto = {"nombre": "Laptop", "precio": 1200, "stock": 10}
# Tu código aquí
print(producto.get("precio"))
# Ejercicio 4
# Agrega una nueva llave "color" con valor "negro" al diccionario producto.
# Luego imprime el diccionario actualizado.

# Tu código aquí
producto.update({"color":"negro"})
print(producto)
# Ejercicio 5
# Dado el diccionario alumno = {"nombre": "Ana", "nota": 8.5, "curso": "Python"},
# modifica la "nota" a 9.0 y luego imprime el diccionario.

alumno = {"nombre": "Ana", "nota": 8.5, "curso": "Python"}
# Tu código aquí
producto["nota"]=[9]
print(producto)
# Ejercicio 6
# Dado el diccionario edades = {"Luis": 25, "Sofía": 30, "Pedro": 22},
# usa keys() para obtener todas las llaves e imprimirlas.

edades = {"Luis": 25, "Sofía": 30, "Pedro": 22}
# Tu código aquí
print(edades.keys())
# Ejercicio 7
# Usando el diccionario edades del ejercicio anterior, usa values() para
# obtener todos los valores e imprimirlos.
print(edades.values())
# Tu código aquí

# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 8
# Usando el diccionario edades, usa items() para recorrerlo con un bucle for
# e imprimir "Nombre: X, Edad: Y" para cada persona.

# Tu código aquí

# Ejercicio 9
# Dado el diccionario inventario = {"manzanas": 10, "peras": 5, "naranjas": 8},
# usa pop() para eliminar "peras" y obtener su valor. Imprime el valor eliminado
# y el diccionario resultante.

inventario = {"manzanas": 10, "peras": 5, "naranjas": 8}
# Tu código aquí
a=inventario.pop("peras")
print(a)
# Ejercicio 10
# Dado el diccionario notas = {"Matemáticas": 7, "Historia": 8, "Ciencias": 9},
# usa update() para agregar las materias {"Lengua": 6, "Arte": 10}.
# Imprime el diccionario actualizado.

notas = {"Matemáticas": 7, "Historia": 8, "Ciencias": 9}
# Tu código aquí
notas.update({"Lengua": 6, "Arte": 10})
print(notas)
# Ejercicio 11
# Usa el método fromkeys() para crear un diccionario a partir de la lista
# vocales = ["a", "e", "i", "o", "u"], donde cada vocal tenga el valor 0.
# Imprime el diccionario resultante.

vocales = ["a", "e", "i", "o", "u"]
# Tu código aquí

# Ejercicio 12
# Dado el diccionario precios = {"pan": 1.5, "leche": 2.0, "huevos": 3.0},
# usa get() para buscar "queso". Si no existe, asigna el valor 2.5.
# Imprime el resultado.

precios = {"pan": 1.5, "leche": 2.0, "huevos": 3.0}
# Tu código aquí
precios.get("queso")
precios.update({"queso":2.5})
print(precios)
# Ejercicio 13
# Recorre el diccionario poblaciones = {"Madrid": 3.2, "Barcelona": 1.6, "Valencia": 0.8}
# y encuentra la ciudad con mayor población usando un bucle.

poblaciones = {"Madrid": 3.2, "Barcelona": 1.6, "Valencia": 0.8}
# Tu código aquí

# Ejercicio 14
# Dado el diccionario calificaciones = {"Ana": [7, 8, 9], "Luis": [6, 7, 8], "Sofía": [9, 9, 10]},
# calcula e imprime el promedio de cada estudiante.

calificaciones = {"Ana": [7, 8, 9], "Luis": [6, 7, 8], "Sofía": [9, 9, 10]}
# Tu código aquí
print("Ana", (7+8+9)/3)
print("luis", (6+7+8)/3)
print("Sofia", (9+9+10)/3)
# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 15
# Escribe una función 'contar_palabras' que reciba una cadena y devuelva un
# diccionario con la frecuencia de cada palabra (sin distinguir mayúsculas).

def contar_palabras(cadena):
    pass

# Tu código aquí (llama a la función con un ejemplo)

# Ejercicio 16
# Dado el diccionario edades, usa pop() para intentar eliminar "Carlos" que no existe.
# Captura la excepción KeyError. Luego usa pop() con un valor por defecto para evitarlo.

edades_2 = {"Luis": 25, "Sofía": 30}
# Tu código aquí
#edades_2.pop("carlos")
# Ejercicio 17
# Combina dos diccionarios: d1 = {"a": 1, "b": 2} y d2 = {"b": 3, "c": 4}
# de forma que si hay llaves repetidas, se sumen los valores.

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
# Tu código aquí

# Ejercicio 18
# Dado el diccionario edades, crea un nuevo diccionario 'mayores'
# que contenga solo las personas con edad >= 18 usando Dictionary Comprehension.

edades_3 = {"Ana": 17, "Luis": 22, "Sofía": 15, "Carlos": 30}
# Tu código aquí

# Ejercicio 19
# Dado el diccionario de notas, usa el método items() para ordenar los estudiantes
# por calificación de mayor a menor e imprimir el ranking.

notas_2 = {"Ana": 8.5, "Luis": 6.0, "Sofía": 9.5, "Carlos": 7.0}
# Tu código aquí
notas_2.items()
# Ejercicio 20
# Escribe una función 'invertir_diccionario' que reciba un diccionario y devuelva
# uno nuevo donde las llaves sean los valores y los valores sean listas de llaves.

def invertir_diccionario(dic):
    pass

# Tu código aquí (llama a la función con un ejemplo)

# Ejercicio 21
# Crea un diccionario usando fromkeys() con los números del 1 al 5 como llaves
# y una lista vacía como valor para cada una. Luego agrega el número 10 a la
# lista de la llave 3. Verifica que las demás listas no se vean afectadas.

# Tu código aquí

# Ejercicio 22
# Dado el diccionario anidado empresa = {"empleados": {"Juan": {"puesto": "Ingeniero", "salario": 50000},
# "María": {"puesto": "Analista", "salario": 40000}}}, imprime el salario de María.

empresa = {
    "empleados": {
        "Juan": {"puesto": "Ingeniero", "salario": 50000},
        "María": {"puesto": "Analista", "salario": 40000}
    }
}
# Tu código aquí

# Ejercicio 23
# Escribe una función 'fusionar_diccionarios' que reciba dos diccionarios y
# devuelva uno fusionado. Si hay llaves repetidas, el valor del segundo reemplaza al primero.

def fusionar_diccionarios(dic1, dic2):
    pass

# Tu código aquí (llama a la función con un ejemplo)

# Ejercicio 24
# Dado el diccionario stock = {"producto1": {"precio": 10, "cantidad": 100},
# "producto2": {"precio": 25, "cantidad": 50}}, calcula el valor total del inventario.

stock = {
    "producto1": {"precio": 10, "cantidad": 100},
    "producto2": {"precio": 25, "cantidad": 50}
}
# Tu código aquí

# Ejercicio 25
# Crea un diccionario que mapee cada carácter de una cadena a su código ASCII.
# Usa Dictionary Comprehension y ord().

cadena = "Hola"
# Tu código aquí
