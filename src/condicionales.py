"""
Uso: Condicionales
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 30 Junio 2021
"""

edad = int(input("Hola, dime tu edad\n"))
if(edad>=18):
    print("Ya eres mayor de edad")
    print("Tu naciste en al anio " + str(2019-edad))
elif (edad < 18 and edad > 0):
    print("Es menor de edad")


