"""
Uso: Convertir cierta cantidad de segundos en su equivalente en semanas, días, horas y minutos
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 01 Julio 2021
"""

minutos = 0
dias = 0
semana = 0
segundos = 0
segundos = int(input("Ingresa la cantidad de segundos: "))

semana = (segundos / 604800)
dias = (segundos / 86400)
horas = (segundos / 3600)
minutos = (segundos / 60)

print("Semanas: {:.0f}, Dias: {:.0f}, Horas: {:.5f}, Minutos: {:.5f}".format(semana, dias, horas, minutos))



