"""
Uso: API
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 30 Junio 2021
"""

import requests
import json
from datetime import datetime

##Hacemos un request para obtener el reporte actual
## Ver documentacion para su uso https://openweathermap.org/api/one-call-api
page = requests.get ("https://api.openweathermap.org/data/2.5/onecall?lat=25.725536&lon=-100.315157&exclude=minutely,hourly,daily&units=metric&appid=")    #Internamente es un método HTTP GET
print (page.status_code)                                #Status code 200 significa "Ok", 
print ("Page es de tipo:",type(page))
print ("Page content es de tipo:",type(page.content))


input ("Vamos a imprimir el contenido de la página")
print (page.content)

input("parse del contenido de la página a json")
weatherData = json.loads(page.content)
print ("El tipo de dato ahora es:", type(weatherData))

input("Vamos a imprimir el dict")
print (weatherData)


input("las keys del dictionary")
for key in weatherData:
    print (key,":",type(weatherData[key]))

print ("current es de tipo diccionario")

input("Imprimimos el diccionario current")
for elem in weatherData["current"]:
    print (elem,":\t",weatherData["current"][elem],"\t",type(elem))


input ("Como weather es un dict, imprimimos sus valores")
for key in weatherData["current"]["weather"][0]:
    print (key,"\t",weatherData["current"]["weather"][0][key], "\t",type(key))

##!UTC -> GMT -6
##!UNIX -> GMT -6

print ("dt",datetime.utcfromtimestamp(int(weatherData["current"]["dt"])).strftime("%d - %m - %Y %H:%M"))
print ("sunrise", datetime.utcfromtimestamp(int(weatherData["current"]["sunrise"])).strftime("%d-%m-%Y %H:%M:%S"))
print ("sunset",datetime.fromtimestamp(int(weatherData["current"]["sunset"])).strftime("%d-%m-%Y %H:%M:%S"))


