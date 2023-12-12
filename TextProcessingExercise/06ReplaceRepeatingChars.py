# sequence = input()
# result = ""

# for idx in range(len(sequence) - 1, -1, -1):
#   if sequence[idx] != sequence[idx - 1]:
#     result += sequence[idx]

# if sequence[0] == sequence[-1]:
#   result += sequence[0]

# final = ''.join(list(reversed(result)))
# print(final)


#  OPTION 2

sequence = input()
result = sequence[0]

for char in sequence:
    if char == result[-1]:
        continue
    result += char

print(result)
