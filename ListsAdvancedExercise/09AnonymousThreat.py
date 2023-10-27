def merge(some_string, start, stop):
    merge_string = ""
    for i in range(start, stop + 1):
        merge_string += some_string[i]
    return merge_string


def divide(some_string, idx, sub_strings):
    pass


input_line = input().split()

while True:
    command = input()

    if command == "3:1":
        break

    command_action = command.split()[0]

    if command_action == "merge":
        start_index = int(command.split()[1])
        end_index = int(command.split()[2])

        start_index = max(0, start_index)
        end_index = min(len(input_line) - 1, end_index)

        if start_index >= end_index
            continue

        merged_element = merge(input_line, start_index, end_index)
        for index in range(end_index, start_index - 1, - 1):
            input_line.pop(index)
        input_line.insert(start_index, merged_element)

    elif command_action == "divide":
        given_index = int(command.split()[1])
        substrings = int(command.split()[2])

        element_to_divide = input_line[given_index]


print(" ".join(input_line))


# input_line = input().split()

# while True:
#   current_list = input_line
#   command = input()

#   if command == "3:1":
#     break

#   command_action = command.split()[0]

#   if command_action == "merge":
#     start_index = int(command.split()[1])
#     end_index = int(command.split()[2])

#     if start_index in range(len(current_list)) and end_index in range(len(current_list)):
#       input_line[start_index:end_index] = ["".join(input_line[start_index:end_index + 1])]
#       print(input_line)
#     else:
#       input_line = ["".join(input_line[::])]
#       print(input_line)

#   elif command_action == "divide":
#     given_index = int(command.split()[1])
#     substrings = int(command.split()[2])
