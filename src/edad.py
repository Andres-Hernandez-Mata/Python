"""
Uso: Fecha de nacimiento
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 01 Julio 2021
"""

edad = 0
dia = 0
mes = 0

age = 0
day = 0
month = 0

age = int(input("Hola, Ingresa tu edad: "))
while age < 0 or age > 100:
    print("Por favor, Ingresa un valor numerico o mayor que cero")
    age = int(input("Hola, Ingresa tu edad: "))
edad = age

day = int(input("Ingresar el dia de tu compleaños: "))
while day < 0 or day > 31:
    print("Por favor, Ingresa un valor numerico o un dia valido del mes")
    day = int(input("Ingresar el dia de tu compleaños: "))
dia = day

month = int(input("Ingresar el mes de tu compleaños: "))
while month < 0 or month > 12:
    print("Por favor, Ingresa un valor numerico o un mes valido del año")
    month = int(input("Ingresar el mes de tu compleaños: "))
mes = month

print("Fecha de Nacimiento: " + str(dia) + "/" + str(mes) + "/" + str(2019-edad))


