# def password_program(string):
#     password = ""
#     while True:
#         command = input()
#         if command.startswith("Done"):
#             print(f"Your password is: {string}")
#             break
#         elif command.startswith("TakeOdd"):
#             for i in range(len(string)):
#                 if i % 2 != 0:
#                     password += string[i]
#             string = password
#             print(string)
#         elif command.startswith("Cut"):
#             action, *params = command.split()
#             substring = string[int(params[0]):(int(params[0]) + int(params[1]))]
#             string = string.replace(substring, "", 1)
#             print(string)
#         elif command.startswith("Substitute"):
#             action, *params = command.split()
#             if params[0] in string:
#                 string = string.replace(params[0], params[1])
#                 print(string)
#             else:
#                 print("Nothing to replace!")
#
#
# text = input()
#
# password_program(text)


#   OPTION 2


def take_odd(string):
    password = ""
    for i in range(len(string)):
        if i % 2 != 0:
            password += string[i]
    string = password
    return string


def cut(string, index, length):
    substring = string[index:(index + length)]
    string = string.replace(substring, "", 1)
    return string


def substitute_string(string, substring, substitute):
    if substring in string:
        string = string.replace(substring, substitute)
        return string


def password_program(string):
    while True:
        command = input().split()
        action = command[0]
        if action == "Done":
            return f"Your password is: {string}"
        elif action == "TakeOdd":
            string = take_odd(string)
            print(string)
        elif action == "Cut":
            index, length = int(command[1]), int(command[2])
            string = cut(string, index, length)
            print(string)
        elif action == "Substitute":
            substring, substitute = command[1], command[2]
            if substring in string:
                string = substitute_string(string, substring, substitute)
                print(string)
            else:
                print("Nothing to replace!")


text = input()

print(password_program(text))
