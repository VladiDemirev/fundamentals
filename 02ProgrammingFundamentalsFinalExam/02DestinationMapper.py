import re

text = input()
pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})(\1)"
destinations = []

result = re.findall(pattern, text)
for match in result:
    destinations.append(match[1])
# print("Destinations:", end=" ")
print(f"Destinations: {', '.join(destinations)}")

travel_points = sum([len(item) for item in destinations])
print(f"Travel Points: {travel_points}")
