"""Escribir una función que reciba un número entero positivo y devuelva su factorial."""


def factorial(num):
    if num < 0:
        print("No existe el factorial de un número negativo")

    elif num == 0:
        return 1

    else:
        fact = 1
        while (num > 1):
            fact *= num
            num -= 1
        return fact
    
print(factorial(5))
