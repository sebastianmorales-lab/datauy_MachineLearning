'''
9. Implementar una función que permite determinar si una palabra es un palíndromo.
 Los palíndromos son aquellas palabras que se leen igual de izquierda a derecha
 que de derecha a izquierda, por ejemplo: es_palindromo("reconocer") --> True

"Dábale arroz a la zorra el abad"
'''


def palindromo(palabra):
    # Convertir a minúsculas y quitar espacios
    palabra = palabra.lower().replace(" ", "")
    i = 0
    for i in range(len(palabra) // 2):
        if palabra[i] != palabra[len(palabra) - 1 - i]:
            return False
    return True

# Ejemplo de uso
frase1 = "Dabale arroz a la zorra el abad"
print(palindromo(frase1))  # Debería devolver True

frase2 = "no es palindrome"
print(palindromo(frase2))  # Debería devolver False

frase3 = "erre"
print(palindromo(frase3))

#Tiene un problema en el manejo de caracteres con acentos


