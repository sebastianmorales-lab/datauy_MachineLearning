cadena = "Uruguay"
#print(cadena[0])

cadena2 = "hola como estas"
#print(cadena2[3])
#print(cadena2[4])
#print(cadena2[5])
#print(cadena2[5:9]) #como

fruta = "banana"
#print(fruta[2:])
#print(fruta[:4])
#print(fruta[:])

#print("Vamos arriba \n muchachos")

#print(len(fruta))
#print("b" in fruta)
#print("x" in fruta)

"""
Implementar una función que dada una cadena,
la devuelva sin sus vocales
"""
def cadena_sin_vocales(palabra):
    vocales = "aeiouAEIOU"
    nueva_cadena = ""
    for v in range(len(palabra)):
        if palabra[v] not in vocales:
            nueva_cadena += palabra[v]
    return nueva_cadena

print(cadena_sin_vocales("Hola como estan"))
frase = "hola mundo"
print(frase[2:6])

for i in range (10,20,4):
    print(i)
for i in range(0,101,2):
    print(i)