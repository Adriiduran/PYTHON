import math

def cuadradoNumero(numero):
    print("El cuadrado del número es: " + str(numero*numero))
    
def raizCuadrada(numero):
    print("La raíz cuadrada del número es: " + str(math.sqrt(numero)))
    
def primo(numero):
    contador = 0
    for i in range(2,numero):
        if numero % i == 0:
            contador += 1
    
    if contador == 1:
        print("El número es primo")
    else:
        print("El número no es primo")

def pintaMenu():
    print("Opción  'c'  o  'C':  mostrar  el  cuadrado  del  número")
    print("Opción 'r' o 'R': mostrar la raíz cuadrada del número (elevar el número a 1/2)")
    print("Opción  'p'  o  'P':  decir  si  el  número  es  primo  o  no")
    print("Opción 's' o 'S': salir del programa")
    return input("Introduce una opción")

numero = int(input("Introduce un número"))

usuario = 'a'

while usuario != 's' and usuario != 'S':
    usuario = pintaMenu()
    
    if usuario == 'c' or usuario == 'C':
        cuadradoNumero(numero)
    elif usuario == 'r' or usuario == 'R':
        raizCuadrada(numero)
    elif usuario == 'p' or usuario == 'P':
        primo(numero)
    elif usuario == 's' or usuario == 'S':
        print("Saliendo...")
    else:
        print("Opción no válida")