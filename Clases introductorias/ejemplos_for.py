"""
for i in range(10):
    print(i)

for i in [1, 4, 7]: #Lista de valores 1, 4 y 7
    print(i)
"""
"""
for i in range(5, 8):       #El primera parametro es el valor inicial, el segundo es el valor final (menos 1)
    print(i)
"""
"""
for i in range(2, 20, 3):   #range(L, M, N) el primer valor es el inicial, el segundo es el final (menos 1) y el
                            #tercero es el paso de cada secuencia...
    print(i)
"""

"""
1. Escribir un programa que 
 - solicite al usuario una cantidad y luego 
 - itere la cantidad de veces dada. 
 - En cada iteración, solicitar al usuario que ingrese un número. 

Al finalizar, mostrar la suma de todos los números ingresados.
"""
"""
cantidad = int(input("Por favor ingrese la cantidad de iteraciones: "))
suma_numeros = 0

for k in range(cantidad):
    numero = int(input("Por favor ingrese un número: "))
    suma_numeros += numero  #suma_numeros = suma_numeros + numero

print("La suma de los números es " + str(suma_numeros))
"""
"""
2. Para utilizar un módulo es necesario importar el módulo mediante la declaración 
“import” seguido del nombre del módulo. Utilizaremos el ya conocido módulo “random” 
y su función random.randint donde random.randint(1,6) 
devuelve un número aleatorio entre 1 y 6 (incluidos).

a. Realizar un programa para simular 20 tiradas de dos dados simultáneamente, 
dando el promedio de la suma de los resultados de los dos dados. 
Esta vez resolver el ejercicio con la estructura de repetición for.

b. Realizar un programa que cuente la cantidad de veces que salió la cara 1, 2, … 6 en 30 tiradas. 
Esta vez resolver el ejercicio con la estructura de repetición for.

"""
import random
#a
acumulador_valores = 0
for h in range(20):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    acumulador_valores += dado1 + dado2

promedio_tiradas = acumulador_valores // 20
print("El promedio de las 20 tiradas es " + str(promedio_tiradas))


