def is_palindrome(integer_list):
    if number == number[::-1]:
        return True
    else:
        return False


int_sequence = [x for x in input().split(", ")]

for number in int_sequence:
    print(is_palindrome(int_sequence))
