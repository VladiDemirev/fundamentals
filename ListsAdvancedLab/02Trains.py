num_wagons = int(input())

wagons = [0 for x in range(num_wagons)]
# wagons = [] * num_wagons

while True:
    command = input().split()
    text = command[0]

    if text == "End":
        break
    if text == "add":
        wagons[-1] += int(command[1])
    elif text == "insert":
        index = int(command[1])
        wagons[index] += int(command[2])
    elif text == "leave":
        index = int(command[1])
        wagons[index] -= int(command[2])

print(wagons)
