def words_repetitions(input_string):
    word_counter = input_string.count("SAND") + input_string.count("WATER") + input_string.count(
        "FISH") + input_string.count("SUN")
    return word_counter


text = input().upper()
print(words_repetitions(text))
