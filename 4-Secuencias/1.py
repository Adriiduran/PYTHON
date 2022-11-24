"""Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
y posteriormente muestre en pantalla cada elemento de la lista junto con su
cuadrado y su cubo."""

import random

lista = []

for x in range(10):
	aleatorio = random.randint(1,10)
	lista.append(aleatorio)
	print(str(aleatorio) + " " + str(aleatorio*aleatorio) + " " + str(aleatorio*aleatorio*aleatorio))
