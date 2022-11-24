"""10. Escribir dos funciones que permitan calcular: 
• La cantidad de segundos en un tiempo dado en horas, minutos y segundos. 
• La cantidad de horas, minutos y segundos de un tiempo dado en segundos. 
Escribe  un  programa  principal  con  un  menú  donde  se  pueda  elegir  la  opción  de 
convertir a segundos, convertir a horas, minutos y segundos o salir del programa."""


def tiempoASegundos(hora, minuto, segundo):
    resultado = 0
    resultado = (hora * 3600) + (minuto * 60) + segundo
    return resultado


def pintaMenu():
    print("MENU DEL PROGRAMA")
    print("----------------------------")
    print("1- Convertir tiempo a segundos")
    print("2- Convertir segundos a tiempo")
    print("3- Salir del programa")
    return int(input("Introduce una opción"))


salir = False
while not salir:
    opcion = pintaMenu()

    if opcion < 1 or opcion > 3:
        print("Opción no válida")

    elif opcion == 1:
        hora = int(input("Introduce las horas"))
        minuto = int(input("Introduce los minutos"))
        segundos = int(input("Introduce los segundos"))
        print("El resultado del tiempo introducido pasado a segundos es = ",
              tiempoASegundos(hora, minuto, segundos))
    elif opcion == 2:
        pass
    else:
        salir = True
        print("Gracias por usar el programa")
