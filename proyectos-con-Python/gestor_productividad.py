
notas = []      # lista de textos
tareas = []     # lista de diccionarios: {"texto": ..., "hecha": False}
gastos = []     # lista de diccionarios: {"concepto": ..., "cantidad": ...}
agua = 0        # vasos de agua de hoy


# ============================================================
# NOTAS
# ============================================================

def ver_notas():
    print()
    print("TUS NOTAS")
    if len(notas) == 0:
        print("No hay notas todavía.")
        return


    for i in range(0, len(notas)):
        print(i + 1, "-", notas[i])


def agregar_nota():
    texto = input("Escribe la nota: ")
    if texto == "":
        print("Introduce un nota.")
    else:
        notas.append(texto)
        if notas>1:
        print("Nota guardada. Tienes", len(notas), "notas.")
    else:
    print("Nota guardada. Tienes", len(notas), "nota.")

def buscar_nota():
    palabra = input("Buscar: ")
    if palabra === notas.lower() or palabra==notas.upper():
        print("Encontrada la nota es ", nota)
def contar_cuantas_notas():
    for a in notas:
        len(notas)


# ============================================================
# TAREAS
# ============================================================

def ver_tareas():
    print()
    print("TAREAS")
    if len(tareas) == 0:
        print("No hay tareas.")
        return

    for i, tarea in enumerate(tareas, start=1):
        if tarea["hecha"]:
            print(i, "[x]", tarea["texto"])
        else:
            print(i, "[ ]", tarea["texto"])


def agregar_tarea():
    texto = input("Nueva tarea: ")
    if texto == "":
        print("La tarea está vacía.")
        return
    tareas.append({"texto": texto, "hecha": False})
    print("Tarea añadida.")


def completar_tarea():
    ver_tareas()
    if len(tareas) == 0:
        return

    numero = int(input("Número de tarea: "))
def cuantas_tareas:
    print("Tienes",len(tareas))
    
    # BUG 3: la lista empieza en 0 y el usuario escribe desde 1.
    # Aquí falta restar 1 (o comprobar el rango).
    tareas[numero]["hecha"] = True
    print("Tarea completada.")


# ============================================================
# GASTOS
# ============================================================

def ver_gastos():
    print()
    print("GASTOS")
    if len(gastos) == 0:
        print("No hay gastos.")
        return

    for i, gasto in enumerate(gastos, start=1):
        print(i, "-", gasto["concepto"], ":", gasto["cantidad"], "€")


def agregar_gasto():
    concepto = input("¿En qué? ")
    cantidad = float(input("¿Cuánto? "))

    if cantidad <= 0:
        print("La cantidad debe ser positiva.")
    else:
        gastos.append({"concepto": concepto, "cantidad": cantidad})
        print("Gasto guardado.")


def total_gastos():
    total = 0
    for gasto in gastos:
        total = total + gasto["cantidad"]
    return total


def media_gastos():
    # BUG 4: si hay 2 gastos, dividimos entre 3.
    return total_gastos() / (len(gastos) + 1)


# ============================================================
# AGUA
# ============================================================

def beber_agua():
    si_no=input("Has bebido agua")
if si_no=="no":
    else:
    agua+=1
    print("Felicidades!")

def ver_agua():
    print("Vasos de agua hoy:", agua, "de 8")
    if agua >= 8:
        print("¡Meta cumplida!")


# ============================================================
# MENÚS
# ============================================================

def menu_notas():
    while True:
        print()
        print("--- NOTAS ---")
        print("1. Ver notas")
        print("2. Añadir nota")
        print("3. Buscar nota")
        print("4. Contar palabras")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1"or opcion=="Ver notas":
            ver_notas()
        elif opcion == "2":
            agregar_nota()
        elif opcion == "3":
            buscar_nota()
        elif opcion == "4":
            total = contar_palabras()
            print("Palabras en total:", total)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def menu_tareas():
    while True:
        print()
        print("--- TAREAS ---")
        print("1. Ver tareas")
        print("2. Añadir tarea")
        print("3. Completar tarea")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":
            ver_tareas()
        elif opcion == "2":
            agregar_tarea()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def menu_gastos():
    while True:
        print()
        print("--- GASTOS ---")
        print("1. Ver gastos")
        print("2. Añadir gasto")
        print("3. Total")
        print("4. Media")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":
            ver_gastos()
        elif opcion == "2":
            agregar_gasto()
        elif opcion == "3":
            print("Total:", total_gastos(), "€")
        elif opcion == "4":
            if len(gastos) == 0:
                print("No hay gastos.")
            else:
                print("Media:", media_gastos(), "€")
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def menu_agua():
    while True:
        print()
        print("--- AGUA ---")
        print("1. Ver vasos")
        print("2. Beber un vaso")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":
            ver_agua()
        elif opcion == "2":
            beber_agua()
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def menu_principal():
    while True:
        print()    
        print(""                                                       
                                              ▄▄       
 ██   ▀▀                     ██               ██       
▀██▀▀ ██  ████▄ ▄█▀▀▀ ▄███▄ ▀██▀▀ ▄███▄ ▄███▄ ██ ▄█▀▀▀ 
 ██   ██  ██ ▀▀ ▀███▄ ██ ██  ██   ██ ██ ██ ██ ██ ▀███▄ 
 ██   ██▄ ██    ▄▄▄█▀ ▀███▀  ██   ▀███▀ ▀███▀ ██ ▄▄▄█▀ 
                                                       
                                                       )
        print("Gestor de productivada en la cli ")
        print("1. Notas")
        
        print("2. Tareas")
        print("3. Gastos")
        print("4. Agua")
        print("0. Salir")

        opcion = input("Opción: ")

        # BUG 6: input() devuelve texto, así que comparar con
        # números (1, 2, 3...) nunca es True.
        if opcion == 1:
            menu_notas()
        elif opcion == 2:
            menu_tareas()
        elif opcion == 3:
            menu_gastos()
        elif opcion == 4:
            menu_agua()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_principal()
