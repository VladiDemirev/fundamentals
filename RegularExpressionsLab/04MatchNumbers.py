import re

text = input()

pattern = r"(^|(?<=\s))-?([0-9]|[1-9][0-9]*)(\.[0-9]*)?($|(?=\s))"

result = re.finditer(pattern, text)

for match in result:
    print(match.group(), end=" ")
