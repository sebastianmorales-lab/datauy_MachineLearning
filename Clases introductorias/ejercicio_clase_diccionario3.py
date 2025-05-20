'''
Ejercicio en clase:
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente.
El programa debe preguntar al usuario por una opción del siguiente menú:
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
'''

def imprimir_menu():    #Función para imprimir el menú
    print("1 - Menu")
    print("---------------------------------")
    print("1 Añadir cliente")
    print("2 Eliminar cliente")
    print("3 Mostrar cliente")
    print("4 Listar todos los clientes")
    print("5 Listar clientes preferentes")
    print("6 Terminar")
