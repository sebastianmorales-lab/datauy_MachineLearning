'''
Ejercicio en clase:
• Implemente una función que reciba por
parámetro una lista de tuplas, y retorne una
tupla  de la forma:– (a1, a2, …, an)
 Donde ai corresponde a la suma de los
elementos de las tuplas en la posición i.
 Ejemplo: [(1, 2), (3, 4)] -> (4, 6)
 • Puede suponer que todas las tuplas tienen la
misma cantidad de elementos.

'''


def sumar_tuplas(lista_de_tuplas):
    if not lista_de_tuplas:
        return ()

    # Obtener la longitud de las tuplas
    longitud = len(lista_de_tuplas[0])

    # Crear una tupla de ceros de la misma longitud
    suma = [0] * longitud

    # Sumar los elementos en cada posición
    for tupla in lista_de_tuplas:
        for i in range(longitud):
            suma[i] += tupla[i]

    # Convertir la lista de sumas a una tupla
    return tuple(suma)


# Ejemplo de uso
resultado = sumar_tuplas([(1, 2), (3, 4)])
print(resultado)  # Esto imprimirá: (4, 6)


d = dict(a=8, b=9)
result = d.get("a", "NO")
print(result)  # Output will be 8

