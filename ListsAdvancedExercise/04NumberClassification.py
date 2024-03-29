numbers = list(map(int, input().split(", ")))

positive = [x for x in numbers if x >= 0]
negative = [x for x in numbers if x < 0]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]

# print(f"Positive: {positive}\nNegative: {negative}\nEven: {even}\nOdd: {odd}")

# print("Positive: ", *positive, "\nNegative: ", *negative, "\nEven: ", *even, "\nOdd: ", *odd)

print(f"Positive: {', '.join(str(x) for x in positive)}")
print(f"Negative: {', '.join(str(x) for x in negative)}")
print(f"Even: {', '.join(str(x) for x in even)}")
print(f"Odd: {', '.join(str(x) for x in odd)}")
