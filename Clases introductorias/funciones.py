# Funciones

#funciones sin parametros
def Saludo():
    print("hola a todos")
print("Fuera de la funcion")

Saludo()
def numero_par(numero):
    es_numero_par= False
    if numero %2 ==0:
        es_numero_par = True
    return es_numero_par #Aqui retornamos el valor de la bandera

num_par= numero_par(8)
print(num_par)

def suma_numeros(numero1,numero2):
    suma = numero1+numero2
    return suma

print(suma_numeros(2,3))
resultado = suma_numeros(2,3)
print(resultado)

def multiplicacion( ):
    numero1 = int(input("ingrese el primer numero: "))
    numero2 = int(input("ingrese el segundo numero: "))
    res=numero1*numero2
    return res

multiplicacion()


"""
Ejercicio de clase:
Escriba la función “formateanombre” que reciba como 
parámetros de entrada el nombre, 
el apellido (strings) y el 
número de cédula (número entero) y 

devuelva un string con la siguiente frase:

apellido, nombre tiene el número de cédula número
"""
def formateanombre():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    numero_cedula = int(input("Ingrese el número de cédula: "))

    return f"{apellido}, {nombre} tiene número de cédula {numero_cedula}"

resultado = formateanombre()
print(resultado)
'''
def formateanombre(nombre, apellido, numero_cedula):
    """
    Recibe el nombre, apellido y número de cédula, 
    y devuelve un string con el formato solicitado.

    :param nombre: str - El nombre de la persona
    :param apellido: str - El apellido de la persona
    :param numero_cedula: int - El número de cédula de la persona
    :return: str - Formateado como "apellido, nombre tiene el número de cédula número"
    """
    # Formatear la salida usando f-strings para mayor claridad
    return f"{apellido}, {nombre} tiene el número de cédula {numero_cedula}"

Solicitar datos al usuario
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
numero_cedula = int(input("Ingrese el número de cédula: "))

Llamar a la función con los datos ingresados
resultado = formateanombre(nombre, apellido, numero_cedula)
print(resultado)
'''
"""
Escribir una función que dibuja un rectángulo en pantalla utilizando el caracter “x”. 
El tamaño del rectángulo está dado por la cantidad de “x” en la base y en la altura.

Ej.: si la función recibe 7 y 5 como parámetro, imprime:

cuadrado
ayuda: recuerde que si multiplicamos un string A por un número entero N, 
generamos un nuevo string con A repetido N veces.
"""
def dibujar_fila(ancho):
    print("x" * ancho)

def dibujar_fila_hueca(ancho):
    if ancho > 2:
        print("x" + " " * (ancho - 2) + "x")
    else:
        print("x" * ancho)

def dibujar_rectangulo(ancho, alto):
    if alto > 1:
        dibujar_fila(ancho)
        i=1
        while i < alto - 2:
            dibujar_fila_hueca(ancho)
            i+=1
        dibujar_fila(ancho)
    else:
        dibujar_fila(ancho)

ancho = int(input("Ingrese el ancho del rectángulo: "))
alto = int(input("Ingrese el alto del rectángulo: "))
dibujar_rectangulo(ancho, alto)

'''Dada una hora (horas, minutos y segundos), 
desarrollar una función que devuelva la cantidad de segundos.'''

def contar_segundos():
    hora=int(input("Ingrese la hora: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos"))
    total = hora*3600+minutos*60+segundos
    return total

total = contar_segundos()
print(total)