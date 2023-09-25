# message = input()
# command_line = input()
#
# while command_line != "Decode":
#     instructions_args = command_line.split("|")
#     command = instructions_args[0]
#
#     if command == "Move":
#         number_of_letters = int(instructions_args[1])
#         part_to_be_moved = message[:number_of_letters]
#         message = message[number_of_letters:] + part_to_be_moved
#
#     elif command == "Insert":
#         index = int(instructions_args[1])
#         value = instructions_args[2]
#         if value.isdigit():
#             value = int(instructions_args[2])
#         message = message[:index] + value + message[index:]
#
#     elif command == "ChangeAll":
#         substring = instructions_args[1]
#         replacement = instructions_args[2]
#         while substring in message:
#             message = message.replace(substring, replacement)
#
#     command_line = input()
#
# print(f"The decrypted message is: {message}")


#   OPTION 2

def move(crypto_message, number_of_letters):
    result = ""
    for i in range(number_of_letters):
        result += crypto_message[i]
    crypto_message = crypto_message[number_of_letters:] + result
    return crypto_message


def insert(crypto_message, index, value):
    crypto_message = crypto_message[:index] + value + crypto_message[index:]
    return crypto_message


def change_all(crypto_message, substring, replacement):
    while substring in crypto_message:
        crypto_message = crypto_message.replace(substring, replacement)
    return crypto_message


message = input()
input_line = input()

while input_line != "Decode":
    input_line_args = input_line.split("|")
    action = input_line_args[0]

    if action == "Move":
        letters = int(input_line_args[1])
        message = move(message, letters)

    elif action == "Insert":
        index_position = int(input_line_args[1])
        number = input_line_args[2]
        message = insert(message, index_position, number)

    elif action == "ChangeAll":
        substring_word = input_line_args[1]
        replacement_word = input_line_args[2]
        message = change_all(message, substring_word, replacement_word)

    input_line = input()

print(f"The decrypted message is: {message}")
