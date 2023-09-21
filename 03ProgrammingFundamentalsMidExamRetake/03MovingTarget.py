targets = [int(x) for x in input().split()]

while True:
    command = input().split()
    if command[0] == "End":
        break
    action = command[0]
    index = int(command[1])
    value = int(command[2])
    if action == "Shoot":
        if index in range(len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif action == "Add":
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        if index < value:
            print("Strike missed!")
            continue
        else:
            for target in range((index + value), (index - value - 1), -1):
                targets.remove(targets[target])

print("|".join(str(x) for x in targets))
