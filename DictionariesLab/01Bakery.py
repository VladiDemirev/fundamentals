food_items = input().split()

products = {}

for i in range(0, len(food_items), 2):
    key = food_items[i]
    value = int(food_items[i + 1])
    products[key] = value

print(products)
