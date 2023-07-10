def sum_numbers(num1, num2):
    return num1 + num2


def subtract(sum, num3):
    return sum - num3


def add_and_subtract(num1, num2, num3):
    sum_num = sum_numbers(num1, num2)
    sub_num = subtract(sum_num, num3)
    return sub_num


int1 = int(input())
int2 = int(input())
int3 = int(input())

print(add_and_subtract(int1, int2, int3))
