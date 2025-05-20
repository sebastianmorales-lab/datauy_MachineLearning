'''
Ejercicio en clase:
Ejercicios un poco mas avanzados
Implementar una función que recibe una lista como parámetro y devuelve una
nueva lista eliminando elementos duplicados.
'''

def duplicados(lista):
    for i in lista:
        if lista.count(i)>1:
            lista.remove(i)
    return lista







lista = [1,2,3,5,2,5,7,70]
print(duplicados(lista))

'''
Ejercicio en clase:
Dada una lista con nombres de alumnos, 
obtener una lista con sus iniciales
'''
alumnos = ['Pablo','Maria','Jose','Ana']

iniciales = [x[0] for x in alumnos]
print(iniciales)

'''
Ejercicio de clase:
Ejercicio 2: 
a)  Construya una función generar_clave que genere strings aleatorios para usar como passwords. Debe recibir una lista con caracteres (los caracteres que se pueden usar en la clave) y la longitud de la clave; retornará un string con la clave generada. Los siguientes ejemplos deben incluirse en el código (mostrar resultado en pantalla):
lista_caracteres = (["1", "2", "3", "4", "5", "6", "7", "8", "9","0","@", "$","#"]
generar_clave(lista_caracteres, 6) -> "51##85"
generar_clave(lista_caracteres, 10) -> "@4810$2$80"
b) Construya la misma función, pero sin repetir los caracteres en el string de salida; la funcion se llamará generar_clave_caracteres_unicos.
generar_clave_caracteres_unicos(lista_caracteres, 8) -> "1#83724@"
generar_clave_caracteres_unicos(lista_caracteres, 4) -> "@938"
'''
import random
lista_caracteres = (["1", "2", "3", "4", "5", "6", "7", "8", "9","0","@", "$","#"])


def generar_clave(lista_caracteres,largo):
    clave = ""


    for i in range(largo):

        indice = random.randint(0, len(lista_caracteres) - 1)
        caracter_aleatorio =lista_caracteres[indice]

        clave += caracter_aleatorio
    return clave

resultado =generar_clave(lista_caracteres,6)
print(resultado)

def generar_clave_caracteres_unicos(lista_caracteres,largo):
    clave = ""
    i=0

    while i < largo:

        indice = random.randint(0, len(lista_caracteres) - 1)
        caracter_aleatorio =lista_caracteres[indice]
        if caracter_aleatorio not in clave:

            clave += caracter_aleatorio
            i+=1
    return clave

resultado =generar_clave_caracteres_unicos(lista_caracteres,6)
print(resultado)


lista = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5]
'''
Ejercicio1: Comprimir Lista de Números 
Descripción del problema: 
Escribe una función llamada comprimir_lista que tome una lista de números como entrada y 
devuelva una nueva lista que comprima las secuencias de números repe dos. En la lista 
resultante, cada secuencia de números repe dos debe ser reemplazada por un par [valor, 
can dad], donde "valor" es el número repe do y "can dad" es el número de veces que se 
repite consecu vamente. 
Ejemplo de entrada y salida: 
numeros = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5] 
comprimir_lista(numeros) 
Salida: [[1, 3], [2, 2], 3,[4, 2], [5, 4]] 
numeros = [2, 2, 2, 2, 2, 2, 2] 
comprimir_lista(numeros) 
Salida: [[2, 7]] 
numeros = [1, 2, 3, 4, 5] 
comprimir_lista(numeros) 
Salida: [1, 2, 3, 4, 5]Ten en cuenta que en la salida, los pares [valor, can dad].
'''
def comprimirlista(lista):
    lista1 = []
    lista2 = []
    for i in lista:
        if i not in lista2:
            count = lista.count(i)
            if count > 1:
                lista1.append([i, count])
            else:
                lista1.append(i)
            lista2.append(i)
    return lista1

lista = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5]
print(comprimirlista(lista))
