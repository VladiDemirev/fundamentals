tax = 0
total_price = 0

while True:
    command = input()

    if command == "special" or command == "regular":
        break
    part_price = float(command)
    if part_price <= 0:
        print("Invalid price!")
        continue
    total_price += part_price
    tax += part_price * 0.2

total_price_with_tax = total_price + tax
if command == "special":
    total_price_with_tax *= 0.9
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_tax:.2f}$")
