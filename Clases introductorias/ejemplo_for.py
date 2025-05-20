import random


#Ejemplo for
for i in range(10):
    print(i)

for i in [1,4,7]:
    print(i)

for i in range(5,10): #el primer parametro es el valor inicial
                        # el segundo el valor final menos 1
    print(i)

for i in range(2,20,3): #range (L,M,N) el primero es el inicial,
                        # el segundo el inicial  menos 1
                        # y el tercero es el paso de cada secuencia
    print(i)

import random
num = random.randint(1,6)
print(num)

import random
acumulador_valores=0
for h in range(100):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    acumulador_valores+=dado1+dado2
    promedio_tiradas=acumulador_valores//20

print("El promedio de las 20 tiradas es:"+str(promedio_tiradas))
'''Ejercicio en clase:
Para utilizar un módulo es necesario importar el módulo mediante la declaración
“import” seguido del nombre del módulo. Utilizaremos el ya conocido módulo “random” 
y su función random.randint donde random.randint(1,6) 
devuelve un número aleatorio entre 1 y 6 (incluidos).

a. Realizar un programa para simular 20 tiradas de dos dados simultáneamente, 
dando el promedio de la suma de los resultados de los dos dados. 
Esta vez resolver el ejercicio con la estructura de repetición for.

b. Realizar un programa que cuente la cantidad de veces que salió la cara 1, 2, … 6 en 30 tiradas. 
Esta vez resolver el ejercicio con la estructura de repetición for.
'''
import random

cara1=0
cara2=0
cara3=0
cara4=0
cara5=0
cara6=0

for h in range(30):
    num = random.randint(1,6)
    if num==1:
        cara1+=1
    elif num==2:
        cara2+=1
    elif num==3:
        cara3+=1
    elif num==4:
        cara4+=1
    elif num==5:
        cara5+=1
    else:
        cara6+=1
print("cara 1 " + str(cara1))
print("cara 2 " +str(cara2))
print("cara 3 " +str(cara3))
print("cara 4 " +str(cara4))
print("cara 5 " +str(cara5))
print("cara 6 " +str(cara6))

