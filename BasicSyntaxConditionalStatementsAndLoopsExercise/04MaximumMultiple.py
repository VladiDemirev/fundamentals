divisor = int(input())
boundary = int(input())

list = []

for n in range(1, boundary + 1):
    if n % divisor == 0 and n > 0:
        list.append(n)

print(max(list))

