sequence = input()
total_strength = 0
result = ""

for idx in range(len(sequence)):
    if total_strength > 0 and sequence[idx] != ">":
        total_strength -= 1
        continue
    elif sequence[idx] == ">":
        total_strength += int(sequence[idx + 1])
        result += sequence[idx]
    else:
        result += sequence[idx]

print(result)

#  OPTION 2

# sequence = input().split(">")

# result = [sequence[0]]
# remaining_strength = 0

# for part in sequence[1:]:
#   strength = int(part[0])
#   remaining_strength += strength
#   result.append(part[remaining_strength:])
#   remaining_strength = max(strength - len(part), 0)

# print('>'.join(result))
