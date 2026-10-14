"""
Ejercicios de Fechas y Tiempos en Python
Modulos: datetime, date, time, timedelta, strftime(), strptime(), timezone
"""

# ============================================================
# NIVEL BÁSICO
# ============================================================

# Ejercicio 1: Obtener fecha actual
# Crea un programa que muestre la fecha actual usando datetime.date.today()
# Ejemplo de salida: "Hoy es: 2025-03-15"

fecha_actual = None  # Tu código aquí
print(f"Hoy es: {fecha_actual}")


# Ejercicio 2: Obtener fecha y hora actual
# Usa datetime.datetime.now() para mostrar la fecha y hora actual completa

fecha_hora_actual = None  # Tu código aquí
print(f"Fecha y hora actual: {fecha_hora_actual}")


# Ejercicio 3: Crear una fecha específica
# Crea un objeto date para el 25 de diciembre de 2024

fecha_navidad = None  # Tu código aquí
print(f"Navidad: {fecha_navidad}")


# Ejercicio 4: Crear una hora específica
# Crea un objeto time para las 14:30:00 (2:30 PM)

hora_especifica = None  # Tu código aquí
print(f"Hora: {hora_especifica}")


# Ejercicio 5: Extraer componentes de una fecha
# Dada la fecha actual, muestra por separado: año, mes, día, día de la semana

hoy = None  # Tu código aquí
# Extrae año, mes, día, dia_semana
print(f"Año: {hoy.year}, Mes: {hoy.month}, Día: {hoy.day}, Día semana: {hoy.weekday()}")


# ============================================================
# NIVEL MEDIO
# ============================================================

# Ejercicio 6: Diferencia entre fechas (timedelta)
# Calcula cuántos días faltan para el próximo Año Nuevo (1 de enero del próximo año)

from datetime import date

hoy = date.today()
proximo_anio_nuevo = None  # Tu código aquí (sugerencia: date(hoy.year + 1, 1, 1))
dias_restantes = None  # Tu código aquí
print(f"Días para Año Nuevo: {dias_restantes.days}")


# Ejercicio 7: Sumar días a una fecha
# Suma 30 días a la fecha actual y muestra la nueva fecha

from datetime import timedelta

hoy = date.today()
treinta_dias_despues = None  # Tu código aquí
print(f"Dentro de 30 días será: {treinta_dias_despues}")


# Ejercicio 8: Formatear fechas con strftime()
# Muestra la fecha actual en formato: "15 de marzo de 2025"

from datetime import datetime

ahora = datetime.now()
fecha_formateada = None  # Tu código aquí (pista: "%d de %B de %Y")
print(fecha_formateada)


# Ejercicio 9: Convertir string a fecha con strptime()
# Convierte el string "25-12-2024" a un objeto datetime

fecha_str = "25-12-2024"
fecha_objeto = None  # Tu código aquí (pista: "%d-%m-%Y")
print(fecha_objeto)


# Ejercicio 10: Edad de una persona
# Calcula la edad de una persona dada su fecha de nacimiento (15/05/1990)

from datetime import date

fecha_nac = date(1990, 5, 15)
hoy = date.today()
edad = None  # Tu código aquí (resta de años, ajusta si no ha cumplido aún)
print(f"Edad: {edad} años")


# Ejercicio 11: Día de la semana en español
# Muestra el día de la semana de una fecha dada en español (lunes, martes, etc.)

from datetime import date

fecha = date(2025, 3, 17)
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
# Obtén el nombre del día usando weekday() y la lista dias_semana
nombre_dia = None  # Tu código aquí
print(f"El {fecha} es {nombre_dia}")


# Ejercicio 12: Primer y último día del mes
# Dado un año y mes, muestra el primer y último día de ese mes

import calendar
from datetime import date

anio = 2025
mes = 2
primer_dia = date(anio, mes, 1)
# Usa calendar.monthrange(anio, mes) para obtener el último día
ultimo_dia = None  # Tu código aquí
print(f"Primer día: {primer_dia}, Último día: {ultimo_dia}")


# Ejercicio 13: Diferencia en horas y minutos
# Calcula la diferencia entre dos horas específicas: 08:30 y 17:45

from datetime import datetime, timedelta

hora1 = datetime(2025, 3, 15, 8, 30)
hora2 = datetime(2025, 3, 15, 17, 45)
diferencia = None  # Tu código aquí
print(f"Diferencia: {diferencia}")


# Ejercicio 14: ¿Es fin de semana?
# Determina si una fecha dada cae en sábado o domingo

from datetime import date

fecha = date(2025, 3, 22)
# Usa weekday() (5=sábado, 6=domingo) o isoweekday()
es_fin_de_semana = None  # Tu código aquí (True o False)
print(f"¿Es fin de semana? {es_fin_de_semana}")


# ============================================================
# NIVEL AVANZADO
# ============================================================

# Ejercicio 15: Zonas horarias (timezone)
# Muestra la hora actual en Nueva York (UTC-5) y Tokio (UTC+9)

from datetime import datetime, timezone, timedelta

hora_utc = datetime.now(timezone.utc)
# Crea timezone para Nueva York (UTC-5) y Tokio (UTC+9)
tz_ny = None  # Tu código aquí (timezone(timedelta(hours=-5)))
tz_tokio = None  # Tu código aquí
hora_ny = hora_utc.astimezone(tz_ny)
hora_tokio = hora_utc.astimezone(tz_tokio)
print(f"Nueva York: {hora_ny.strftime('%H:%M')}")
print(f"Tokio: {hora_tokio.strftime('%H:%M')}")


# Ejercicio 16: Calculadora de edad exacta
# Dada una fecha de nacimiento, calcula años, meses y días exactos

from datetime import date

fecha_nac = date(1990, 5, 15)
hoy = date(2025, 3, 15)

# Calcula años, meses y días exactos (considerando meses con diferentes días)
anios = None  # Tu código aquí
meses = None  # Tu código aquí
dias = None   # Tu código aquí
print(f"Tienes {anios} años, {meses} meses y {dias} días")


# Ejercicio 17: Generador de fechas
# Genera una lista con todas las fechas entre dos fechas dadas

from datetime import date, timedelta

fecha_inicio = date(2025, 1, 1)
fecha_fin = date(2025, 1, 15)

fechas = []  # Tu código aquí (usa un bucle while o for)
print(fechas)


# Ejercicio 18: Formato personalizado de fecha
# Convierte una fecha al formato: "15 de marzo de 2025, 03:45 PM"

from datetime import datetime

ahora = datetime.now()
# Investiga los códigos de formato de strftime para lograr el formato deseado
formato_personalizado = None  # Tu código aquí
print(formato_personalizado)


# Ejercicio 19: Validador de fecha
# Pide al usuario una fecha en formato DD/MM/AAAA y valida si es correcta

fecha_input = "32/13/2025"  # Simula entrada del usuario
try:
    fecha_valida = None  # Tu código aquí con strptime
    print(f"Fecha válida: {fecha_valida}")
except ValueError:
    print("Fecha inválida")


# Ejercicio 20: Diferencia entre dos fechas con timezone
# Calcula la diferencia horaria entre dos eventos en diferentes zonas horarias

from datetime import datetime, timezone, timedelta

evento_ny = datetime(2025, 3, 15, 14, 0, tzinfo=timezone(timedelta(hours=-5)))
evento_londres = datetime(2025, 3, 15, 19, 0, tzinfo=timezone(timedelta(hours=0)))

# Convierte ambos a UTC y calcula la diferencia
diferencia_utc = None  # Tu código aquí
print(f"Diferencia entre eventos: {diferencia_utc}")


# Ejercicio 21: ¿Es bisiesto?
# Determina si un año dado es bisiesto (usa calendar.isleap())

import calendar

anio = 2024
es_bisiesto = None  # Tu código aquí
print(f"{anio} {'es' if es_bisiesto else 'no es'} bisiesto")


# Ejercicio 22: Agenda de cumpleaños
# Crea un programa que almacene cumpleaños (nombre -> fecha) y avise si alguien
# cumple años hoy o en los próximos 7 días

from datetime import date, timedelta

cumpleanios = {
    "Ana": date(1995, 3, 18),
    "Luis": date(1990, 6, 22),
    "Marta": date(1988, 12, 5),
    "Carlos": date(1992, 3, 20),
}

hoy = date.today()
proximos_cumples = []  # Tu código aquí (filtra cumpleaños en los próximos 7 días)
print(f"Cumpleaños próximos: {proximos_cumples}")


# Ejercicio 23: Tiempo transcurrido
# Calcula cuánto tiempo ha pasado desde una fecha/hora específica hasta ahora
# en un formato legible: "X años, Y meses, Z días, H horas, M minutos"

from datetime import datetime

evento = datetime(2020, 1, 1, 0, 0, 0)
ahora = datetime.now()
# Calcula la diferencia y descomponla en años, meses, días, horas, minutos
tiempo_transcurrido = None  # Tu código aquí
print(f"Han pasado: {tiempo_transcurrido}")


# Ejercicio 24: Semana laboral
# Dada una fecha, encuentra el lunes y viernes de esa misma semana

from datetime import date, timedelta

fecha = date(2025, 3, 19)  # Miércoles
# Calcula el lunes (resta días según weekday) y viernes (suma días)
lunes = None   # Tu código aquí
viernes = None # Tu código aquí
print(f"Semana del {lunes} al {viernes}")


# Ejercicio 25: Cronómetro simple
# Usa datetime para medir cuánto tarda un bucle en ejecutarse

from datetime import datetime
import time

inicio = datetime.now()
# Simula trabajo
sum(range(1, 1000000))
fin = datetime.now()

tiempo_ejecucion = None  # Tu código aquí
print(f"El bucle tardó: {tiempo_ejecucion}")
