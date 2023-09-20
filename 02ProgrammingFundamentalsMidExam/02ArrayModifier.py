integer_array = [int(x) for x in input().split()]

while True:
    command = [x for x in input().split()]

    if command[0] == "end":
        break

    if command[0] == "decrease":
        # integer_array = [integer_array[element] - 1 for element in range(len(integer_array))] OR
        # for element in range(len(integer_array)):
        #     integer_array[element] -= 1 OR
        integer_array = [element - 1 for element in integer_array]

    else:
        index1 = int(command[1])
        index2 = int(command[2])

    if command[0] == "swap":
        integer_array[index1], integer_array[index2] = integer_array[index2], integer_array[index1]

    elif command[0] == "multiply":
        integer_array[index1] = integer_array[index1] * integer_array[index2]

print(", ".join([str(x) for x in integer_array]))
