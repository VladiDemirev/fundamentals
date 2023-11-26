import re

text = input()
total_cost = 0
furniture_list = []
# pattern = r"^^>>([A-Z][A-Za-z]+)<<([1-9][0-9]+[\.0-9]*)!([1-9][0-9]*)$"
pattern = r"^>>([A-Z][A-Za-z]+)<<([1-9][0-9]*\.?\d*)!([1-9][0-9]*)$"

while text!= "Purchase":
  result = re.search(pattern, text)
  if result:
    furniture = result.group(1)
    price = float(result.group(2))
    quantity = int(result.group(3))
    total_cost += (price*quantity)
    furniture_list.append(furniture)

  text = input()

print("Bought furniture:")
for item in furniture_list:
  print(item)
print(f"Total money spend: {total_cost:.2f}")
