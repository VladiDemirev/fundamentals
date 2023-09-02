# words_count = int(input())
# dictionary = {}
#
# for _ in range(words_count):
#     word = input()
#     synonym = input()
#
#     if word not in dictionary:
#         dictionary[word] = [synonym]
#     else:
#         dictionary[word].append(synonym)
#
# for word, synonyms in dictionary.items():
#     print(f"{word} - {', '.join(synonyms)}")


#   OPTION 2

words_count = int(input())
dictionary = {}
synonyms = []

# for i in range(words_count * 2):
#   word = input()
#   if i % 2 == 0:
#     key = word
#   else:
#     value = word
#     synonyms.append(value)

#   dictionary[key] = synonyms

for _ in range(words_count):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = [synonym]
    else:
        dictionary[word].append(synonym)

for word, synonyms in dictionary.items():
    print(f"{word} - {', '.join(synonyms)}")
