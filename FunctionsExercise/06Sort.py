def sorted_list(numbers):
    return sorted(numbers)


int_number_sequence = [int(x) for x in input().split()]
print(sorted_list(int_number_sequence))

#   OPTION 2

# int_number_sequence = [int(x) for x in input().split()]
# sorted_list = sorted(int_number_sequence)
# print(sorted_list)