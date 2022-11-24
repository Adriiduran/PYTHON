def pintaMenu():
    print("\n")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("0. Salir")
def opcion1 (lista):
    num = int(input("Dime un número:"))

    lista.append(num)
def opcion2 (lista):
    num = int(input("Dime un número:"))
    pos = int(input("Dime una posición (empezando por 1):"))
    if pos > len(lista):
        print("Posición incorrecta")
    else:
        lista.insert(pos - 1,num)
def opcion4 (lista):
    if len(lista)>0:
        print("El último elemento es %s y lo borramos." % lista.pop())
    else:
        print("La lista está vacía")
def opcion5 (lista):
    pos = int(input("Dime una posición (empezando por 1):"))
    if pos > len(lista):
        print("Posición incorrecta")
    else:
        print("El elemento es %d y lo borramos." % lista.pop(pos - 1))
def opcion6 (lista):
    num = int(input("Dime un número:"))
    print("El número %d aparece %d veces en la lista." % (num,lista.count(lista)))
def opcion7 (lista):
    num = int(input("Dime un número:"))
    indice_buscar = 0
    print("Posiciones: ")

    for indice in range(0,lista.count(num)):

        indice_buscar = lista.index(num,indice_buscar)
        indice_buscar +=1
        print(indice_buscar," ")

lista = []

opcion = 1

while opcion != 0:

    pintaMenu()

    opcion = int(input("Dime opción:"))

    if opcion == 1:
        opcion1(lista)

    elif opcion == 2:
        opcion2(lista)

    elif opcion == 3:
        print("Longitud de la lista: %d" % len(lista))

    elif opcion == 4:
        opcion4(lista)

    elif opcion == 5:
        opcion5(lista)

    elif opcion == 6:
        opcion6(lista)
   
    elif opcion == 7:
        opcion7(lista)

    elif opcion == 8:

        for num in lista:

            print(num," ")

    elif opcion == 0:

        print("Saliendo...")

    else:
        print("Opción incorrecta")