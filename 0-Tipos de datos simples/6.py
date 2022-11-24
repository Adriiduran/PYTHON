"""6 - Escribir una función que reciba una muestra de números en una lista y devuelva su
media."""

def media(listaNumeros):
	sumatorio = 0

	for i in range(len(listaNumeros)):
		sumatorio+=listaNumeros[i]

	return sumatorio/len(listaNumeros)