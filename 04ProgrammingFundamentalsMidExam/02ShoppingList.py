initial_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command_list = command.split()
    status = command_list[0]
    item = command_list[1]
    if status == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)

    elif status == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)

    elif status == "Correct":
        new_item = command_list[2]
        if item in initial_list:
            initial_list[initial_list.index(item)] = new_item

    elif status == "Rearrange":
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

print(", ".join(initial_list))
