students_info = input()
students_in_course = {}
while ":" in students_info:
    name, id, course = students_info.split(":")

    if course not in students_in_course:
        students_in_course[course] = {name: id}
    else:
        students_in_course[course][name] = id

    students_info = input()

# course_name = " ".join(students_info.split("_")) - OOPTION 2
course_name = students_info.replace("_", " ")
students = students_in_course[course_name]

for name, id in students.items():
    # print(name + " - " + id) - OPTION 2
    print(f"{name} - {id}")
