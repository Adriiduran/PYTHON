"""Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza 
dicha  función  en  un  programa  principal  que  lea  el  radio  de  una  circunferencia  y 
muestre su área y perímetro."""

from math import pi


def areaYPerimetro(radio):
    area = pi * (radio**2)
    perimetro = pi * (radio*2)
    return area, perimetro


radio = int(input("Introduzca el radio de una circunferencia"))
area, perimetro = areaYPerimetro(radio)
print("El perimetro de la circunferencia es de" ,perimetro, "y el radio es" ,radio)
