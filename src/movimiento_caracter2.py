"""
Uso: Movimiento de caracter
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 03 Julio 2021
"""

import os, time, sys

direccion = "d"
posicion = -1
cadena = ""
limite_espacios = 0

def mover_caracter(direccion, posicion, limite_espacios):
	if direccion == "d" and posicion < limite_espacios:
		posicion = posicion + 1
	elif direccion == "i" and posicion > 0:
		posicion = posicion - 1
	return posicion


def nueva_cadena(posicion):
	cadena = ""
	for contador in range(0, posicion):
		cadena = cadena + " "
	cadena = cadena + "\U0001f600"
	return cadena


def leer_limite_espacios():
	try:
		limite_espacios = int(input("Total de espacios: "))
	except:
		print("Se esperaban numeros enteros entre el 0 y el 20")
		print("Vuelve a intentar")
		sys.exit()
	return limite_espacios



limite_espacios = leer_limite_espacios()

while direccion != "s":
	posicion = mover_caracter(direccion, posicion, limite_espacios)
	cadena = nueva_cadena(posicion)
	print(cadena)
	direccion = input("Mover, ¿derecha, izquierda, salir? d/i/s : ")



