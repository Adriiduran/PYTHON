"""Pide una cadena y un carácter por teclado (valida que sea un carácter) y
muestra cuantas veces aparece el carácter en la cadena"""

cadena = input("Introduce una cadena: ")
caracter= input("Introduce un caracter para comprobar: ")

if len(caracter) == 1:
	contador = 0

	for c in cadena:
		if c == caracter:
			contador = contador + 1;

	print("Se ha encontrado el caracter: " + str(contador) + " veces")
else:
	print("El caracter introducido no es correcto")


