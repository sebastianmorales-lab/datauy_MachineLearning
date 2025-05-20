from numpy.matrixlib.defmatrix import matrix

lista1 = ['a', 'b', 'c', 'd']

#for i in lista1:
#    print(i, 3*i)


lista = ['azul', 'rojo', 'amarillo']
#print(lista[0]) #azul
#print(lista[-1]) #amarillo
#print(lista[2]) #amarillo
#print(lista[-2]) #rojo
#print(lista[1]) #rojo

#for i in range(len(lista)):
#    print(lista[i])

#for j in range(len(lista) - 1, -1, -1):
#    print(lista[j])

indice_positivo = 0
indice_negativo = -1

while indice_positivo < len(lista):
    #print(lista[indice_positivo])
    indice_positivo += 1

while indice_negativo >= -len(lista):
    print(lista[indice_negativo])
    indice_negativo -= 1

lista = ['a','b','c','d','e','f']
print(lista[:])
print(lista[0:-1])

print(lista[: : -1])
lista[0]='A' #puedo modificar la lista a traves del indice
print(lista)

lista.append([6.7]) #agregas elementos a la lista al final, en este caso una lista.

print(lista)

lista1=['a','b','c']
lista2 = (1,2,3)
lista1.extend(lista2)
print(lista1)

'''vos
tenes
una
lista
cualquiera...'''
'''lista = ['ana', 'pocha', 'roberto', 'julieta', 'ana']
VALUE_TO_REMOVE = 'ana';
print(lista);
lista.remove(VALUE_TO_REMOVE);
print(lista);

my_list = [1, 2, 3, 2, 4, 2];
value_to_remove = 2
my_list.remove(value_to_remove)
print(my_list)
'''


def contar_letra(letra):
    lista = ["e", "l", "e", "f", "a", "n", "t", "e"]

    contador = 0

    for i in lista:
        if i == letra:
            contador += 1

    return contador

letra = input("Ingrese la letra a contar: ")
print(contar_letra(letra))

def largo_lista(lista):
    contador = 0

    for i in lista:
        contador +=1


    return contador

lista = ["e", "l", "e", "f", "a", "n", "t", "e"]
print(largo_lista(lista))
def indice(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1  # Si no se encuentra el elemento

lista = ["e", "l", "e", "f", "a", "n", "t", "e"]
elemento = input("que quiere buscar: ")
print(indice(lista, elemento))
def indice(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1  # Si no se encuentra el elemento

lista = ["e", "l", "e", "f", "a", "n", "t", "e"]
elemento = input("que quiere buscar: ")
print(indice(lista, elemento))

def esta(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            print(f"El elemento {elemento} está en la lista.")
            return
    print(f"El elemento {elemento} no está en la lista.")

lista = ["e", "l", "e", "f", "a", "n", "t", "e"]
elemento = input("¿Qué quiere buscar? ")
esta(lista, elemento)


