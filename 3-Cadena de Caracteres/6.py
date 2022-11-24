"""Pide una cadena y dos caracteres por teclado (valida que sea un carácter),
sustituye la aparición del primer carácter en la cadena por el segundo
carácter."""

cadena = input("Introduce una cadena ")

caracter1 = input("Introduce el caracter a sustituir")
caracter2 = input("Introduce el caracter por el que sustituir")

if len(caracter1) > 1 or len(caracter2) > 1:
	print("Los caracteres introducidos no son correctos")
else:
	cadena = cadena.replace(caracter1,caracter2)

	print(cadena)