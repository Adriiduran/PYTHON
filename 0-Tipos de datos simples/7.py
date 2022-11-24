"""7 - Escribir una función que reciba una muestra de números en una lista y devuelva
otra lista con sus cuadrados."""

def cuadradoLista(listaNumeros):
	Cuadrados = []
	
	for i in range (len(listaNumeros)):
		Cuadrados.append(pow(listaNumeros[i],2))

	return Cuadrados

lista = [1,2,3]

print(cuadradoLista(lista))