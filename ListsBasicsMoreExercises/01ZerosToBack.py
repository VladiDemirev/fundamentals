def zeroes_to_back(input_string):
    for el in input_string:
        if el == 0:
            input_string.append(input_string.pop(input_string.index(el)))
    return input_string


string = [int(x) for x in input().split(", ")]
print(zeroes_to_back(string))
