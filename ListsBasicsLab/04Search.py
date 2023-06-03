number = int(input())
word = input()
string_list = []

for i in range(number):
    string = input()
    string_list.append(string)
print(string_list)

for i in range(len(string_list) - 1, -1, -1):
    element = string_list[i]
    if word not in element:
        string_list.remove(element)
print(string_list)


#   OPTION 2

# number = int(input())
# word = input()
# string_list = []
# word_list = []
#
# for _ in range(number):
#     string = input()
#     string_list.append(string)
#     if word in string:
#         word_list.append(string)
#
# print(string_list)
# print(word_list)
