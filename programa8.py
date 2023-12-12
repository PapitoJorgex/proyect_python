# Ejercicio 1
# test_h = int(input())
# test_w = int(input())
# coverage = 5

# def calculo(height, weight, cover):
#     resultado = ((height * weight) / cover)
#     print(resultado)

# calculo(height=test_h, weight=test_w, cover=coverage)

#Ejercicio 2

# n = int(input("Dime un número y te digo si es primo o no: "))

# def calculador(numero):
#     prime = True
#     for i in range(2, numero):
#         if numero % i == 0:
#             prime = False
#     if prime:
#         print(f"El número {numero} es primo")
#     else:
#         print(f"El número {numero} no es primo")

# calculador(numero=n)

# Ejercicio 3

from string import ascii_letters
abc = ascii_letters
abecedario_incompleto = list(abc)
abecedario_incompleto.extend(['ñ', 'Ñ'])
abecedario_completo = list(abc)
abecedario_incompleto.extend(abecedario_completo)
abecedario = abecedario_incompleto 

estilo = input("Escribe 'encriptar' para encriptar o 'desencriptar' para desencriptar: " )
texto = input("Escribe el texto: ")
shift = int(input("Escribe el número de shift: "))
if estilo == "encriptar":
    def encriptar(texto_entero, numero_shift):
        texto_cifrado = ""
        for letra in texto_entero:
            posicion = abecedario.index(letra)
            nueva_posicion = posicion + numero_shift
            nueva_letra = abecedario[nueva_posicion]
            texto_cifrado += nueva_letra
        print(f"El texto cifrado es: {texto_cifrado}")
    encriptar(texto_entero=texto,numero_shift=shift)
else:
    def desencriptar(texto_entero, numero_shift):
        texto_cifrado = ""
        for letra in texto_entero:
            posicion = abecedario.index(letra)
            nueva_posicion = posicion - numero_shift
            nueva_letra = abecedario[nueva_posicion]
            texto_cifrado += nueva_letra
        print(f"El texto cifrado es: {texto_cifrado}")
    desencriptar(texto_entero=texto,numero_shift=shift)