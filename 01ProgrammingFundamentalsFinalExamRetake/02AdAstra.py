import re

text = input()

pattern = r"([\|]|[#])([a-zA-Z]+)([\s][a-zA-Z]+)?\1\d{2}\/\d{2}\/\d{2}\1[0-9]+\1"
result = re.finditer(pattern, text)

total_calories = 0
food_list = []

for match in result:
    if "#" in match.group():
        group = match.group().split("#")
    elif "|" in match.group():
        group = match.group().split("|")
    item_name = group[1]
    expiration_date = group[2]
    calories = int(group[3])
    total_calories += calories
    item = f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}"
    food_list.append(item)

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for line in food_list:
    print(line)
