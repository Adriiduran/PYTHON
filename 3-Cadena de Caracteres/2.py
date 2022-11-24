"""Realizar un programa que compruebe si una cadena leída por teclado
comienza por una subcadena introducida por teclado"""

cadena = input("Introduce una cadena: ")
subCadena = input("Introduce una subcadena: " )

if cadena.startswith(subCadena):
	print("La cadena comienza por la subcadena")
else:
	print("La cadena no comienza por la subcadena")