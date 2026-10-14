# Adivinar el numero
import random

vidas = 1

dificultad = input("¿Qué nivel quieres: Facil, Medio, Dificil? ")

if dificultad == "Facil":
    numero_secreto = random.randint(1, 5)
elif dificultad == "Medio":
    numero_secreto = random.randint(1, 10)
elif dificultad == "Dificil":
    numero_secreto = random.randint(1, 15)

numero_usuario = int(input("¿Cuál es el número que estoy pensando? "))

if numero_usuario == numero_secreto:
    print("¡Acertaste!")
else:
    print("Fallaste")

print("Te quedan", vidas, "vidas")
