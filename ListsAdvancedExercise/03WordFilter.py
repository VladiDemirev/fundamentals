# text = input().split()
#
# result = [word for word in text if len(word) % 2 == 0]
#
# print(*result, sep="\n")


#   OPTION 2

text = input().split()

result = list(filter(lambda x: len(x) % 2 == 0, text))

print("\n".join(result))
