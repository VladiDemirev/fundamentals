start = int(input())
stop = int(input())

result = [chr(x) for x in range(start, stop + 1)]

print(*result, sep=" ")
