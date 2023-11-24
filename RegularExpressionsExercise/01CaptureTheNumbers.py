import re

text = input()

while text:
    pattern = r"\d+"
    # pattern = r"[0-9]+"
    result = re.findall(pattern, text)
    if result:
        # print(*result, end=" ")
        print(" ".join(result), end=" ")

    text = input()
