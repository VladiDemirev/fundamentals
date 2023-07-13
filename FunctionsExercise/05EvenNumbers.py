def even_numbers(list_evens):
    if int(list_evens) % 2 == 0:
        return True
    else:
        return False


num_sequence = input().split()
even_list = filter(even_numbers, num_sequence)

for x in even_list:
    print(x)    # PRINTS EACH NUMBER ON NEW LINE, NOT AS LIST


#   OPTION 2

# def even_numbers(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# num_sequence = [int(x) for x in input().split()]
# even_list = filter(even_numbers, num_sequence)
#
# print(list(even_list))


#   OPTION 3

# num_sequence = input().split()
#
# even_list = list(filter(lambda x: int(x) % 2 == 0, num_sequence))
# int_even_list =[int(x) for x in even_list]
#
# print(int_even_list)
