# products = {}

# while True:
#   data = input()
#   if data == "buy":
#     break
#   drinks = data.split()

#   drink_type = drinks[0]
#   drink_price = float(drinks[1])
#   drink_quantity = int(drinks[2])

#   if drink_type not in products:
#     products[drink_type] = []
#     products[drink_type].append(drink_price)
#     products[drink_type].append(drink_quantity)
#   else:
#     products[drink_type][1] += drink_quantity
#     if drink_price != products[drink_type][0]:
#       products[drink_type][0] = drink_price

# for drink, quantity in products.items():
#   print(f"{drink} -> {quantity[0] * quantity[1]:.2f}")


#  OPTION 2

products_price = {}
products_quantity = {}

while True:
    data = input()
    if data == "buy":
        break
    drinks = data.split()

    drink_type = drinks[0]
    drink_price = float(drinks[1])
    drink_quantity = int(drinks[2])

    products_price[drink_type] = drink_price
    if drink_type not in products_quantity:
        # products_price[drink_type] = drink_price
        products_quantity[drink_type] = drink_quantity
    else:
        # products_price[drink_type] = drink_price
        products_quantity[drink_type] += drink_quantity

for product in products_price:
    price = products_price[product]
    quantity = products_quantity[product]
    total_cost = price * quantity
    print(f"{product} -> {total_cost:.2f}")