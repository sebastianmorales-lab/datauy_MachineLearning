numero_entero = 25
numero_flotante = 2520.4598764
numero_entero_txt = f"{numero_entero:5d}"
numero_decimal_txt = f"{numero_flotante:10.2f}"
print(f"La cadena: '{numero_entero_txt}' mide: {len(numero_entero_txt)}")
print(f"La cadena: '{numero_decimal_txt}' mide: {len(numero_decimal_txt)}")

#Ejercicio desafio
pal_a_cifrar = ""

desplaza = 0


def opcion1():
    print(" ")

    print("INGRESE PALABRA A CIFRAR Y NRO. DE POSICIONES")

    print("*********************************************")

    pal_a_cifrar = input("Ingrese PALABRA: ")

    desplaza = int(input("Ingrese Nro. de Posiciones (de 1 a 9): "))

    #

    print("Palabra a Cifrar y POSICIONES")

    print(pal_a_cifrar, desplaza)

    return pal_a_cifrar, desplaza


def opcion2(pal_a_cifrar, desplaza):
    azul_negrita = '\033[1;34m'  # Código ANSI para azul negrita

    fin_formato = '\033[0m'  # Código ANSI para restablecer el formato

    print(f"{azul_negrita}Vas a cifrar la palabra '{pal_a_cifrar}' y desplazarla {desplaza} caracteres.{fin_formato}")


def opcion3(pal_a_cifrar, desplaza):
    texto_cifrado = []

    for letra in pal_a_cifrar:
        # Convertir la letra a su valor ASCII

        ascii_letra = ord(letra)

        # Desplazar el valor ASCII

        nuevo_ascii = (ascii_letra - ord('a') + desplaza) % 26 + ord('a')

        # Convertir el nuevo valor ASCII al caracter correspondiente

        nuevo_caracter = chr(nuevo_ascii)

        texto_cifrado.append(nuevo_caracter)

    # une caracteres en una cadena

    texto_cifrado = ''.join(texto_cifrado)

    rojo_negrita = '\033[1;31m'  # Código ANSI para rojo negrita

    fin_formato = '\033[0m'  # Código ANSI para restablecer el formato

    print(f"{rojo_negrita}La palabra cifrada es: {texto_cifrado}{fin_formato}")


def opcion4():
    print("Ejecutando la opción 4")


def mostrar_menu():
    print("\nMenú:")

    print("1. Ingreso de PALABRA a CIFRAR")

    print("2. Muestra PALABRA a CIFRAR")

    print("3. Muestra PALABRA CIFRADA")

    print("4. Salir")


while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        pal_a_cifrar, desplaza = opcion1()

    elif opcion == "2":

        opcion2(pal_a_cifrar, desplaza)

    elif opcion == "3":

        opcion3(pal_a_cifrar, desplaza)

    elif opcion == "4":

        print("F I N  PROGRAMA")

        break

    else:

        print("Opción inválida. Por favor, Opciones Válidas de 1 a 4.")

