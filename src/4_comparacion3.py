"""
Uso: Comparacion 3
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 15 Junio 2021
"""

def es_bool(str):
    if str == "true":
        return True
    else:
        return False


sabe_manejar   =  es_bool( input("Es conductor: ").lower() )
tiene_licencia =  es_bool( input("Tiene licencia: ").lower() )

print( es_conductor , type(es_conductor)  )
print( tiene_licencia, type(tiene_licencia) )

deberia_manejar = es_conductor and tiene_licencia
print("deberia manejar: " + str(deberia_manejar) )

print()

print( "es_conductor: "  + str(es_conductor) + " and " + "tiene_licencia: "  + str(tiene_licencia) + " deberia_manejar: " + str(deberia_manejar) )



