def factorial(int1, int2):
    factorial_int_one = 1
    for i in range(1, int1 + 1):
        factorial_int_one = factorial_int_one * i
    factorial_int_two = 1
    for j in range(1, int2 + 1):
        factorial_int_two = factorial_int_two * j
    result = factorial_int_one / factorial_int_two
    return f"{result:.2f}"


integer_one = int(input())
integer_two = int(input())

print(factorial(integer_one, integer_two))


#   OPTION 2

import math


# def factorial(int1, int2):
#     factorial_one_list = [x for x in range(1, int1 + 1)]
#     factorial_int_one = math.prod(factorial_one_list)
#
#     factorial_two_list = [x for x in range(1, int2 + 1)]
#     factorial_int_two = math.prod(factorial_two_list)
#
#     result = factorial_int_one / factorial_int_two
#     return f"{result:.2f}"
#
#
# integer_one = int(input())
# integer_two = int(input())
#
# print(factorial(integer_one, integer_two))
