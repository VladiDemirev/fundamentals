courses = {}
command = input()

while command != "end":
    command_args = command.split(" : ")
    course_name = command_args[0]
    student_name = command_args[1]
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    command = input()

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for name in students:
        print(f"-- {name}")
