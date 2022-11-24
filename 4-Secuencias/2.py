"""Crea una lista e iníciala con 5 cadenas de caracteres leídas por teclado. Copia los
elementos de la lista en otra lista, pero en orden inverso, y muestra sus elementos
por la pantalla."""

lista = []

for x in range(5):
	lista.append(input("Introduce una cadena de caracteres"))

lista.reverse()
listaReverse = lista[:]

print(listaReverse)