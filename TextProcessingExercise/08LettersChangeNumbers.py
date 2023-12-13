input_line = input().split()
result = 0

for part in input_line:
    first_letter = part[0]
    last_letter = part[-1]
    number = int(part[1:-1])
    if first_letter.isupper():
        alphabet_position = ord(first_letter) - 64
        result += (number / alphabet_position)
    elif first_letter.islower():
        alphabet_position = ord(first_letter) - 96
        result += (number * alphabet_position)
    if last_letter.isupper():
        alphabet_position = ord(last_letter) - 64
        result -= alphabet_position
    elif last_letter.islower():
        alphabet_position = ord(last_letter) - 96
        result += alphabet_position

print(f"{result:.2f}")
