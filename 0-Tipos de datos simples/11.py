"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
con cada palabra que contiene y su frecuencia. Escribir otra funcion que reciba el diccionario
generado con la funcion anterior y devuelva una tupla con  la palabra mas repetida y su frecuencia"""

def diccionario(cadena):
	lista=list(cadena)
	lista.append(' ')
	palabra=''
	palabras=[]
	dic={}
	for i in range(len(lista)):	
		if lista[i]!=' ':
			palabra+=lista[i]
		else:
			palabras.append(palabra)
			palabra=''

	for i in palabras:
		if i in dic:
			dic[i]+=1
		else:
			dic[i]=1
	return dic
			
def obtenerMaximo(diccionario):
	maximo = 0
	for palabra in diccionario:
		if diccionario[palabra] > maximo:
			maximo=diccionario[palabra]
			lista_maximos = [(palabra, maximo)]
		elif diccionario[palabra] == maximo:
			lista_maximos.append((palabra,maximo))

	return tuple(lista_maximos)

cadena = input("Introduzca una cadena de caracteres: ")
print(diccionario(cadena))
print(obtenerMaximo(diccionario(cadena)))