"""
Uso: Google search
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 06 Junio 2021
"""

import os, time, random

try:
    from googlesearch import search
except ImportError:
    os.system('pip install google')
    print('Installing google... Ejecute de nuevo')
    exit()

# to search 
query = input("Búsqueda: ")
print("Buscando...")
time.sleep(2)
selec = random.randint(0,14)
valor = 0
for enlace in search(query, tld="com", num=15, stop=15, pause=5):
    print (enlace)
    if valor == selec:
        print(selec,enlace)
        break
    valor += 1



