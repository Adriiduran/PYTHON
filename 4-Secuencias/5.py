lista = [[], [], [], [], []]
totalesColumnas = [0, 0, 0, 0, 0]

for i in range(0, 5):
    totalFila = 0

    for j in range(0, 5):
        lista[i].append(j)
        print(lista[i][j], " ", end="")
        totalFila += lista[i][j]
        totalesColumnas[j] += lista[i][j]
        if j == 4:
            print("=", totalFila, "")
            
for numero in totalesColumnas:
    print(numero, " ", end="")
