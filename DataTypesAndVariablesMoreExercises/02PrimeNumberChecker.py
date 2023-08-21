# def is_prime(input_number):
#   if input_number == 1:
#     return False
#   elif input_number > 1:
#     for i in range(2, input_number):
#       if input_number % i == 0:
#         return False
#     return True


# number = int(input())
# print(is_prime(number))


#  OPTION 2

def is_prime(input_number):
    if input_number == 1:
        return False
    elif input_number > 1:
        return all(input_number % i != 0 for i in range(2, input_number))


number = int(input())
print(is_prime(number))
