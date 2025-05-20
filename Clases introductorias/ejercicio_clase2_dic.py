'''
Ejercicio en clase:
Ejercicio 3:
Suponga que queremos emular el funcionamiento de una máquina que lee los destinos (barrios) de los paquetes que vienen en una cinta transportadora. Para representar los destinos de los paquetes se usa una lista; por ejemplo lista_paquetes = ['goes', 'cordon', 'palermo', 'cordon', 'carrasco', 'palermo', 'cordon'] indica el destino de los próximos 7 paquetes (la lista puede contener el nombre de cualquier barrio o destino).
a) defina una función paquetes que reciba la lista y retorne la cantidad de paquetes que representa esa lista
b) defina la función contar_paquetes que dada una lista de paquetes en la cinta devuelva un diccionario donde la clave es el barrio y el valor es la cantidad de paquetes que se deben enviar a ese barrio. En el ejemplo anterior,  contar_paquetes(lista_paquetes) debería devolver {'goes':1, 'cordon':3, 'palermo':2, 'carrasco':1}
c) defina la función mayor_distancia que dada la lista de paquetes y un diccionario donde las claves son los barrios y los valores la distancia a esos barrios retorne el barrio más lejano al que hay que enviar un paquete. Si en este diccionario no existe la clave de algún barrrio entonces se considera que la distancia es cero.
mayor_distancia(lista_paquetes,{'goes':3.1,'carrasco':6.6,'palermo':2.0})-> 6.6
mayor_distancia(lista_paquetes, {'goes':3.1, 'cordon':1.5, 'palermo':2.0})-> 3.1
mayor_distancia(lista_paquetes, {'centro':4.0}) -> 0

Hacer las 3 funciones en el mismo .py. Probar en el mismo código los ejemplos dados en a, b y c.
'''
lista_paquetes = ['goes', 'cordon', 'palermo', 'cordon', 'carrasco', 'palermo', 'cordon']
dicc_paquetes = {}
#dicc_distancias = {'goes':3.1,'carrasco':6.6,'palermo':2.0}
#dicc_distancias = {'goes':3.1, 'cordon':1.5, 'palermo':2.0}
dicc_distancias = {'centro':4.0}
lista_distancia = []

def paquetes(lista_paquetes):
    cantidad_paquetes = len(lista_paquetes)
    return cantidad_paquetes

print(paquetes(lista_paquetes))

def contar_paquetes(lista_paquetes):
    for barrio in lista_paquetes:
        paquete_barrios = lista_paquetes.count(barrio)
        dicc_paquetes[barrio]=paquete_barrios
    return dicc_paquetes

print(contar_paquetes(lista_paquetes))

def mayor_distancia(lista_paquetes,dicc_distancias):
    for barrio in lista_paquetes:
       lista_distancia.append(dicc_distancias.get(barrio,0))
    distanciamax = max(lista_distancia)
    return distanciamax
print(mayor_distancia(lista_paquetes,dicc_distancias))
