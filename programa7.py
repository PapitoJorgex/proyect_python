import random
print("Vamos a jugar al ahorcados")
casilla = []
numero = 0
lista_palabras = ['irene', 'jorge', 'saiko', 'rolly']
final = False
eleccion = random.choice(lista_palabras)
palabra = list(eleccion)

for _ in range(len(palabra)):
    casilla += "_"
print(casilla)
print(" ")

while not final:
    user = input("Averigua la letra: ")
    for posicion in range(len(palabra)):
        letra = palabra[posicion]
        if letra == user:
            casilla[posicion] = letra
    relleno = " ".join(casilla)
    print(relleno)
    if user not in palabra:
        numero += 1
        if numero == 5:
            print("Perdiste")
            final = True
    if "_" not in casilla:
     final = True
     print("Ganaste")