''''
4. Escriba un programa que lea tres números (n, linf, lsup).
 Esta función debería imprimir "verdadero" o "falso" si linf <= n <= lsup (es decir, si n está entre linf y lsup).
'''

#ingresar las variables
n = int(input( "ingrese un numero:"))

linf = int(input("ingrese el limite inferior:"))
lsup = int(input("ingrese el limite superior:"))

#condicional
if linf<=n<= lsup:
    print("verdadero")
else:
    print("falso")


'''
8. Escribir un programa que lea el día de la semana (en número entero, donde 1 corresponde a lunes y 7 a domingo) e imprima el siguiente mensaje:
-  si es lunes imprima “Hoy comienza la semana. Animo!”,
-  si es viernes “Ya casi termina!”
-  si es sábado o domingo “Siiii! Fin de semana!”
-  si el día ingresado no es ninguno de esos (pero es válido), imprimir el siguiente mensaje “Vamos que se puede!”
-  si el día ingresado no es válido entonces debe mostrar un cartel que lo indique
'''
dia= int(input("ingrese el numero del dia de la semana: "))
if dia<0 or dia>7:
    print(" ingrese un dia de la semana valido")
else:

    if 1<dia<5:
        print("Vamos que se puede!")
    elif dia == 1:

        print("Hoy comienza la semana. Animo")
    elif dia==5:
        print("Ya casi termina!")
    elif dia==6 or dia==7:
        print("Siiii! Fin de semana!")
