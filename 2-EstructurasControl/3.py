"""Hacer  un  programa  llamado  TablaMult.py  que  le  pida  al  usuario  un  número 
entero,  y  calcule  su  tabla  de  multiplicar  (del  0  al  10),  dejando  un  hueco  de  3 
espacios para cada número."""

usuario = int(input("Introduce un número para generar su tabla de multiplicar "))

for i in range(0,11):
    print(str(usuario) + " x " + str(i) + " = " + str(usuario*i))