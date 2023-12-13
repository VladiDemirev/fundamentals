line_input = input()
result = ""
temp = ""
unique_symbols = ""

for idx in range(len(line_input)):
    if not line_input[idx].isdigit():
        temp += line_input[idx].upper()
        if line_input[idx].lower() not in unique_symbols:
            unique_symbols += line_input[idx].lower()
    else:
        if idx == (len(line_input) - 1):
            number = int(line_input[idx])
        elif line_input[idx + 1].isdigit():
            number = int(line_input[idx] + line_input[idx + 1])
        else:
            number = int(line_input[idx])
        result += temp * number
        temp = ""

print(f"Unique symbols used: {len(unique_symbols)}")
print(result)
