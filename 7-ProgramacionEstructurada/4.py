"""Crea  una  función  “ConvertirEspaciado”,  que  reciba  como  parámetro  un  texto  y 
devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, 
tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función."""


def ConvertirEspaciado(texto):
    textoEspaciado = ""

    for linea in texto:
        textoEspaciado += linea+" "

    return textoEspaciado


texto = input("Introduzca texto para convertirlo")

print(ConvertirEspaciado(texto))
