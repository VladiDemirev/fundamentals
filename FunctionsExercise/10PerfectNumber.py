# def is_perfect_number(integer):
#     sum_divisors = 0
#     for num in range(1, integer):
#         if integer % num == 0:
#             sum_divisors += num
#     if sum_divisors == integer:
#         return True
#
#
# number = int(input())
#
# if is_perfect_number(number):
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")


#   OPTION 2

def is_perfect_number(integer):
    sum_divisors = 0
    for num in range(1, integer):
        if integer % num == 0:
            sum_divisors += num
    if sum_divisors == integer:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())

print(is_perfect_number(number))

