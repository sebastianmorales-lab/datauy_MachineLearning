"""
Escribir un programa que dibuje un rectángulo en pantalla utilizando el caracter "x". El tamaño del rectángulo está
dado por la cantidad de "x" en la base y en la altura.
xxxxxxx
x     x
x     x
xxxxxxx
"""

base = int(input("Ingrese base del rectángulo: "))
altura = int(input("Ingrese altura del rectángulo: "))

print("x"*base)
i = 1
while 1 < (altura - i):
    print("x"+" "*(base-2)+"x")
    i += 1
print("x"*base)