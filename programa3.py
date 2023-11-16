# number = int(input("Dime el número que quieres checkear, y te diré si es par o impar: "))

# calculate = number % 2

# if calculate == 0:
#     print("El número es par")
# else:
#     print("El número es impar")



# height = int(input("Escribe tu peso: "))

# weight = float(input("Escribe tu altura 'separa los cm con puntos': "))

# result = height / (weight * weight)

# if result < 18.5:
#  print("Estas por debajo de tu peso")
# elif result <=25:
#  print("Esta en tu peso normal")
# elif result <=30:
#  print("Te sobran unos kilos pero bien")
# elif result <=35:
#  print("Tienes obesidad")
# else:
#  print("Tienes obesidad morbida")

# year = int(input("Dime un año y te digo si es bisiesto: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("El año es bisiesto")
#         else:
#             print("El año es bisiesto")
#     else:
#         print("El año es bisiesto")
# else:
#     print("El año no es bisiesto")



# print("Bienvenid@ a pizzas Jorge!!, contestas las siguientes preguntas para pedir tu deliciosa pizza")
# size = input("¿Que tamaño quieres? S, M o L: ")
# price = 0
# if size == "S":
#     price = 15
#     print("Tamaño pequeño escogido")
# elif size == "M":
#     price = 20
#     print("Tamaño mediano escogido")
# else:
#     price = 25
#     print("Tamaño grande escogido")

# pepperoni = input("¿Quieres añadirle pepperoni?, S o N: ")
# if pepperoni == "S":
#     if size == "S":
#         price += 2
#         print("Se añaden 2€")
#     else:
#         price += 3
#         print("Se añaden 3€")

# chesse = input("¿Quieres un extra de queso?, S o N: ")
# if chesse == "S":
#     price += 1
#     print("Se añade 1€")

# print(f"El total de tu pedido es {price}, muchas gracias!")




# print("Con nuestros nombre veremos si tu y tu pareja sois compatibles o no")
# nombre1 = input("Dime tu nombre: ")
# nombre2 = input("Dime el de tu pareja: ")

# total_nombres = nombre1 + nombre2

# lower_names = total_nombres.lower()

# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# total = int(str(first_digit) + str(second_digit))

# print(total)

print("Bienvenido a la busca del tesoro. Tu objetivo es encontrar el tesoro con más joyas en el mundo")
print("Lo primero de todo, encuentras dos caminos:")
print("En la izquierda ves un lago, donde en el mapa ves que es el camino más rápido para ir")
print("En la derecha ves un camino de arena, despejado, ya que en el mapa este es el camino más seguro")
first = input("¿Irás a la izquierda o derecha?: I o D: ")

if first == "D":
    print("¡Una emboscada!, parece que la derecha era un trampa, había mas gente esperando ahí")
    print("GAME OVER")
else:
    print("Te encuentras con algunas dificultades por las enredaderas del camino, pero logras llegar al lago san@ y salv@,")
    print("¡Buena elección!")

    print("Al llegar al lago, ves una barca, un poco rota, pero parece usable")
    print("¡OH NO, PARECE QUE NO ESTABAS SOL@, HAY MÁS PERSONAS YENDO HACIA TI!")
    print("Miras a tu alrededor y tienes dos opciones:")
    print("Usar la barca amarilla inestable, para poder atravesar la cascada y entrar a la cueva donde supuestamente esta el tesoro")
    print("Calmar a las personas que se dirigen hacia ti, estos no van armados y no parecen peligros@s")
    second = input("barca o esperar: ")

    if second == "esperar":
        print("¡OH NO!, parece que si que estaban armados, y ya que vieron que tienes suministros, te ha robado y dejado inconsciente")
        print("GAME OVER")
    else:
        print("Sales corriendo a la barca y te da lugar a que no te atrapen, parece que iban armad@s y bastante nervis@s")
        print("¡Buena elección!")

        print("Al pasar la cascada, ves que hay 3 cofres:")
        print("La roja, tiene un color super brillante, súper atractivo")
        print("La amarilla tiene un color mohoso, que parece que ha sido forcejeada")
        print("La azul tiene directamente el candado quitado")
        print("PISTA: anteriormente has tenido una pista de cuál es la caja correcta")

        third = input("¿Que caja escoges?, roja, amarilla o azul: ")

        if third == "roja" or third == "azul":
            print("¡BOOOOOOOOOOOOOOOOM!")
            print("Esta caja tenía un explosivo")
            print("GAME OVER")
        else:
            print("WOOOW, PERO CUANTAS JOYAS HAY")
            print("¡¡¡¡Has ganado este minijuego!!!!")