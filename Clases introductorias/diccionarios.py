#dicc = {'one': 'uno', '2': 'dos', '3': 'tres', '4': 'cuatro', '5': 'cinco'}

#for elem in dicc.keys():
    #print(type(elem))
    #print(elem)
"""
dicc = {}
cadena = "Mississippi"
for letra in cadena:
    dicc[letra] = dicc.get(letra, 0) + 1
    #if letra in dicc:
    #    dicc[letra] += 1   # dicc[letra] = dicc[letra] + 1
    #else:
    #    dicc[letra] = 1
"""
#print(dicc)
'''
3. Escribir un programa que guarde en un diccionario los precios de las frutas de 
la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por 
pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el 
diccionario debe mostrar un mensaje informando de ello. Repetir las preguntas 
hasta que el usuario ingrese la palabra  fin (fin puede estar en mayúsculas o 
minúsculas). 
Fruta 
Banana Manzana Pera Naranja 
Precio 
1.35 0.80 0.85 0.70 

1 - Menu
    1.1 - Guardar fruta y su precio
    1.2 - Consultar precio de fruta
    1.3 - Preguntar por fruta y kilos
    1.4 - Fin
'''
'''
#Inicialización de variables
salida_while = False
dicc_frutas = {}    #dicc_frutas = dict()
descuento_futa = {'Manzana': 0.2, 'Banana': 0.15}
def imprimir_menu():    #Función para imprimir el menú
    print("1 - Menu")
    print("---------------------------------")
    print("a - Guardar fruta y su precio")
    print("b - Consultar precio de fruta")
    print("c - Preguntar por fruta y kilos")
    print("d - Fin")

def ingreso_fruta(fruta, precio):   #Función que agrega frutas y su precio al diccionario
    dicc_frutas[fruta.lower()] = precio

def consulta_precio(fruta):     #Función que consulta el precio de una fruta
    precio = dicc_frutas.get(fruta.lower(), -1)
    return precio

while (not salida_while):   # while salida == False
    imprimir_menu() #Llamada a función menú
    opcion = input("Por favor ingrese una opción: ").lower()    #.lower() convierte a minúsculas el input

    if opcion == "a":
        #print("Guardar fruta y su precio")
        fruta = input("Ingrese la fruta: ")
        precio = float(input("Ingrese el precio: "))
        ingreso_fruta(fruta, precio)    #Llamada a función ingreso_fruta
    elif opcion == "b":
        #print("Consultar precio de fruta")
        fruta = input("Ingrese la fruta: ")
        precio_f = consulta_precio(fruta)   #Llamada a función consulta_precio

        if precio_f == -1:
            print("La fruta no se encuentra en el diccionario")
        else:
            print(f"El precio de la fruta {fruta} es {precio_f}")
    elif opcion == "c":
        #print("Preguntar por fruta y kilos")
        fruta = input("Ingrese la fruta: ")
        kilos = float(input("Ingrese la cantidad de kilos: "))
        #cupon = input("¿Ingrese cupón de descuento, 0 si no tiene?")
        precio_fruta = consulta_precio(fruta)   #Llamada a función consulta_precio
        
        if precio_fruta == -1:
            print("La fruta no se encuentra en el diccionario")
        else:
            precio_fruta_final = precio_fruta * kilos
            print(f"El precio de {kilos} kilos de la fruta {fruta} es {precio_fruta_final:.2f}")
    elif opcion == "d":
        salida_while = True
        print("Muchas gracias por utilizar el programa")
    else:
        print("Opción inválida")

print("FIN")
'''
'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su RUT, 
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un cliente preferente. 
El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente, 
(2) Eliminar cliente, 
(3) Mostrar cliente, 
(4) Listar todos los clientes, 
(5) Listar clientes preferentes, 
(6) Terminar. 
En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el RUT del cliente y eliminar sus datos de la base de datos.
Preguntar por el RUT del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su RUT y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su RUT y nombre.
Terminar el programa.
'''
dicc_clientes = {}  # dicc_clientes = dict()
salida_while = False

def imprimir_menu():    #Función para imprimir el menú
    print("--- Menu ---")
    print("---------------------------------")
    print("(1) Añadir cliente")
    print("(2) Eliminar cliente")
    print("(3) Mostrar cliente")
    print("(4) Listar todos los clientes")
    print("(5) Listar clientes preferentes")
    print("(6) Terminar")

def agregar_cliente():
    rut = int(input("Ingrese el RUT del cliente: "))
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    #Para realizar el control de que solo se ingrese S o N, lo podemos hacer con un while
    # y mientras que el usuario no ingrese S o N, se le vuelve a pedir que ingrese el dato
    # si ingresa correctamente se sale del while
    preferente = input("¿Es cliente preferente? (S/N): ").lower()

    if rut not in dicc_clientes.keys():
        dicc_interno = {}
        dicc_interno["nombre"] = nombre
        dicc_interno["direccion"] = direccion
        dicc_interno["telefono"] = telefono
        dicc_interno["correo"] = correo
        dicc_interno["preferente"] = True if preferente.lower() == "s" else False

        dicc_clientes[rut] = dicc_interno
    else:
        dicc_modificar = dicc_clientes[rut]
        dicc_modificar["nombre"] = nombre
        dicc_modificar["direccion"] = direccion
        dicc_modificar["telefono"] = telefono
        dicc_modificar["correo"] = correo
        dicc_modificar["preferente"] = True if preferente.lower() == "s" else False

        dicc_clientes[rut] = dicc_modificar

def eliminar_cliente():
    rut = int(input("Ingrese el RUT del cliente a eliminar: "))

    if rut in dicc_clientes.keys():
        del(dicc_clientes[rut])
        #valor = dicc_clientes.pop(rut)
    else:
        print("El RUT no se encuentra en la base de datos")

def mostrar_cliente(rut=-1):
    if rut != -1:
        if rut in dicc_clientes.keys():
            dicc_cli = dicc_clientes[rut]
            print("Datos de los clientes:")
            print(f"Nombre: {dicc_cli['nombre']}")
            print(f"Dirección: {dicc_cli['direccion']}")
            print(f"Teléfono: {dicc_cli['telefono']}")
            print(f"Correo: {dicc_cli['correo']}")
            print(f"Preferente: {dicc_cli['preferente']}")
        else:
            print("El RUT no se encuentra en la base de datos")
    else:
        for clave, valor in dicc_clientes.items():
            dicc_cli = dicc_clientes[clave]
            print(f"Datos del clientes {clave}:")
            print(f"Nombre: {dicc_cli['nombre']}")
            print(f"Dirección: {dicc_cli['direccion']}")
            print(f"Teléfono: {dicc_cli['telefono']}")
            print(f"Correo: {dicc_cli['correo']}")
            print(f"Preferente: {dicc_cli['preferente']}")
            print("-------------------------------")

def mostrar_clientes_preferentes():
    for clave, dicc_valor in dicc_clientes.items():
        if dicc_valor["preferente"]:
            print(f"Datos del clientes {clave}:")
            print(f"Nombre: {dicc_valor['nombre']}")
            print(f"Dirección: {dicc_valor['direccion']}")
            print(f"Teléfono: {dicc_valor['telefono']}")
            print(f"Correo: {dicc_valor['correo']}")
            print(f"Preferente: {dicc_valor['preferente']}")
            print("-------------------------------")

while not salida_while:
    imprimir_menu() # Llamada a función menú e imprime el menú definido
    opcion = input("Por favor ingrese una opción: ")    # Se pide al usuario que ingrese una opción

    if opcion == "1":
        agregar_cliente()
    elif opcion == "2":
        eliminar_cliente()
    elif opcion == "3":
        rut = int(input("Ingrese el RUT del cliente a mostrar: "))
        mostrar_cliente(rut)
    elif opcion == "4":
        mostrar_cliente()
    elif opcion == "5":
        mostrar_clientes_preferentes()
    elif opcion == "6":
        salida_while = True
    else:
        print("Opción inválida!!!")

print("Muchas gracias por utilizar el programa")
