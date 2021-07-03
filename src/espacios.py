"""
Uso: Agregar espacios a un caracter
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 03 Julio 2021
"""

import os, time, sys

op_usr = " "
pos = 0
lim = int(input("Espacios: "))

os.system("clear")
while op_usr == "d" or op_usr == "i" or " ":
	if op_usr == "d" and pos < lim:
		pos = pos + 1
	elif op_usr == "i" and pos > 0:
		pos = pos - 1
	elif op_usr == "s":
		os.system("clear")
		print("Hasta Pronto!")
		time.sleep(3)
		sys.exit()

	print(" " * pos + "\U0001f600")
	op_usr = input("Avanzar |" + str(lim) + "| ¿Derecha, Izquierda, Salir? d/i/s : ")
	os.system("clear")



