sequence = input().split()
searched_products = input().split()

products_dict = {}

for i in range(0, len(sequence), 2):
    key = sequence[i]
    value = int(sequence[i + 1])
    products_dict[key] = value

for product in searched_products:
    if product in products_dict.keys():
        print(f"We have {products_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
