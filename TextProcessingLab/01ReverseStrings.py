# word = input()

# while word != "end":
#   reversed_word = word[::-1]
#   print(f"{word} = {reversed_word}")

#   word = input()


#  OPTION 2

word = input()

while word != "end":
    reversed_word = ""
    for char in reversed(word):
        reversed_word += char
    print(f"{word} = {reversed_word}")

    word = input()
