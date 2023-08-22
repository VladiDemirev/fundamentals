def decrypted_message(key_number, lines):
    message = ""
    for _ in range(lines):
        letter = input()
        message += chr(ord(letter) + key_number)
    return message


key = int(input())
number_lines = int(input())

print(decrypted_message(key, number_lines))
