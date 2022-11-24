"""Escribir una función que reciba una muestra de números en una lista y devuelva un
diccionario con su media, varianza y desviación típica."""

import math

def estadisticaDiccionario(listaNumeros):
	sumaNumeros = 0

	for i in range(len(listaNumeros)):
		sumaNumeros += i

	media = sumaNumeros/len(listaNumeros)

	sumatorio = 0

	for i in range(len(listaNumeros)):
		sumatorio += pow((i-media),2)

	varianza = sumatorio/(len(listaNumeros)-1)

	desviacionTipica = math.sqrt(varianza)

	diccionario = {"Media":media,"Varianza":varianza,"Desviación Típica":desviacionTipica}

	return diccionario