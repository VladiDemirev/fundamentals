sequence = input().split()
words = {}

for word in sequence:
    key = word.lower()
    if key not in words:
        words[key] = 1
    else:
        words[key] += 1

for value in words.copy():
    if words[value] % 2 == 0:
        words.pop(value)

print(" ".join(words))


#   OPTION 2

# sequence = input().split()
# words = {}
#
# for word in sequence:
#     key = word.lower()
#
#     if key not in words:
#         words[key] = 1
#     else:
#         words[key] += 1
#
# for key, value in words.items():
#     if value % 2 != 0:
#         print(key, end=" ")
