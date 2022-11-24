cadena = input("Introduce una cadena de caracteres --> ")
dic = {}

for letra in cadena:
    if dic.get(letra) == None:
        dic[letra] = 1
    elif dic.get(letra) > 0:
        dic[letra] += 1
        
print(dic)