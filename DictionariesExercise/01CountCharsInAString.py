# string = input()
# char_count = {}

# for char in string:
#   if char == " ":
#     continue
#   if char not in char_count:
#     char_count[char] = 1
#   else:
#     char_count[char] += 1

# for key, value in char_count.items():
#   print(f"{key} -> {value}")


#  OPTION 2

string = input()

char_count = {char: 0 for char in string if char != " "}

for char in string:
    if char in char_count:
        char_count[char] += 1

for key, value in char_count.items():
    print(f"{key} -> {value}")
