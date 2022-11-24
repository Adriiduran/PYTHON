"""Escribir una función que convierta un número decimal en binario y otra que
convierta un número binario en decimal."""

def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"

    binario = ""

    while decimal > 0:

        residuo = int(decimal % 2)

        decimal = int(decimal / 2)

        binario = str(residuo) + binario

    return binario

def binario_a_decimal(binario):
	posicion = 0
    decimal = 0

    binario = binario[::-1]

    for digito in binario:

        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion ++

    return decimal