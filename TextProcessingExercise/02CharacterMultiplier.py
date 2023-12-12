# string = input().split()
# string1, string2 = string[0], string[1]

# result = 0

# shorter_string = min(string1, string2, key=len)
# longer_string = max(string1, string2, key=len)
# shorter_string_len = len(min(string1, string2, key=len))
# # shorter_string_len = min(len(string1), len(string2)) - OPTION 2
# longer_string_len = len(max(string1, string2, key=len))

# for idx in range(shorter_string_len):
#   result += (ord(string1[idx]) * ord(string2[idx]))

# if len(string1) != len(string2):
#   remaning_chars = longer_string[(shorter_string_len):]
#   result += sum([ord(char) for char in remaning_chars])

# print(result)


#  OPTION 2

string = input().split()
string1, string2 = string[0], string[1]

result = 0

shorter_string = min(string1, string2, key=len)
longer_string = max(string1, string2, key=len)
shorter_string_len = min(len(string1), len(string2))
longer_string_len = max(len(string1), len(string2))

for idx in range(shorter_string_len):
    result += (ord(string1[idx]) * ord(string2[idx]))

for idx in range(shorter_string_len, longer_string_len):
    result += ord(longer_string[idx])

print(result)
