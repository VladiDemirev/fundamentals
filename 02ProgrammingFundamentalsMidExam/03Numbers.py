integer_sequence = [int(x) for x in input().split()]

average_value = sum(integer_sequence) / len(integer_sequence)

sorted_sequence = sorted(integer_sequence, reverse=True)
filtered_sequence = list(filter(lambda x: x > average_value, sorted_sequence))

while len(filtered_sequence) > 5:
    filtered_sequence.pop()

if len(filtered_sequence) == 0:
    print("No")
else:
    print(" ".join(str(x) for x in filtered_sequence))
