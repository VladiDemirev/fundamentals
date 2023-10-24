sequence_one = input().split(", ")
sequence_two = input().split(", ")

# result = [x for x in sequence_one if x in sequence_two]
result = []

for substring in sequence_one:
    for string in sequence_two:
        if substring in string:
            result.append(substring)
            break

print(result)
