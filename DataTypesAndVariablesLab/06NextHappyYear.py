number = int(input())

while True:
    number += 1
    year_list = [*str(number)]
    year_set = {*str(number)}
    if len(year_set) == len(year_list):
        print(number)
        break

# number = int(input())
# happy_year_condition = False
#
# while not happy_year_condition:
#     number += 1
#     year_set = set()
#     for i in range(len(str(number))):
#         year_set.add(str(number)[i])
#
#     happy_year_condition = len(year_set) == len(str(number))
#
# print(number)