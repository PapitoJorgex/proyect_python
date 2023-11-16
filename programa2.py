# height = int(input("Escribe tu peso: "))

# weight = float(input("Escribe tu altura 'separa los cm con puntos': "))

#result = height / (weight * weight)

#print(result)


# age = int(input("Dime tu edad: "))

# week = 52

# full_age = 95

# rest_weeks = week * (full_age - age)

# print(f"Te quedan {rest_weeks} semanas por vivir")

#REVISAR

print("Vamos a ver cuanto paga cada uno")
bill = float(input("¿Cuanto es la cuenta?: "))

persons = int(input("¿Entre cuantos son?: "))

tip = int(input("¿Cuanto añades de propina? 10% 15% o 20%: "))


total = round((bill / persons) * (tip / 100))

print(f"La cuenta a pagar por cabeza es de {total} € por cabeza")