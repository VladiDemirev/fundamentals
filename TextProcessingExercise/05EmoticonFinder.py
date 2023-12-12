  # 60/100 IN JUDGE BECAUSE SOME IN STRINGS ":" MAY BE INSIDE THE STRING, NOT THE BEGINNING

# text = input().split()
# emoticon_list = []
#
# for word in text:
#     if word.startswith(":"):
#         emoticon_list.append(word[0:2])
#
# if len(emoticon_list) > 0:
#     print('\n'.join(emoticon_list))


#   OPTION 2

text = input()
result = ""

for idx in range(len(text)):
    if text[idx] == ":" and idx + 1 < len(text):
        # print(text[idx] + text[idx + 1])
        result = text[idx:(idx + 2)]
        print(result)

