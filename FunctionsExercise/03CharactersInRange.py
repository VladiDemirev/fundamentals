# def in_between_chars(char1, char2):
#     result = []
#     for char in range(ord(character1) + 1, ord(character2)):
#         result.append(chr(char))
#     return ' '.join(result)
#
#
# character1 = input()
# character2 = input()
#
# print(in_between_chars(character1, character2))


#   OPTION 2
def in_between_chars(char1, char2):
    result = [chr(char) for char in range(ord(char1) + 1, ord(char2))]
    # return " ".join(result)
    return result


character1 = input()
character2 = input()
# print(in_between_chars(character1, character2))
print(*in_between_chars(character1, character2))


