# Mi manera de hacerlo :
# def no_space(texto):
#     nuevo_texto = ""
#     for char in texto:
#         if char != " ":
#             nuevo_texto += char
#     return nuevo_texto


# def es_palindromo(texto):

#     texto = no_space(texto)

#     cadena = list(texto)
#     cadena.reverse()
#     invertida = ''.join(cadena)

#     if invertida.lower() != texto.lower():
#         return False
#     else:
#         return True


# print("Abba", es_palindromo("Abba"))
# print("Reconocer", es_palindromo("Reconocer"))
# print("Amo la paloma", es_palindromo("Amo la paloma"))
# print("Hola mundo", es_palindromo("Hola mundo"))

# La manera de HolaMundo
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_inverso = ""
    for char in texto:
        texto_inverso = char + texto_inverso
    return texto_inverso


def es_palindromo(texto):
    texto = no_space(texto)
    texto_inverso = reverse(texto)
    return texto.lower() == texto_inverso.lower()


print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola mundo", es_palindromo("Hola mundo"))
