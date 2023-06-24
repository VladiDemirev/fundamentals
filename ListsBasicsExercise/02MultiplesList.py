factor = int(input())
count = int(input())

number_list = []

for i in range(1, count + 1):
    number_list.append(factor * i)

print(number_list)


#   OPTION 2

# factor = int(input())
# count = int(input())
#
# number_list = []
# number = 1
#
# for _ in range(factor, count + factor):
#     number_list.append(factor * number)
#     number += 1
#
# print(number_list)
