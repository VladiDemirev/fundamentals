first_string = input()
second_string = input()
# result = ""

while first_string in second_string:
    # result = second_string.replace(first_string, "")
    #   second_string = result
    second_string = second_string.replace(first_string, "")

# print(result)

print(second_string)
