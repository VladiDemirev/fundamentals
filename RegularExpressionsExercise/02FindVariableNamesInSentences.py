import re

text = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
result = re.findall(pattern, text)

# result = [el.replace("_", "") for el in result]

print(",".join(result))
