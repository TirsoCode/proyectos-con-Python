# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)






# Variable de tipo string (texto)
language = "python"

# capitalize()
# Pone la primera letra en mayúscula y el resto en minúsculas.
print(language.capitalize())   # Python

# upper()
# Convierte todo el texto a MAYÚSCULAS.
print(language.upper())        # PYTHON

# count()
# Cuenta cuántas veces aparece un carácter o una palabra.
print(language.count("t"))     # 1

# isnumeric()
# Devuelve True si todos los caracteres son números.
print(language.isnumeric())    # False, porque "python" no son números.

# También podemos probar con un número.
print("1".isnumeric())         # True

# lower()
# Convierte todo el texto a minúsculas.
print(language.lower())        # python

# isupper()
# Comprueba si todas las letras están en mayúsculas.
# Como primero usamos lower(), el resultado será False.
print(language.lower().isupper())  # False

# startswith()
# Comprueba si el texto empieza por "Py".
# Python distingue entre mayúsculas y minúsculas.
print(language.startswith("Py"))   # False

# Comparación de textos.
# "Py" y "py" no son iguales porque Python diferencia
# entre mayúsculas y minúsculas.
print("Py" == "py")           # False
# Variable de tipo string (texto)

# replace()
# Reemplaza una parte del texto por otra.
# Sintaxis: replace("texto_viejo", "texto_nuevo")
print(language.replace("python", "Java"))  # Java

# También podemos reemplazar solo una letra.
print(language.replace("p", "P"))          # Python

# Si el texto que queremos cambiar no existe,
# la cadena permanece igual.
print(language.replace("C++", "Java"))     # python

# Variable de tipo string (texto)
language = "Python"

# Slicing
# Sirve para obtener una parte del texto.
# Sintaxis: texto[inicio:fin]

print(language[0:2])   # Py
# Empieza en la posición 0 y termina antes de la 2.

print(language[2:6])   # thon
# Empieza en la posición 2 y termina antes de la 6.

print(language[:3])    # Pyt
# Desde el principio hasta antes de la posición 3.

print(language[3:])    # hon
# Desde la posición 3 hasta el final.

print(language[-1])    # n
# Último carácter.

print(language[-3:])   # hon
# Los últimos 3 caracteres.

print(language[::2])   # Pto
# Muestra un carácter sí y otro no.