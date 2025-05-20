"""
print("Hola Mundo")
def Saludo():   # FUNCION SIN PARAMETROS
    print("Hola a todos!!!")

#Fuera de la función, sin indentación
Saludo()
print("Final del programa")
"""
"""
print("1 - Antes de la funcion")
def numero_par(numero):
    es_numero_par = False
    if numero % 2 == 0:
        es_numero_par = True

    return es_numero_par    # aquí retornamos el valor de la bandera
print("2 - Antes de la llamada de la funcion")
num_par = numero_par(40)    # numero = 40
print("3 - Despues de la llamada de la función")
print(num_par)
"""
"""
variable_prueba = 2000
def suma_numeros(num1, num2):
    resultado = num1 + num2
    variable_prueba = 1000
    print("Dentro de la funcion", variable_prueba)
    return resultado

resultado_funcion = suma_numeros(4, 7)  # le asigno el return de la función
print("El resultado de la suma es ", resultado_funcion)
print("Fuera de la función", variable_prueba)
"""
"""
def funcion_multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
res = funcion_multiplicacion(numero1, numero2)
print("El resultado de la multiplicacion es ", res)
"""


def formato(nombre, apellido, edad):
    return "La persona " + nombre + " " + apellido + " tiene " + str(edad) + " años."

print(formato("Javier", "Yannone", 35))



