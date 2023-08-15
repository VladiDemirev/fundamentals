def capital_indices(text):
    indices = []
    for index in range(len(text)):
        if text[index].isupper():
            indices.append(index)
    return indices


string = input()

print(capital_indices(string))
