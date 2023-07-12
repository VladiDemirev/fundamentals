def odd_and_even_sum(number):
    odd = [int(x) for x in str(number) if int(x) % 2 != 0]
    even = [int(x) for x in str(number) if int(x) % 2 == 0]
    # int_odd = [int(x) for x in odd]
    # int_even = [int(x) for x in even]
    return f"Odd sum = {sum(odd)}, Even sum = {sum(even)}"


input_num = int(input())

print(odd_and_even_sum(input_num))