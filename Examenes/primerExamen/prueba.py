#Importa random
import random

def calcularMultiplos():
    numero = -1

    #Bucle que controla que se introduzca un número válido
    while numero <= 0:
        numero = int(input("Introduce un número entero mayor a 0 --> "))

        if numero <= 0:
            print("Debes introducir un número mayor a 0")

    print("CALCULO DE MÚLIPLOS")
    print("-------------------")

    #bucle que va desde el número + 1 hasta 100
    for i in range(numero + 1, 101):
        if i % numero == 0:
            print(i)


def adivinaNumero(numero):
    aleatorio = random.randint(1, 5) #generación de número aleatorio entre (1,5)

    #Se muestran el número introducido por el usuario y el aleatorio generado
    print("Los números que se comprueban son: aleatorio -> " +
          str(aleatorio) + " y el número del usuario -> " + str(numero))

    #Muestra el resultado
    if aleatorio == numero:
        print("Has acertado")
        return True
    else:
        print("No has acertado")
        return False

#Función que engloba el apartado 2
def Principal2():
    intentos = 5
    bandera = False
    
    #bucle que controla los intentos y el acierto del número aleatorio
    while intentos != 0 and bandera == False:
        print("Tienes " + str(intentos) + " intentos disponibles") #Muestra los intentos disponibles
        numeroUsuario = int(input("Introduce un número para comprobar --> "))

        
        if adivinaNumero(numeroUsuario) == True:
            bandera = True #Termina el bucle si se acierta
        else:
            intentos -= 1 #Cada vez que el usuario no acierta resta un intento del contador general


def SexagesimalADecimal():
    #Recepción de datos
    grados = int(input("Introduce los grados --> "))
    minutos = int(input("Introduce los minutos --> "))
    segundos = int(input("Introduce los segundos --> "))

    #Formula para el paso de sexagesimal a decimal
    resultado = grados + (minutos / 60) + (segundos / 3600)

    #Muestra el resultado por pantalla
    print(str(resultado) + "º")
    
    return resultado


def DecimalASexagesimal():
    #Casteamos a tipo float para poder guardar el valor decimal
    decimal = float(input("Introduce los grados decimales --> "))

    #!IMPORTANTE DARLE PRIORIDAD CON LOS PARENTESIS A LAS OPERACIONES¡
    #Para obtener la parte decimal restamos la parte entera al numero decimal completo
    grados = int(decimal)
    auxiliar = (decimal - grados) * 60 #Recoge los minutos tanto con su parte entera como decimal
    minutos = int((decimal - grados) * 60)
    segundos = (auxiliar - minutos) * 60

    print(str(grados) + "º " + str(minutos) + "' " + str(segundos) + "''") #Muestra el resultado

#Función que engloba el apartado 3
def Principal3():
    print("1- Sexagesimal a Decimal")
    print("2- Decimal a Sexagesimal")

    opcion = int(input("Introduce una opción --> "))

    if opcion == 1:
        SexagesimalADecimal()
    elif opcion == 2:
        DecimalASexagesimal()


def leerFecha():
    #Recoge la fecha en el formato esperado
    fecha = input("Introduce una fecha separada por guiones. Ejemplo (23-8-2022) --> ")
    arrayFecha = fecha.split("-") #Divide la cadena por el caracter -

    #Comprobaciones de rangos
    if int(arrayFecha[0]) < 1 or int(arrayFecha[0]) > 31:
        print("El día introducido no es correcto es menor a 1 o mayor a 31")
    elif int(arrayFecha[1]) < 1 or int(arrayFecha[1]) > 12:
        print("El mes introducido no es correcto es menor a 1 o mayor a 12")

    return int(arrayFecha[0]), int(arrayFecha[1]), int(arrayFecha[2])


def esBisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False


def diasDelMes(mes, año):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    elif mes == 2:
        if esBisiesto(año) == False:
            return 28
        else:
            return 29
    else:
        return 30

#Función que engloba el apartado 4
def comprobarFecha():
    #Recoge los resultados obtenidos por la funcion leerFecha()
    dia, mes, año = leerFecha()

    #Recoge el valor max de dias esperados para el mes y el año introducidos por el usuario
    numeroDias = diasDelMes(mes, año)

    #Si el número de días introducido por el usuario es mayor al número de dias totales del mes y del año introducido la fecha es errónea
    if dia > numeroDias:
        print("La fecha introducida no es válida")
    else:
        print("La fecha introducida es válida")

#Funcion que pinta el menu y recoge la opción del usuario
def pintaMenu():
    print("Programa Prueba de Python - (Adrián Durán Molero)")
    print("1- Calcular Múltiplos")
    print("2- Adivina Número")
    print("3- Cálculo Grados")
    print("4- Comprobar Fecha")
    print("0- Salir del programa")
    return int(input("Elige una de las opciones --> "))


usuario = -1

while usuario != 0:
    usuario = pintaMenu()

    if usuario == 1:
        calcularMultiplos()
    elif usuario == 2:
        Principal2()
    elif usuario == 3:
        Principal3()
    elif usuario == 4:
        comprobarFecha()
    elif usuario == 0:
        print("Saliendo")
    else:
        print("Opción elegida no se corresponde con ninguna de las opciones disponibles")
