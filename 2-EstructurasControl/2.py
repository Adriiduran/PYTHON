"""Escribir un programa llamado MinMax.py que vaya pidiendo al usuario números  por  teclado,  y  saque  en  cada  iteración  cuál  es  el  mayor  y  el  menor que ha introducido hasta el momento. El programa debe terminar si el usuario escribe 0."""

usuario = 1
max = usuario
min = usuario

while usuario != 0:
    usuario = int(input("Introduce un número: "))
    
    if (usuario > max):
        max = usuario
    elif (usuario < min):
        min = usuario
    elif (usuario == 0):
        print("Saliendo...")
        
    print("El valor max es: " + str(max) + " y el valor min es: " + str(min))