# EJERCICIO 1
def calcularMaxMin():
    print("\n\nCÁLCULO MÁXIMO Y MÍNIMO\n")
    numeros = []  # Lista de numeros introducidor
    introducido = 1  # 1 para que siempre entre la primera vez
    while (introducido != 0):  # mientras no se introduzca 0
        introducido = int(input("Introduce un entero: "))  # pide numero
        if (introducido != 0):
            numeros.append(introducido)  # si no es 0 se añade al array
        else:  # Sino, se acaba el while
            break
    mayor = max(numeros)
    menor = min(numeros)
    return mayor, menor  # Devuelve ámbos valores

# EJERCICIO 2


def TotalSegundos():
    # pido dias, horas, minutos y segundos
    dias = int(input("Introduce los dias: "))
    horas = int(input("Introduce las horas: "))
    minutos = int(input("Introduce los minutos: "))
    segundos = int(input("Introduce los segundos: "))

    dias = dias*24*3600  # Convierte los días a segundos
    horas = horas*3600  # Convierte horas a segundos
    minutos = minutos*60  # Convierte minutos a segundos
    total = dias+horas+minutos+segundos  # calculo total
    return total  # devuelvo total


def TransformarSegundos():
    tiempo = float(input("Introduce el tiempo en segundos: "))
    dias = tiempo // (24 * 3600)  # Saca el entero del día
    tiempo = tiempo % (24 * 3600)  # Saca el resto de lo calculado
    horas = tiempo // 3600  # Saca el entero de las horas
    tiempo = tiempo % 3600  # Saca el resto de lo calculado
    minutos = tiempo // 60  # Saca el entero de los minutos
    tiempo = tiempo % 60  # Saca el resto de lo calculado
    segundos = tiempo
    return dias, horas, minutos, segundos


def calculoTiempo():
    print("\n\nCÁLCULO TIEMPO EN SEGUNDOS\n")
    print("1. Meter días, horas, minutos y segundos")
    print("1. Meter segundos")
    op = int(input("Elige:"))  # Elección del menú
    if (op == 1):
        print("La cantidad dse segundos es %d" %
              TotalSegundos())  # Llama a la función
    elif (op == 2):
        d, h, m, s = TransformarSegundos()
        print("%d:%d:%d:%d" % (d, h, m, s))  # Llama a la función y lo imprime
    else:
        return "Te has equivocado."  # Comprobación de que el menú sea un valor correcto


# EJERCICIO 3
def login():
    usuario = input("Introduce tu usuario:")
    contrasena = input("Introduce tu contraseña: ")
    # Comprueba que los datos introducidos son correctos
    if (usuario == "usuario1" and contrasena == "asdasd"):
        return True
    else:
        return False


def principal3():
    print("\nLOGIN")
    intentos = 3  # Número de intentos
    while (intentos > 0 and True):
        if (login()):
            break  # Si es correcto, se para el bucle
        else:
            intentos = intentos-1  # Se restan los intentos
            print("Intento fallido. Te quedan %d intentos." % intentos)
            if (intentos == 0):
                # Si no quedan intentos se termina el bucle
                print("No te quedan intentos.")
                break

# EJERCICIO 4


def leerFecha():
    fecha = input("Introduce una fecha (formato dd-m-yyyy): ")
    fecha = fecha.split("-", 3)  # Leo la fecha y la divido por -
    # Devuelvo los 3 elementos de la lista
    return int(fecha[0]), int(fecha[1]), int(fecha[2])


def esBisiesto(año):
    if ((año % 4 == 0 and año % 100 != 0) or año % 400 == 0):  # Condición para que sea bisiesto
        return True
    else:
        return False


def diasDelMes(mes, año):
    # No sé hacer switch case así que lo hago así (puede que ni se pueda en python xD)
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        return 31
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        return 30
    else:
        if (esBisiesto(año)):
            return 29
        else:
            return 28


def calcularDiaJuliano():
    print("\n\nCÁLCULO DÍA JULIANO")
    diaJ, mesJ, añoJ = leerFecha()  # Recibo los 3 elementos de leer fecha
    diasTotales = 0
    for i in range(1, mesJ):  # Voy sumando por cada mes la cantidad de días
        diasTotales = diasTotales+diasDelMes(i, añoJ)
    diasTotales = diasTotales+diaJ  # Sumo los días del último mes
    return diasTotales


def menu():
    print("Programa Prueba de Python - Maria Lopez Fernandez")
    opcion = 1
    while (opcion >= 0):
        # muestro menu
        print("Menu del programa")
        print("-----------------")
        print("1. Calcular maximo")
        print("2. Calcular tiempo")
        print("3. Hacer login")
        print("4. Dia juliano")
        print(">0. Salir")
        opcion = int(input("Elige:"))
        if (opcion > 4 or opcion == 0):  # Comprueba que no estás metiendo nada raro
            print("Elección incorrecta.\n")
        elif (opcion < 0):  # Se termina si metes un negativo
            print("Un placer.")
            break
        else:
            if (opcion == 1):
                a, b = calcularMaxMin()  # Recibe los dos valores del return
                print("El mayor es %d y el menor %d." %
                      (a, b))  # Imprime los dos valores
            elif (opcion == 2):
                calculoTiempo()  # Ejecuta la función
            elif (opcion == 3):
                principal3()  # Ejecuta la función
            else:
                # Llama a la función e imprime la cantidad de días
                print("Hay %d días entre la fecha indicada y el 1 de enero." %
                      calcularDiaJuliano())


menu()
