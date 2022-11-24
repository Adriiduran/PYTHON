"""Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos 
es  múltiplo  del  otro.  Crea  una  función  EsMultiplo  que  reciba  los  dos  números,  y 
devuelve si el primero es múltiplo del segundo."""

def esMultiplo(numero1,numero2):
    if numero1 % numero2 == 0:
        return True
    else:
        return False
    
numero1 = int(input("Introduce el numero 1"))
numero2 = int(input("Introduce el numero 2"))

if esMultiplo(numero1,numero2):
    print(numero1," es multiplo de ", numero2)
else:
    print("No es multiplo")