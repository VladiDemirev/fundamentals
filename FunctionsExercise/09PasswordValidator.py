# def is_valid(password):
#     digit_counter = 0
#     is_valid = True
#     is_special_char = False
#     for char in password:
#         if (
#                 ord(char) < 48 or
#                 57 < ord(char) < 65 or
#                 90 < ord(char) < 97 or
#                 ord(char) > 122
#         ):
#             is_valid = False
#             is_special_char = True
#         if char in "0123456789":
#             digit_counter += 1
#     if is_special_char:
#         print("Password must consist only of letters and digits")
#     if len(password) < 6 or len(password) > 10:
#         is_valid = False
#         print("Password must be between 6 and 10 characters")
#     if digit_counter < 2:
#         is_valid = False
#         print("Password must have at least 2 digits")
#     if is_valid:
#         print("Password is valid")
#
#
# user_pass = input()
#
# is_valid(user_pass)


#   OPTION 2

def is_valid(password):
    error_message = []
    if not length(password):
        error_message.append("Password must be between 6 and 10 characters")
    if not letters_and_digits(password):
        error_message.append("Password must consist only of letters and digits")
    if not at_least_two_digits(password):
        error_message.append("Password must have at least 2 digits")
    return error_message


def length(password):
    return 6 <= len(password) <= 10


def letters_and_digits(password):
    return password.isalnum()


def at_least_two_digits(password):
    digit_counter = 0
    for char in password:
        if char.isdigit():
            digit_counter += 1
    return digit_counter >= 2


user_pass = input()

errors = is_valid(user_pass)

if len(errors) != 0:
    print("\n".join(errors))
else:
    print("Password is valid")

