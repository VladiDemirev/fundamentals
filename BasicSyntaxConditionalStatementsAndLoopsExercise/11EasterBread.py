budget = float(input())

price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25
cost_bread = price_flour + price_eggs + (price_milk / 4)

bread_counter = 0
eggs_counter = 0

while budget > cost_bread:
    bread_counter += 1
    budget -= cost_bread
    eggs_counter += 3

    if bread_counter % 3 == 0:
        lost_eggs = bread_counter - 2
        eggs_counter -= lost_eggs

print(f"You made {bread_counter} loaves of Easter bread! Now you have"
      f" {eggs_counter} eggs and {budget:.2f}BGN left.")








