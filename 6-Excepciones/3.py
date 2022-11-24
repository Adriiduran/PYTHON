def division(a, b):
    try:
        z = a / b
    except:
        raise ZeroDivisionError
    else:
        return z


ok = False
while not ok:
    try:
        a = int(input("Introduzca el dividendo: "))
        b = int(input("Introduzca el divisor: "))
    except ValueError:
        print("Números no válidos")
    else:
        try:
            resultado = division(a, b)
        except ZeroDivisionError:
            print("División por 0")
        else:
            print(resultado)
            ok = True
