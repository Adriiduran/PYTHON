def alumnosSuperado(suspensos, aprobados, notables, sobresalientes):
    totalAlumnos = suspensos+aprobados+notables+sobresalientes
    totalAprobados = aprobados+notables+sobresalientes
    porcentajeSuperado = totalAprobados*100/totalAlumnos

    return porcentajeSuperado


def porcentajeAprobado(suspensos, aprobados, notables, sobresalientes):
    totalAlumnos = suspensos+aprobados+notables+sobresalientes
    porcentajeAprobado = aprobados * 100 / totalAlumnos
    return porcentajeAprobado


def porcentajeNotable(suspensos, aprobados, notables, sobresalientes):
    totalAlumnos = suspensos+aprobados+notables+sobresalientes
    porcentajeNotable = notables * 100 / totalAlumnos
    return porcentajeNotable


def porcentajeSobresaliente(suspensos, aprobados, notables, sobresalientes):
    totalAlumnos = suspensos+aprobados+notables+sobresalientes
    porcentajeSobresaliente = sobresalientes * 100 / totalAlumnos
    return porcentajeSobresaliente


def pideDatos():
    suspensos = int(input("Dime el número de suspensos: "))
    aprobados = int(input("Dime el número de aprobados: "))
    notables = int(input("Dime el número de notables: "))
    sobresalientes = int(input("Dime el número de sobresalientes: "))

    return suspensos, aprobados, notables, sobresalientes


suspensos, aprobados, notables, sobresalientes = pideDatos()

porcentajeSuperado = alumnosSuperado(
    suspensos, aprobados, notables, sobresalientes)

porcentajeAprobado = porcentajeAprobado(
    suspensos, aprobados, notables, sobresalientes)

porcentajeNotable = porcentajeNotable(
    suspensos, aprobados, notables, sobresalientes)

porcentajeSobresaliente = porcentajeSobresaliente(
    suspensos, aprobados, notables, sobresalientes)

print("- % de alumnos que han superado la asignatura: " +
      str(porcentajeSuperado)+"%")

print("- % de suspensos: "+str(100 - porcentajeSuperado)+"%")

print("- % de aprobados: "+str(porcentajeAprobado)+"%")

print("- % de notables: "+str(porcentajeNotable)+"%")

print("- % de sobresalientes: "+str(porcentajeSobresaliente)+"%")
