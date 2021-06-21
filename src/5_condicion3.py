"""
Uso: Condicional 3
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 21 Junio 2021
"""

calificacion = int(input("Calificacion: "))
CALIF_APROBATORIA = 70

if(calificacion > CALIF_APROBATORIA):
	print("Aprobado!")
elif(calificacion == CALIF_APROBATORIA):
	print("Aprobado, justo en el limite de la calificación aprobatoria!")
else:
	print("Reprobado!")
