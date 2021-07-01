"""
Uso: Calcular y mostrar la distancia entre 2 puntos si se da como entrada las coordenadas de cada punto
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 01 Julio 2021
"""

import math

x_p1 = 0
y_p1 = 0
x_p2 = 0
y_p2 = 0
operacion = 0

def x_abscisa_uno():
  while True:
    try:
      x_abscisa_primer = int(input("Ingresa la abacisa del punto uno: "))
      x_abscisa_primer = int(x_abscisa_primer)      
      return x_abscisa_primer
    except ValueError:
      print("Favor de ingresar el dato numerico solicitado")

def y_ordenada_uno():
  while True:
    y_ordenada_primer = int(input("Ingresa la ordenada del punto uno: "))
    try:
      y_ordenada_primer = int(y_ordenada_primer)
      return y_ordenada_primer
    except ValueError:
      print("Favor de ingresar el dato numerico solicitado")

def x_abscisa_dos():
  while True:
    x_abscisa_segundo = int(input("Ingresa la abacisa del segundo uno: "))
    try:
      x_abscisa_segundo = int(x_abscisa_segundo)
      return x_abscisa_segundo
    except ValueError:
      print("Favor de ingresar el dato numerico solicitado")

def y_ordenada_dos():
  while True:
    y_abscisa_segundo = int(input("Ingresa la ordenada del segundo uno: "))
    try:
      y_abscisa_segundo = int(y_abscisa_segundo)
      return y_abscisa_segundo
    except ValueError:
      print("Favor de ingresar el dato numerico solicitado")

x_p1 = x_abscisa_uno()
y_p1 = y_ordenada_uno()
x_p2 = x_abscisa_dos()
y_p2 = y_ordenada_dos()

operacion = math.sqrt(abs(((x_p2-x_p1))*(x_p2-x_p1)) + ((y_p2-y_p1)*(y_p2-y_p1)))

print("La distancia entre los dos puntos es de: {:.2f}".format(operacion))



