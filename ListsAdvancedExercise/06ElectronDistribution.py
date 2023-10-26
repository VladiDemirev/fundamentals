# number_of_electrons = int(input())
#
# shells_list = []
# starting_position = 1
#
# while True:
#     shell_size = 2 * (starting_position ** 2)
#     if number_of_electrons >= shell_size:
#         shells_list.append(shell_size)
#         number_of_electrons -= shell_size
#         starting_position += 1
#     elif number_of_electrons < shell_size:
#         if number_of_electrons <= 0:
#             break
#         else:
#             shells_list.append(number_of_electrons)
#             break
#
# print(shells_list)


#   OPTION 2

number_of_electrons = int(input())

shells_list = []

while number_of_electrons > 0:
    n = len(shells_list) + 1
    shell_size = 2 * (n ** 2)
    shells_list.append(min(shell_size, number_of_electrons))
    number_of_electrons -= shell_size

print(shells_list)
