text = input()

result = [x for x in text if x not in ('a', 'o', 'u', 'e', 'i')]

print("".join(result))
