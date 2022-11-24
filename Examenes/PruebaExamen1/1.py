def calcularMaxMin():
    lista = []
    usuario = 1

    while usuario != 0:
        usuario = int(
            input("Introduce un número -- (Para terminar introduce 0) -->"))

        if usuario != 0:
            lista.append(usuario)

    maximo = str(max(lista))
    minimo = str(min(lista))

    print("\nEl mayor número de la lista es " + maximo)
    print("El menor número de la lista es " + minimo + "\n")
    
def Login(usuario,contraseña):
    if usuario == "usuario1" and contraseña == "asdasd":
        return True
    else:
        return False
    
def Principal3():
    intentos = 0
    bandera = False
    
    while intentos != 3 and bandera == False:
        print("Tienes " + str(3 - intentos) + " intentos disponibles")
        usuario = input("Introduce el usuario --> ")
        contraseña = input("Introduce la contraseña --> ")
        
        bandera = Login(usuario,contraseña)
        
        if bandera == False:
            intentos += 1
            
    if bandera == True:
        print("Has accedido correctamente")
    else:
        print("No te acuerdas de las credenciales")


def pintaMenu():
    print("Programa Prueba de Python - (Adrián Durán Molero)")
    print("1- Calcular Max Min")
    print("2- Calculo de Tiempo")
    print("3- Login")
    print("4- Diajuliano")
    print("*Introduce cualquier número negativo para finalizar el programa*")
    return int(input("Introduce la opción --> "))


usuario = 0

while usuario >= 0:
    usuario = pintaMenu()

    if usuario < 0:
        print("Saliendo...")
    elif usuario == 1:
        calcularMaxMin()
    elif usuario == 2:
        pass
    elif usuario == 3:
        Principal3()
    elif usuario == 4:
        pass
    else:
        print("La opción introducida no se corresponde con ninguna opción disponble")
