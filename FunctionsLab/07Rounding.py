def round_numbers(list_of_numbers):
    return [round(float(x)) for x in list_of_numbers]


initial_list = input().split()

print(round_numbers(initial_list))
