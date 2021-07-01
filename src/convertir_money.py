"""
Uso: Calcular y mostrar el equivalente de una cantidad en pesos mexicanos a dólares americanos, dólares canadienses, yenes, rupias, colones, euros, pesetas españolas y marcos alemanes
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 01 Julio 2021
"""

cantidad = 0
dolares = 0
canadiense = 0
yenes = 0
rupia_india = 0 
colon_costarricense = 0
euros = 0
pesetas = 0
alemanes = 0

def validar_cantidad():
  while True:
    try:
      cantidad = int(input("Ingresar una cantidad en pesos mexicanos: "))
      cantidad = int(cantidad)
      return cantidad
    except ValueError:
      print("Favor de ingresar el dato numerico solicitado")

cantidad = validar_cantidad()

dolares = round((0.046*cantidad)/1, 2)

canadiense = round((0.061*cantidad)/1, 2)

yenes = round((4.83*cantidad)/1, 2)

rupia_india = round((3.38*cantidad)/1, 2)

colon_costarricense = round((27.64*cantidad)/1, 2)

euros = round((0.039*cantidad)/1, 2)

pesetas = round((0.000326*cantidad)/1, 2)

alemanes = round((0.027766*cantidad)/1, 2)

lista_conversiones = [['USD', euros, ''],['CAD', canadiense, ''], ['JPY', yenes, ''], ['INR',rupia_india, ''],['CRC',colon_costarricense, ''], ['EUR', euros, ''], ['ESP', pesetas, ''], ['DEM', alemanes, '']]

formato_tabla = """\
+----------------------------+
|---CONVERSIONES DE MEXICO---|
+----------------------------+
| MONDEDA    CANTIDAD        |
|----------------------------|
{}
+----------------------------+\
"""

formato_tabla = (formato_tabla.format('\n'.join("| {:<10} {:<10} {:>4} |".format(*fila)
 for fila in lista_conversiones)))
print(formato_tabla)


