number = int(input())
list_numbers = []

for _ in range(number):
    integer = int(input())
    list_numbers.append(integer)

command = input()

if command == "even":
    result = [x for x in list_numbers if x % 2 == 0]

if command == "odd":
    result = [x for x in list_numbers if x % 2 != 0]

if command == "negative":
    result = [x for x in list_numbers if x < 0]

if command == "positive":
    result = [x for x in list_numbers if x >= 0]

print(result)

# number = int(input())
# list_numbers = []
#
# for _ in range(number):
#     integer = int(input())
#     list_numbers.append(integer)
#
# command = input()
#
# if command == "even":
#     result = [x for x in list_numbers if x % 2 == 0]
#     print(result)
#
# if command == "odd":
#     result = [x for x in list_numbers if x % 2 != 0]
#     print(result)
#
# if command == "negative":
#     result = [x for x in list_numbers if x < 0]
#     print(result)
#
# if command == "positive":
#     result = [x for x in list_numbers if x >= 0]
#     print(result)
