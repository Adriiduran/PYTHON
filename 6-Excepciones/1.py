def compruebaConversion():
    try:
        entero = int(input("Introduce un entero para convertirlo"))
    except:
        raise ValueError("Caracter no valido")
    else:
        return entero

salir = False
while not salir:
    try:
        entero = compruebaConversion()
    except ValueError:
        print("Debes introducir un número entero")
    else:
        salir = True
        print(entero)