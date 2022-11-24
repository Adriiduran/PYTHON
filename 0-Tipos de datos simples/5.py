"""5 - Escribir una función que calcule el área de un círculo y otra que calcule el volumen
de un cilindro usando la primera función."""

import math

def areaCirculo(radio):
	return pow(radio,2)*math.pi

def volumenCilindro(radio,altura):
	return areaCirculo(radio)*altura
