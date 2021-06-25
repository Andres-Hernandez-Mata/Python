"""
Uso: Condicional While 1
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 24 Junio 2021
"""


while True:

	calificacion = int(input("Calificacion: "))
	CALIF_APROBATORIA = 70

	if(calificacion >= 0 and calificacion <= 100):
		if(calificacion > CALIF_APROBATORIA):
			print("Aprobado!")
		elif(calificacion == CALIF_APROBATORIA):
			print("Aprobado, justo en el limite de la calificación aprobatoria!")
		else:
			print("Reprobado!")


