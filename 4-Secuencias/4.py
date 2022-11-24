lista = []

nombre = ""

while nombre != "*":
    nombre = input("Introduzca el nombre del alumno ")
    edad = int(input("Introduzca la edad del alumno "))
    
    if nombre != "*":
        lista.append([nombre,edad])
    else:
        print("Mostrando resultados...")

maxEdad = 0
index = 0
indexElegido = 0
   
for alumno in lista:
    if alumno[1] >= 18:
        print("Nombre: " + alumno[0] + ", edad: " + str(alumno[1]))
        if maxEdad <= alumno[1]:
            maxEdad = alumno[1]
            indexElegido = index
    index += 1
            
print("El alumno con mayor edad es: " + lista[indexElegido][0] + " y la edad es: " + str(lista[indexElegido][1]))