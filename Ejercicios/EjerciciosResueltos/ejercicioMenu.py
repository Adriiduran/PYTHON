def pintaMenu():
    print("Menú del programa")
    print("-----------------")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplica")
    print("4. Divide")
    print("0. Salir")
    return int(input("Escoge una opción válida: "))


def sumaNumeros(num1, num2):
    return num1 + num2


def restaNumeros(num1, num2):
    return num1 - num2


def multNumeros(num1, num2):
    return num1 * num2


def divNumeros(num1, num2):
    return num1 / num2


a = int(input("Introduce un primer número"))
b = int(input("Introduce un segundo número"))
opcion = pintaMenu()

while opcion < 0 or opcion > 4:
    print("Opción no válida! Inténtalo de nuevo")
    opcion = pintaMenu()

while opcion >= 0 and opcion < 5:
    if opcion == 1:
        print(sumaNumeros(a, b))
        pintaMenu()
    elif opcion == 2:
        print(restaNumeros(a, b))
        pintaMenu()
    elif opcion == 3:
        print(multNumeros(a, b))
        pintaMenu()
    elif opcion == 4:
        print(divNumeros(a, b))
        pintaMenu()
    else:
        print("Hasta luego!")
        break