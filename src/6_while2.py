"""
Uso: Condicional While 2
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 25 Junio 2021
"""


while True:

	calificacion = int(input("Calificacion: "))
	CALIF_APROBATORIA = 70

	if(calificacion > CALIF_APROBATORIA and calificacion <= 100):
		print("Aprobado!")
	elif(calificacion == CALIF_APROBATORIA):
		print("Aprobado, justo en el limite de la calificación aprobatoria!")
	elif(calificacion >= 0 and calificacion < CALIF_APROBATORIA):
		print("Reprobado!")
	else:
		print("Hasta pronto!")
		continue


