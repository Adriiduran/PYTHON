"""Crea  un  programa  que  calcule  la  potencia  de  un  número  dados  la  base  y  el exponente por el usuario"""

base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))
resultado = 1

for i in range(0,exponente):
    resultado *= base
    
print("El resultado es: " + str(resultado))