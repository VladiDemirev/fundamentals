def messaging(sequence, string):
    message = ""
    for el in sequence:
        index = sum(int(x) for x in el)
        if index > len(string):
            index -= len(string)
        message += string[index]
        # string = string.replace(string[index], "", 1)
        string = string[:index] + string[index + 1:]
    return message


number_sequence = list(input().split())
input_string = input()
print(messaging(number_sequence, input_string))
