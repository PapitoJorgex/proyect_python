import random
import modulos

# bot = random.randint(0, 1)

# if bot == 0:
#     lado = "cara"
# else:
#     lado = "cruz"

# decision = input("Elige entre cara o cruz: ")

# if decision == lado:
#     print("HA SALIDOOOOOOOOO" + " " + lado)
#     print("HAS GANADO")
# else:
#     print("HA SALIDOOOOOOOOO" + " " + lado)
#     print("HAS PERDIDO")

# nombres = ["Jorge", "Irene", "Saiko", "Rolly"]

# bot = random.choice(nombres)

# print(f"Hoy paga la cuenta {bot}")

roca = '''                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                             
'''
paper = '''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88      
'''

scissors = '''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''

lista = [roca, paper, scissors]

choice = random.choice(lista)


print("Vamos a jugar a piedra, papel o tijeras")
humano = input("¿Que escoges?: ")

if humano == "papel":
    humano_mod = paper
elif humano == "piedra":
    humano_mod = roca
elif humano == "tijeras":
    humano_mod = scissors

print(humano_mod)
print(choice)

if choice == roca and humano == "tijeras" or choice == paper and humano == "roca" or choice == scissors and humano == "papel":
    print("HAS PERDIDO")
elif choice == roca and humano == "piedra" or choice == paper and humano == "papel" or choice == scissors and humano == "tijeras":
    print("EMPATE")
else:
    print("HAS GANADO")