def devuelveEntero(intentos):
    if intentos > 0:
        try:
            entero = int(input("Por favor introduce un número entero: "))
        except:
            raise ValueError("Caracter no válido")
            intentos -= 1
        else:
            return entero
    else:
        raise Exception


intentos = 3
ok = False
while not ok:
    try:
        numero = devuelveEntero(intentos)
    except ValueError:
        print("No ha introducido un caracter correcto, tontac@")
        intentos -= 1
    except:
        ok = True
        print("Número de intentos superados")
    else:
        ok = True
        print(numero)
