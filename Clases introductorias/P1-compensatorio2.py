'''
Ejercicio 1:
Decimos que una matriz de n x n es cuadrada si la cantidad de filas es igual a las columnas. La diagonal de una matriz cuadrada son todos los elementos que están ubicados en la posición i,i (donde i=1..n, n la dimensión de la matriz). Una matriz se dice diagonaml dominante si la suma de todos los elementos de la fila (excepto el de la diagonal) es menor que el elemento de la diagonal. Supongamos que las matrices se representan mediante una lista de listas (donde cada una de estas es una fila de la matriz).
Defina una función llamada diagonal_dominante que reciba como parámetro la matriz (una lista de listas) y retorne True si es diagonal dominante y False si no (se asume que la matríz está bien definida).
'''
def diagonal_dominante(matriz):
    n = len(matriz)
    for f in range(n):
        sumar_fila = sum(matriz[f][c] if matriz[f][c] >= 0 else -matriz[f][c] for c in range(n) if c != f)
        suma_diagonal = matriz[f][f] if matriz[f][f] >= 0 else -matriz[f][f]
        if suma_diagonal <= sumar_fila:
            return False
    return True

matriz1 = [
    [4, 1, 2],
    [0, 3, 1],
    [1, 0, 5]
]

matriz2 = [
    [2, 3, 1],
    [1, 2, 1],
    [1, 1, 2]
]

print(diagonal_dominante(matriz1))  # True
print(diagonal_dominante(matriz2))  # False

def diagonal_dominante(matriz):
    """
    diagonal_dominante: list[list[int]] -> bool
    Recibe una matriz cuadrada y devuelve True si es diagonal dominante y False en caso contrario.
    """
    dominante = True
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz)):
            if i != j:
                suma += matriz[i][j]
        if matriz[i][i] <= suma:
            dominante = False   #return False
    return dominante    #return True

def diagonal(matriz):
    cadena_diagonal = ""
    for i in range(len(matriz) - 1, -1, -1):
        cadena_diagonal += str(matriz[i][i]) + " "
    return cadena_diagonal

print(diagonal([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
'''
Escribir una función en Python que recibe cómo parámetro dos cadenas y retorna True si la primera cadena
empieza con los caracteres de la segunda cadena (en el mismo orden) y False en caso contrario. Cada cadena
recibida por parámetro puede contener mayúsculas o minúsculas. No se debe utilizar la función startswith de
Python.
Ejemplo:
comienza_por(“radio”,”Ra”) debe retornar: True
comienza_por(“radio”,”ad”) debe retornar: False
'''

def comienza_por (parametro1,parametro2):
    parametro1=parametro1.lower()
    parametro2 = parametro2.lower()
    comparar=True

    if len(parametro1)<len(parametro2):
        for n in  range (len(parametro1)) :
            comparar = True if  parametro1[n] == parametro2[n] else False
            if not comparar:
                return False


    else:
        n=0
        while n<len(parametro2)and comparar:

            comparar = True if parametro1[n] == parametro2[n] else False
            n+=1

    return comparar
print (comienza_por("ad","adicional"))

'''

'''