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


#EJERCICIO 2
student_score = input().split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score

print(f"the highest score {n} is {highest_score}")