"""Hacer un programa que inicialice una lista de números con valores aleatorios (10
valores), y posterior ordene los elementos de menor a mayor."""

import random

lista = []

for x in range(10):
	aleatorio = random.randint(1,10)
	lista.append(aleatorio)

lista.sort()

print(lista)