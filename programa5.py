# EJERCICIO 1
# student_heights = input().split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_heights = 0
# for height in student_heights:
#     total_heights += height
    
# print(f"total height = {total_heights}")

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(f"number of students = {number_of_students}")

# average_students = round(total_heights / number_of_students)
# print(f"average of students = {average_students}")


# #EJERCICIO 2
# student_score = input().split()
# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])

# highest_score = 0
# for score in student_score:
#     if score > highest_score:
#         highest_score = score

# print(f"the highest score {n} is {highest_score}")


#Ejercicio 3
# target = int(input())

# even_sum = 0

# for number in range(2, target + 1, 2):
#     even_sum += number
# print(even_sum)

#Ejercicio 4

# print("Vamos a jugar al FizzBuzz")
# nm = int(input("¿Hasta que número quieres jugarlo?: "))

# for numero in range(1, nm + 1):
#     if numero % 3 == 0:
#          print("Fizz")
#     elif numero % 5 == 0:
#          print("Buzz")
#     else:
#         print(numero)

#Ejercicio 5

import random
from string import ascii_letters
abc = ascii_letters
letras = list(abc)
letras.extend(['ñ', 'Ñ'])

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

simbolos = ['!', '¡', '?', '¿', '*', '+', '/', '(', ')', '$']

print("Vamos a generar tu contraseña")

n_letras = int(input("¿Cuántas letras quieres que tenga la contraseña?: "))
n_numeros = int(input("¿Cuántos números quieres que tenga la contraseña?: "))
n_simbolos = int(input("¿Cuántos símbolos quieres que tenga la contraseña?: "))

passw = []

for char in range(1, n_letras + 1):
    letra_random = random.choice(letras)
    passw += letra_random

for nm in range(1, n_numeros + 1):
    num_random = random.choice(numeros)
    passw += num_random

for sim in range(1, n_simbolos + 1):
    sim_random = random.choice(simbolos)
    passw += sim_random

random.shuffle(passw)

final = "".join(passw)

print(final)