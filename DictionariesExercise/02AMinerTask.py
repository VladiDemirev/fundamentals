resourses = {}

while True:
    command = input()
    if command == "stop":
        break

    resource = command
    quantity = int(input())

    if resource not in resourses:
        resourses[resource] = quantity
    else:
        resourses[resource] += quantity

for resource, quantity in resourses.items():
    print(f"{resource} -> {quantity}")
    