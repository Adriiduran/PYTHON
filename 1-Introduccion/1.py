"""Pedir al usuario que introduzca 3 números reales, guardarlos en las variables x, y y z, y mostrar por pantalla el resultado de x2 + y - z . Muestra el resultado con 3 decimales."""

import math

x = float(input("Introduzca un número\n"))
y = float(input("Introduzca un número\n"))
z = float(input("Introduzca un número\n"))

print(round(math.pow(x,2)+y-z,3))