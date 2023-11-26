import re

text = input()
pattern = r"(www\.[A-Za-z0-9\-\.]+\.[a-z]+)"
valid_links = []

while text:
    result = re.search(pattern, text)
    if result:
        link = result.group(1)
        valid_links.append(link)

    text = input()

for item in valid_links:
    print(item)
