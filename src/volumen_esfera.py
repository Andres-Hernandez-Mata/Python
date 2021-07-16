"""
Uso: Calcular y mostrar el volumen de una esfera
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 16 Julio 2021
"""

import math

radio = 0

def volumen_esfera(radio):
  volumen = 0
  volumen=(4/3)*math.pi*radio**3
  return volumen

radio = int(input("Ingresa el radio de la esfera: "))
print("Volumen de la Esfera: {:.2f}".format(volumen_esfera(radio)))


