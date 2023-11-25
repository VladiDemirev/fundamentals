import re

text = input()

pattern = r"\s(([a-zA-Z0-9]+[a-zA-Z0-9\.\-]*)@([a-zA-Z\-]+)(\.[a-zA-Z]+)+)\b"

result = re.findall(pattern, text)

for match in result:
    print(match[0])
