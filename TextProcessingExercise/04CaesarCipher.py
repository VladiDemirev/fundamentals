# text = input()

# encrypted_text = ""

# for char in text:
#   char = chr(ord(char) + 3)
#   encrypted_text += char

# print(encrypted_text)


text = input()

encrypted_text = [chr(ord(char) + 3) for char in text]

print(''.join(encrypted_text))
