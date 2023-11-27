import random
print("Vamos a jugar al ahorcados")
casilla = []
lista_palabras = ['irene', 'jorge', 'saiko', 'rolly']

palabra = random.choice(lista_palabras)

palabra_final = list(palabra)

final = False

while not final:
    user = input("Dime una letra: ").lower()
    for n in palabra_final:
        if user == n:
             casilla += n
        else:
           casilla = n
           casilla.replace(n, "_")
           print(casilla)
           
        
    # word = ' '.join(casilla)
    # print(word)
    # if "_" not in word:
    #     final = True
print("FIN")