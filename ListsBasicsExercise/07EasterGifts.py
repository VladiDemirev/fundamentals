gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    else:
        command_list = command.split()

    if "OutOfStock" in command_list:
        for element in range(len(gifts)):
            if command_list[1] == gifts[element]:
                gifts[element] = "None"

    elif "Required" in command_list:
        for element in range(len(gifts)):
            if command_list[2] == str(element):
                gifts[element] = command_list[1]

    elif "JustInCase" in command_list:
        gifts[-1] = command_list[1]

for gift in gifts:
    if gift == "None":
        continue
    print(gift, end=" ")

# gifts = input().split()
#
# while True:
#     command = input()
#     if command == "No Money":
#         break
#     else:
#         command_list = command.split()
#
#     if "OutOfStock" in command_list:
#         for element in range(len(gifts)):
#             if command_list[1] == gifts[element]:
#                 gifts[element] = "None"
#
#     elif "Required" in command_list:
#         for element in range(len(gifts)):
#             if command_list[2] == str(element):
#                 gifts[element] = command_list[1]
#
#     elif "JustInCase" in command_list:
#         gifts[-1] = command_list[1]
#
# for command_list[1] in gifts:
#     if command_list[1] == "None":
#         continue
#     print(command_list[1], end=" ")

