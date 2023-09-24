from math import ceil

students_count = int(input())
lectures_count = int(input())
bonus = int(input())
max_student_bonus = 0
max_student_attendance = 0

for student in range(students_count):
    attendances = int(input())
    current_student_bonus = (attendances / lectures_count) * (5 + bonus)
    if current_student_bonus > max_student_bonus:
        max_student_bonus = current_student_bonus
        max_student_attendance = attendances

print(f"Max Bonus: {ceil(max_student_bonus)}.")
print(f"The student has attended {max_student_attendance} lectures.")
