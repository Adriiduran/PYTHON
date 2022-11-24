"""Suponiendo que hemos introducido una cadena por teclado que representa
una frase (palabras separadas por espacios), realiza un programa que cuente
cuantas palabras tiene."""

cadena = input("Introduce una cadena ")

array = cadena.split(" ")

print("La cadena tiene " + str(len(array)) + " palabras")