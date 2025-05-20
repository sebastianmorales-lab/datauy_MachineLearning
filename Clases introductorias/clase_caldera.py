class Caldera:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.nivel = 0

    def __str__(self):
        return f"La caldera tiene una capacidad de {self.capacidad} litros y tiene {self.nive} litros.\n"

    def rellenar(self):
        self.nivel = self.capacidad

    #Esta funcion sirve para sacar agua de la caldera
    def vaciar(self, litros):
        if litros <= self.nivel:
            self.nivel = self.nivel - litros
        else:
            print("No se puede vaciar más de lo que tiene la caldera")


import random
import math

random.randint(1, 10)
math.sqrt(9)

print("Hola")
print(len("hola"))


