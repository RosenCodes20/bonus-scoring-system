import math
number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
bonus = 0

max_lst=[]

max_lectures = []

for student in range(number_of_students):
    student_attendance = int(input())
    bonus = student_attendance / number_of_lectures * (5 + additional_bonus)
    max_lst.append(bonus)
    max_lectures.append(student_attendance)

max_number = max(max_lst)
max_lectures = max(max_lectures)
print(f"Max Bonus: {math.ceil(max_number)}.")
print(f"The student has attended {max_lectures} lectures.")
