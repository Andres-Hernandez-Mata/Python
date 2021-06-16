"""
Uso: Comparacion 4
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 15 Junio 2021
"""

def es_bool(str):
	if str == "true":
		return True
	elif str == "false":
		return False
	else:
		print('Respuesta incorrcta intenta con "TRUE" o "FALSE" ')
	

tiene_efectivo =  es_bool( input("Tiene efectivo: ").lower() )
tiene_credito  =  es_bool( input("Tiene credito:  ").lower() )

print( tiene_efectivo , type(tiene_efectivo) )
print( tiene_credito  , type(tiene_credito ) )

puede_comprar = tiene_efectivo or tiene_credito
print(puede_comprar)

print()

print( "tiene_efectivo: "  + str(tiene_efectivo) + " or " + "tiene_credito: "  + str(tiene_credito) + " puede_comprar: " + str(puede_comprar) )



