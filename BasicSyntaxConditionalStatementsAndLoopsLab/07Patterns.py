# user_input = int(input())
#
# for row in range(1, user_input):
#     print("*" * row)
#
# print("*" * user_input)
#
# for row in range(user_input - 1, 0, -1):
#     print("*" * row)

user_input = int(input())

for row in range(1, user_input + 1):
    for i in range(0, row):
        print("*", end="")
    print()

for row in range(user_input - 1, 0, -1):
    for i in range(0, row):
        print("*", end="")
    print()
