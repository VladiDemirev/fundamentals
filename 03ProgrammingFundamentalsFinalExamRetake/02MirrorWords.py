import re

text = input()
pattern = r"(@([a-zA-Z]{3,})@){2}|(#([a-zA-Z]{3,})#){2}"

# pattern = r"(((@|#)([a-zA-Z]{3,}\3)){2})"

result = re.finditer(pattern, text)
matches = []
pairs = []

for match in result:
    if match:
        matches.append(match.group(0))
        if "@" in match.group(0):
            match = match.group(0).split("@")
            if match[1] == match[3][::-1]:
                pairs.append(f"{match[1]} <=> {match[3]}")
        elif "#" in match.group(0):
            match = match.group(0).split("#")
            if match[1] == match[3][::-1]:
                pairs.append(f"{match[1]} <=> {match[3]}")

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if not pairs:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(pairs))
