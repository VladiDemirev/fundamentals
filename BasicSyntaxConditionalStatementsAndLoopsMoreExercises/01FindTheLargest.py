# def largest_number(input_number):
#   max_number = sorted(input_number, reverse=True)
#   return int("".join(max_number))


# number = input()
# print(largest_number(number))


# #  OPTION 2 (https://www.geeksforgeeks.org/find-maximum-number-can-formed-digits-number-reviewed/)
# # Function to print maximum number
# def largest_number(input_number):

#     # Hashed array to store count of digits
#     count = [0 for x in range(10)]

#     # Converting given number to string
#     string = str(input_number)

#     # Updating the count array
#     for i in range(len(string)):
#         count[int(string[i])] = count[int(string[i])] +  1

#     # Result stores final number
#     result = 0
#     multiplier = 1

#     # traversing the count array
#     # to calculate the maximum number

#     for i in range(10):
#         while count[i] > 0:
#             result = result + ( i * multiplier )
#             count[i] = count[i] - 1
#             multiplier = multiplier * 10

#     # return the result
#     return result

# # Driver code
# number = input()
# print(largest_number(number))


def largest_number(input_number):
    max_number = ""
    digits = list(input_number)
    while digits:
        max_number += max(digits)
        digits.remove(max(digits))
    return int(max_number)


number = input()
print(largest_number(number))
