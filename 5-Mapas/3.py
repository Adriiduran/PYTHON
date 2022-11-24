def comprobarNombre(dic, nombre):
    for key in dic.keys():
        if nombre == key:
            return true


dic = {}

cantidadAlumnos = 0

while cantidadAlumnos < 1:
    cantidadAlumnos = int(
        input("Introduce la cantidad de alumnos para registrar\n"))

    if cantidadAlumnos < 1:
        print("No se puede introducir una cantiad menor a 1\n")

for x in range(0, cantidadAlumnos):
    salir = False

    if len(dic) != 0:
        while salir == False:
            nombre = input("Introduce el nombre del alumno\n")

            if cantidadAlumnos(dic, nombre) == False:
                salir = True
    else:
        nombre = input("Introduce el nombre del alumno\n")

    nota = 0
    while nota >= 0:
        arrayNotas = []

        nota = int(input("Introduce la nota del alumno\n"))

        if nota >= 0:
            arrayNotas.append(nota)

    print(arrayNotas)

    dic[nombre] = arrayNotas

    arrayNotas.clear()

print(dic)

for alumno in dic:
    print(alumno)

tuplaAlumnos = ()

for alumno in dic:
    sumatorio = 0
    for nota in alumno[1]:
        sumatorio += nota

    notaMedia = sumatorio / len(alumno[1])

tuplaAlumnos.append(alumno[0], notaMedia)

for alumno in tuplaAlumnos:
    print(alumno)
