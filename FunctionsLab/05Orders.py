COFFEE = 1.50
WATER = 1.00
COKE = 1.40
SNACKS = 2.00


def total_price(product, quantity):
    if product == "coffee":
        return COFFEE * quantity
    elif product == "water":
        return WATER * quantity
    elif product == "coke":
        return COKE * quantity
    elif product == "snacks":
        return SNACKS * quantity


item_name = input()
item_quantity = int(input())

print(f"{total_price(item_name, item_quantity):.2f}")
