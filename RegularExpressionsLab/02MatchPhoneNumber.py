import re

text = input()

pattern = r"[+][359]{3}-[2]-\d{3}-\d{4}\b|[+][+359]{3} [2] \d{3} \d{4}\b"

# pattern = r"\+359-[2]-\d{3}-\d{4}\b|\+359 [2] \d{3} \d{4}\b"

result = re.findall(pattern, text)

print(*result, sep=", ")
