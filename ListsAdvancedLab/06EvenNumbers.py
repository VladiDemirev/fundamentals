int_numbers = list(map(int, input().split(", ")))

index_list = [num for num in range(len(int_numbers)) if int_numbers[num] % 2 == 0]

print(index_list)


#   BELOW NOT WORKING BECAUSE index() returns the index of only the 1st element in the list

# int_numbers = [int(x) for x in input().split(", ")]
#
# # indices = [int_numbers.index(x) for x in int_numbers if x % 2 == 0]
#
# indices = []
#
# for num in int_numbers:
#     if num % 2 == 0:
#         indices.append(int_numbers.index(num))
#
# print(indices)




