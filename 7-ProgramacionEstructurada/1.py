def EscribirCentrado(texto):
    longitud = len(texto)
    espacios = int(40-longitud/2)

    for j in range(0, 4):
        if j == 0 or j == 2:
            for i in range(0, espacios):
                print(" ", end="")

        elif j == 1:
            print(texto)

        else:
            for i in range(0, longitud):
                print("=", end="")


EscribirCentrado("Hola como estas")
