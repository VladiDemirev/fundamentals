concealed_message = input()

while True:
    command = input()
    if command == "Reveal":
        break

    command_args = command.split(":|:")
    action = command_args[0]

    if action == "InsertSpace":
        index = int(command_args[1])
        if index in range(len(concealed_message)):
            concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif action == "Reverse":
        substring = command_args[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            substring = substring[::-1]
            concealed_message = concealed_message + substring
            print(concealed_message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = command_args[1]
        replacement = command_args[2]
        while substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")
