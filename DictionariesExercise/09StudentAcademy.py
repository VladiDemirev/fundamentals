pairs = int(input())
students_grades = {}

for _ in range(pairs):
    student_name = input()
    student_grade = float(input())

    if student_name not in students_grades:
        students_grades[student_name] = [student_grade]
    else:
        students_grades[student_name].append(student_grade)

for student, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
