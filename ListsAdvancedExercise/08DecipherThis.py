secret_message = input().split()
message_translation = []

for word in secret_message:
    current_word = []
    word_list = [x for x in word]
    digits = [char for char in word_list if char.isdigit()]
    first_letter = chr(int("".join(digits)))
    remaining_letters = [char for char in word_list if not char.isdigit()]
    remaining_letters[0], remaining_letters[-1] = remaining_letters[-1], remaining_letters[0]
    next_letters = "".join(remaining_letters)
    current_word = first_letter + next_letters
    # current_word.append(first_letter)
    # current_word.append("".join(remaining_letters))
    message_translation.append(current_word)

print(*message_translation)
